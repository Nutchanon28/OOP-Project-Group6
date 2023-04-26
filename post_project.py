from project import Project
import json
import requests
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

projects = [
    {
        "project_name": "projectttt",
        "category": "type1",
        "project_image": "#",
        "project_duration": "40",
        "pledge-goal": "32564",
        "project-detail": "description1"
    }
]


@app.get("/project-detail", tags=['Projects'])
async def get_project() -> dict:
    return {"Data": projects}

@app.get("/project-detail{project_id}", tags=['Projects'])
async def get_project(project_id: str) -> dict:
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

if __name__ == "__main__":
    main()
