from fastapi import FastAPI
from typing import Union

from project import Project
from system import System
from user import User

import json
from datetime import datetime

system = System()
user_jame = User(
    "Jame", "face_photo", "Just a simple guy", "Bangkok", "jame_project.com"
)
system.add_user(user_jame)
user_john = User(
    "John", "face_photo", "Founder of clean air for all", "Changmai", "clean_air.com"
)
system.add_user(user_john)

user_alice = User(
    "Alice",
    "face_photo",
    "Lover of all things tech",
    "San Francisco",
    "alice.tech",
)
system.add_user(user_alice)

user_bob = User(
    "Bob",
    "face_photo",
    "Adventurer and storyteller",
    "New York",
    "bobadventures.com",
)
system.add_user(user_bob)

project_vr_game = Project(
    "Virtual Reality Game",
    "gaming",
    "image",
    "12-4-2023",
    "Experience a new dimension of gaming with our immersive virtual reality game!",
    user_alice,
)
project_vr_game.add_reward(
    50, "Early Access", "Be one of the first to play our game!", "None", 200
)
project_vr_game.add_reward(
    100, "Custom Character", "Create your own character to use in the game!", "None", 100
)
system.launch_project(project_vr_game)

project_travel_blog = Project(
    "Around the World Travel Blog",
    "travel",
    "image",
    "15-5-2023",
    "Follow our journey around the world as we share stories, photos, and tips for traveling on a budget!",
    user_bob,
)
project_travel_blog.add_reward(
    25, "Travel Tips Ebook", "Learn our secrets for budget travel!", "digital", 500
)
project_travel_blog.add_reward(
    50,
    "Personalized Postcard",
    "Get a postcard from us during our travels!",
    "physical",
    100,
)
system.launch_project(project_travel_blog)

# John create a project "clean air for all"
project_clean_air = Project(
    "clean air for all",
    "health",
    "image",
    "11-4-2023",
    "A project by a guy who is passionate about the environment. Let's save lives by improving the air we breath.",
    user_john,
)

# John added a reward
project_clean_air.add_reward(150, "Oxygen Tank", "It's large", "1 oxygen tank", 100)

# John lauched the project
system.launch_project(project_clean_air)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/view_all_project", tags=["View Project"])
async def get_all_project() -> list:
    # SD: View All Project
    projects = system.launched_projects
    projects_detail = [project.get_project_detail() for project in projects]
    return projects_detail


@app.get("/view_project/{project_id}", tags=["View Project"])
async def get_project(project_id: int) -> dict:
    # SD: View Project
    # User select a project
    selected_project = system.get_project_from_id(project_id)
    project_detail = selected_project.get_project_detail()
    return project_detail


@app.get("/search_project", tags=["View Project"])
async def search_project(keyword: Union[str, None] = "", category: Union[str, None] = "all") -> list:
    # SD: Search Project
    searched_projects = system.search_project(keyword, category)
    projects_detail = [project.get_project_detail() for project in searched_projects]
    return projects_detail

@app.post("/send_comment/{project_id}", tags=["Send Comment"])
async def send_comment(project_id: int, text: str, user_id: int) -> str:
    # SD: Send Comment
    current_user = system.get_user_from_id(user_id)
    selected_project = system.get_project_from_id(project_id)
    selected_project.create_comment(datetime.now(), text, current_user.name)
    return "successful"
