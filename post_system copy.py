from system import System
import json
import requests
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

System = [
    {
        "project_list": "[p1, p2, p3]",
        "launched_projects": "[p1, p2]",
        "user_list": "[a, b, c]",
    }
]


@app.get("/project-detail", tags=['Projects'])
async def get_project() -> dict:
    return {"Data": projects}

@app.post("/project-detail", tags=['Projects'])
async def add_project(project: dict) -> dict:

    projects.append(project)
    return {
        "data": 'A Project is Added!'
    }

def main():
    #print("test")
    pass

if name == "main":
    main()