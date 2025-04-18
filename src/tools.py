import importlib
import os

def rprint(ipt: str):
    print(ipt)
    return ipt

def dynamic_import(module_name: str, attribute: str = None):
    """
    # 使用示例
    math_module = dynamic_import("math")
    print(math_module.sqrt(9))  # 3.0

    datetime_class = dynamic_import("datetime", "datetime")
    print(datetime_class.now())
    """
    try:
        module = importlib.import_module(module_name)
        return getattr(module, attribute) if attribute else module
    except (ImportError, AttributeError) as e:
        print(f"导入失败: {e}")
        return None
    

def agent_template(agent_name: str, exclude: bool=False) -> str:
    de = "" if exclude else "@agent"
    return f"""
    {de}
    def {agent_name}(self) -> Agent:
        return Agent(
            config=self.agents_config['{agent_name}'],
            llm=self.model
        )
    """

def task_template(task_name: str) -> str:
    return f"""
    @task
    def {task_name}(self) -> Task:
        return Task(config=self.tasks_config['{task_name}'])
    """

def crew_template_code(crew_json: dict, save_dir: str):
    save_dir = os.path.join("src", save_dir)
    config_dir = os.path.join(save_dir, "config")
    os.makedirs(save_dir, exist_ok=True)
    os.makedirs(config_dir, exist_ok=True)

    crew_name, process, works, agents, tasks = crew_json["name"], crew_json["type"], \
        crew_json["works"], crew_json["configs"]["agents"], crew_json["configs"]["tasks"]
    
    if process != "flow":
        is_hierarchical = process == "hierarchical"

        agent_yaml = "" 
        task_yaml = ""
        if is_hierarchical:
            with open("src/__templates__/hierarchical/agent.yaml", encoding="utf-8") as f:
                agent_yaml = f.read() 
            with open("src/__templates__/hierarchical/task.yaml", encoding="utf-8") as f:
                task_yaml = f.read()
        else: task_yaml = "\n".join(tasks)
        
        agent_yaml += ("\n" + "\n".join(agents))
        
        # wirte config
        with open(f"{config_dir}/agents.yaml", "w", encoding="utf-8") as f:
            f.write(agent_yaml.strip())
        with open(f"{config_dir}/tasks.yaml", "w", encoding="utf-8") as f:
            f.write(task_yaml.strip())
        
        work_names = [work["name"] for work in works]
        agent_code = ""
        manager_agent = "None"
        if is_hierarchical:
            agent_code += agent_template("manager_agent", exclude=True)
            manager_agent = "self.manager_agent()"
        
        for work_name in work_names:
            agent_code += agent_template(f"{work_name}_agent")
        
        task_code = ""
        if is_hierarchical: task_code = task_template("manager_task")
        else:
            for work_name in work_names:
                task_code += task_template(f"{work_name}_task")

        init_code = f"""
from .crew import {crew_name}Crew
__all__ = ['{crew_name}Crew']
"""
        
        crew_code = f"""
import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class {crew_name}Crew:
    model = LLM(
        model=os.getenv('OPENAI_MODEL_NAME'),
        api_key=os.getenv('OPENAI_API_KEY'),
        base_url=os.getenv('OPENAI_API_BASE')
    )

    {agent_code}
    {task_code}

    @crew
    def crew(self, **kwargs) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.{process},
            manager_agent={manager_agent},
            **kwargs
        )
    """

        # write code
        with open(f"{save_dir}/crew.py", "w", encoding="utf-8") as f:
            f.write(crew_code.strip())
        with open(f"{save_dir}/__init__.py", "w", encoding="utf-8") as f:
            f.write(init_code.strip())
    
    else:
        pass

