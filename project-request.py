from project import Project
import json
import requests
from typing import Optional
from fastapi import FastAPI

projects = {
        "project_name": "projectttt",
        "category": "type1",
        "project_image": "#",
        "project_duration": "40",
        "pledge-goal": "32564"
    }

r = requests.post("http://127.0.0.1:8000/project-detail", data=json.dumps(projects))
r = requests.post("http://127.0.0.1:8000/project-detail", data=json.dumps(projects))
r = requests.post("http://127.0.0.1:8000/project-detail", data=json.dumps(projects))
print(r)
print(r.json())

g = requests.get("http://127.0.0.1:8000/project-detail")
g = g.json()
print(g)