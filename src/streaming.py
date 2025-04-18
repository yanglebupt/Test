import asyncio
import os
import queue
from crewai.task import TaskOutput
    
class StreamingCallback():
    def __init__(self):
        self.messages = queue.Queue()
        self.should_yield = False
        self.need_over = False

    def over_callback(self, result: TaskOutput, **kwargs):
        self.log_paragraph(result.raw, **kwargs)
        self.need_over = True

    def step_callback(self, step, **kwargs):
        pass

    def task_callback(self, task, **kwargs):
        pass

    def log(self, text: str, event: str = "log", verbose = False):
        if event == "work":
            if not text.startswith("["): text = "[" + text
            text = "data: {" + "\"type\": \"" + event + "\", \"content\": " + text + "}\n\n"
        else:
            text = text.replace("\n", "\\n")
            text = "data: {" + "\"type\": \"" + event + "\", \"content\": \"" + text + "\"}\n\n"

        if verbose: print(text)
        self.messages.put(text)
        self.should_yield = True
    
    def log_paragraph(self, paragraph: str, **kwargs):
        # for text in paragraph.split("\n"):
        #    self.log(text, **kwargs)
        self.log(paragraph, **kwargs)

    # 监听文件变化
    async def read_log_filename(self, file_path: str, delay: float = 0.1, remove_at_end = True, **kwargs):
        # 初始状态
        last_size = 0
        last_mtime = 0
        
        while True:
            await asyncio.sleep(delay)
            if not os.path.exists(file_path): continue
            current_size = os.path.getsize(file_path)
            current_mtime = os.path.getmtime(file_path)
            
            if current_mtime != last_mtime or current_size != last_size:
                if current_size > last_size:
                    # 文件被追加了内容
                    with open(file_path, 'r') as f:
                        f.seek(last_size)
                        self.log_paragraph(f.read(), **kwargs)
            
                last_size = current_size
                last_mtime = current_mtime

            if self.need_over: break

        if remove_at_end: os.remove(file_path)

    async def iter_streaming_callback(self, delay: float = 0.1):
        while True:
            await asyncio.sleep(delay)
            if self.should_yield:
                while not self.messages.empty():
                    yield self.messages.get()
                self.should_yield = False
                if self.need_over: break
        