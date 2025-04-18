from pydantic import BaseModel

class CrewConfig(BaseModel):
    agents: list[str]
    tasks: list[str]

class CrewWork(BaseModel):
    name: str
    description: str

class CrewJson(BaseModel):
    name: str
    type: str
    language: str
    configs: CrewConfig
    works: list[CrewWork]

class CrewJsonBody(BaseModel):
    task_input: str
    crew_json: CrewJson