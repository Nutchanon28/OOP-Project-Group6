from fastapi import FastAPI
from typing import Union
from fastapi.middleware.cors import CORSMiddleware

from project import Project
from system import System
from user import User
from creditCardTransaction import CreditCardTransaction

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
    10000
)
project_vr_game.add_reward(
    50, "Early Access", "Be one of the first to play our game!", "None", 200
)
project_vr_game.add_reward(
    100,
    "Custom Character",
    "Create your own character to use in the game!",
    "None",
    100,
)
system.launch_project(project_vr_game)

project_travel_blog = Project(
    "Around the World Travel Blog",
    "travel",
    "image",
    "15-5-2023",
    "Follow our journey around the world as we share stories, photos, and tips for traveling on a budget!",
    user_bob,
    5000
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
    3300
)

# Green Energy for All
project_green_energy = Project(
    "Green Energy for All",
    "Technology",
    "green-energy.jpg",
    "5/1/2023 - 12/31/2023",
    "Join us in our mission to create sustainable energy solutions for everyone. Our team of experts is developing innovative technologies that will revolutionize the way we generate and consume energy.",
    user_john,
    7500
)

system.launch_project(project_green_energy)

# Artificial Intelligence for Business
project_ai_business = Project(
    "Artificial Intelligence for Business",
    "Business",
    "ai-business.jpg",
    "6/1/2023 - 11/30/2023",
    "Artificial intelligence is changing the game for businesses of all sizes. Our team of experienced developers and consultants is creating cutting-edge AI solutions that will help companies streamline operations, increase efficiency, and unlock new revenue streams.",
    user_alice,
    3200
)

system.launch_project(project_ai_business)

# Music Festival in the Park
project_music_festival = Project(
    "Music Festival in the Park",
    "Music",
    "music-festival.jpg",
    "7/15/2023 - 7/17/2023",
    "Join us for a weekend of live music, food, and fun in the park! Our lineup features local and national acts across a variety of genres, and all proceeds will go towards supporting the park's maintenance and community programs.",
    user_bob,
    8800
)

system.launch_project(project_music_festival)

# Open Source Educational Software
project_oss_edu = Project(
    "Open Source Educational Software",
    "Education",
    "oss-edu.jpg",
    "8/1/2023 - 12/31/2023",
    "We believe that education should be accessible to everyone. That's why we're developing a suite of open source educational software that anyone can use, modify, and share. Join us in our mission to democratize learning!",
    user_jame,
    6540
)

system.launch_project(project_oss_edu)

# Sustainable Clothing Line
project_sustainable_clothing = Project(
    "Sustainable Clothing Line",
    "Fashion",
    "sustainable-clothing.jpg",
    "9/1/2023 - 2/28/2024",
    "Fast fashion is taking a toll on our planet. That's why we're launching a sustainable clothing line made from eco-friendly materials and manufactured using ethical practices. Help us make fashion more sustainable!",
    user_alice,
    3500
)

system.launch_project(project_sustainable_clothing)

# Community Garden
project_community_garden = Project(
    "Community Garden",
    "Food",
    "community-garden.jpg",
    "10/1/2023 - 12/31/2023",
    "We're transforming an empty lot in the heart of the city into a vibrant community garden. Our vision is to create a space where anyone can come to grow, learn, and connect with their neighbors. Join us in creating a more sustainable and connected community!",
    user_bob,
    7700
)

system.launch_project(project_community_garden)

# Mental Health Chatbot
project_mental_health_chatbot = Project(
    "Mental Health Chatbot",
    "Health",
    "mental-health-chatbot.jpg",
    "11/1/2023 - 4/30/2024",
    "Mental health is just as important as physical health, but many people still struggle to access the care they need. That's why we're creating a chatbot that provides personalized mental health support and resources to anyone who needs it. Help us break down barriers to care!",
    user_bob,
    1234
)

system.launch_project(project_mental_health_chatbot)


# John added a reward
project_clean_air.add_reward(150, "Oxygen Tank", "It's large", "1 oxygen tank", 100)

# John lauched the project
system.launch_project(project_clean_air)

# country, cvc, expiration, card number
user_jame.add_payment_method("Thailand", "000", "06/25", "420694206928")
user_jame.add_payment_method("Thailand", "001", "06/25", "320694206928")
user_jame.add_payment_method("Thailand", "002", "06/25", "220694206928")

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/view_all_project", tags=["View Project"])
async def get_all_project() -> list:
    # SD: View All Project
    projects = system.launched_projects
    # projects_detail = [project.get_project_detail() for project in projects]
    projects_detail = []
    for project in projects:
        projects_detail.append(
            {
                "id": project.id,
                "name": project.project_name,
                "image": project.project_image,
                "detail": project.project_detail,
                "category": project.category,
            }
        )
    return projects_detail


@app.get("/view_project/{project_id}", tags=["View Project"])
async def get_project(project_id: int) -> dict:
    # SD: View Project
    # User select a project
    selected_project = system.get_project_from_id(project_id)
    project_detail = selected_project.get_project_detail()
    return project_detail


@app.get("/search_project", tags=["View Project"])
async def search_project(
    keyword: Union[str, None] = "", category: Union[str, None] = "all"
) -> list:
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


@app.post("/show_payment_requirements", tags=["Back the Project"])
async def show_payment_requirements(project_id: int, user_id: int) -> dict:
    # SD: Back the Project
    current_user = system.get_user_from_id(user_id)
    selected_project = system.get_project_from_id(project_id)
    project_detail = selected_project.get_project_detail()

    # This returns an entire CreditCardTransaction class, not sure if it will work
    payment_methods = current_user.payment_methods
    return {"project_detail": project_detail, "payment_methods": payment_methods}


@app.post("/back_the_project", tags=["Back the Project"])
async def back_the_project(
    project_id: int,
    user_id: int,
    reward_id: int,
    credit_card_id: int,
    bonus_cost: Union[int, None] = 0,
) -> dict:
    # SD: Back the Project
    current_user = system.get_user_from_id(user_id)
    selected_project = system.get_project_from_id(project_id)
    credit_card = current_user.get_credit_card_from_id(credit_card_id)
    reward = selected_project.get_reward_from_id(reward_id)
    response = current_user.back_project(
        selected_project, credit_card, reward, bonus_cost
    )
    return {"response": response}
