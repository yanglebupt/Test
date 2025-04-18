import asyncio
from contextlib import asynccontextmanager
from datetime import datetime
from __types__ import CrewJsonBody
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import inspect
import json
import hashlib
from streaming import StreamingCallback
from tools import dynamic_import, crew_template_code, rprint
import os
from dotenv import load_dotenv


@asynccontextmanager
async def lifespan(app: FastAPI):
    load_dotenv()
    model_name = os.getenv("OPENAI_MODEL_NAME")
    print(f"use LLM model: {model_name}") 
    yield

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def iterfile():
    while True:
        await asyncio.sleep(1)
        yield rprint(f"data: 这是第{1}行文本\n\n")

@app.get("/")
async def get_text_stream():
    return StreamingResponse(iterfile(), media_type="text/event-stream")

async def kickoff_crew(TaskCrew, sc: StreamingCallback, inputs: dict, **kwargs):
    result = await TaskCrew().crew(step_callback=sc.step_callback, task_callback=sc.task_callback, **kwargs) \
            .kickoff_async(inputs=inputs)
    # 等待日志先写入
    await asyncio.sleep(0.1)
    sc.over_callback(result, verbose=False, event="result")


@app.post("/crew-json")
async def crew_json_execute(body: CrewJsonBody):
    try:
        task_input, crew_json = body.task_input, body.crew_json.model_dump()
        project_name = crew_json["name"]
        json_str = json.dumps(crew_json, sort_keys=True, ensure_ascii=False)
        project_hash = hashlib.sha256(json_str.encode("utf-8")).hexdigest()
        project_root = project_name + "@" + project_hash

        # log 流
        log_dir = f"src/{project_root}/logs"
        human_friendly_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_filename = f"{log_dir}/{human_friendly_date}.json"
        sc = StreamingCallback()
        asyncio.create_task(sc.read_log_filename(log_filename, event="work"))

        if not os.path.exists(f"src/{project_root}"):
            crew_template_code(crew_json, project_root)
            os.makedirs(log_dir, exist_ok=True)
            sc.log(f"创建文件完成, 开始动态加载模块 {project_root}", verbose=True, event="log")

        # 动态加载
        generate_crewai = None
        while generate_crewai is None:
            await asyncio.sleep(0.1)
            generate_crewai = dynamic_import(project_root)

        TaskCrew = [cls for name, cls in inspect.getmembers(generate_crewai, inspect.isclass)][0]

        sc.log(f"{project_root} 模块加载完成, 开始执行 {TaskCrew.__name__}", verbose=True, event="log")
        
        asyncio.create_task(kickoff_crew(TaskCrew, sc, {"user_input": task_input}, verbose=True, output_log_file=log_filename))

        return StreamingResponse(sc.iter_streaming_callback(), media_type="text/event-stream")
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)