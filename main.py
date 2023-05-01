from fastapi import FastAPI
from typing import Union
from fastapi.middleware.cors import CORSMiddleware

from project import Project
from pledge_reward import PledgeReward
from reward_shipping import RewardShipping
from system import System
from user import User
from credit_card_transaction import CreditCardTransaction

import json
from datetime import datetime

system = System()

user_jame = User(
    "Jame@gmail.com", "1234", "Jame", "face_photo", "Just a simple guy", "Thailand", "jame_project.com"
)
system.add_user(user_jame)
user_john = User(
    "John@gmail.com", "2345", "John", "face_photo", "Founder of clean air for all", "Thailand",  "clean_air.com"
)
system.add_user(user_john)

user_alice = User(
    "Alice@gmail.com",
    "3456",
    "Alice",
    "face_photo",
    "Lover of all things tech",
     "Thailand", 
    "alice.tech",
)
system.add_user(user_alice)

user_bob = User(
    "Bob@gmail.com",
    "4567",
    "Bob",
    "face_photo",
    "Adventurer and storyteller",
     "Thailand", 
    "bobadventures.com",
)
system.add_user(user_bob)

#editttttttttttttttttt
user_anne = User(
    "Anne@gmail.com",
    "4567",
    "Anne",
    "face_photo",
    "Do you want to do this?",
    "Thailand", 
    "bobadventures.com",
)
system.add_user(user_anne)
user_anne.add_payment_method("USA", "000", "0000", "0000")
user_anne.add_payment_method("USA", "123", "0000", "0000")
user_anne.add_payment_method("USA", "456", "0000", "0000")

project_vr_game = Project(
    "Virtual Reality Game",
    "gaming",
    "image",
    "12-4-2023",
    user_alice,
    10000
)
project_vr_game.project_detail = "abcdef"

#editttttttttttttttt
system.add_project(project_vr_game)

thailand = RewardShipping("20-4-2023", ["Bankok", "A", "B", "C"])
project_vr_game.add_reward(
    50, "Early Access", "Be one of the first to play our game!", 200, "20-4-2023", ["Bankok", "A", "B", "C"]
)
project_vr_game.add_reward(
    100,
    "Custom Character",
    "Create your own character to use in the game!",
    100,
    "20-4-2023", ["Bankok", "A", "B", "C"]
)
system.launch_project(project_vr_game)

project_travel_blog = Project(
    "Around the World Travel Blog",
    "travel",
    "image",
    "15-5-2023",
    user_bob,
    5000
)
project_travel_blog.project_detail = "Follow our journey around the world as we share stories, photos, and tips for traveling on a budget!"
project_travel_blog.add_reward(
    25, "Travel Tips Ebook", "Learn our secrets for budget travel!", 500, "20-4-2023", ["Bankok", "A", "B", "C"]
)
project_travel_blog.add_reward(
    50,
    "Personalized Postcard",
    "Get a postcard from us during our travels!",
    100, "20-4-2023", ["Bankok", "A", "B", "C"]
)
system.launch_project(project_travel_blog)
project_travel_blog.add_update(
    "finished deal with publisher", 
    user_bob, 
    "make a big deal to print out 500 books in July in budget of 100 baht each", 
    "publisher.png"
)
project_travel_blog.add_update(
    "plan the place to go in July", 
    user_bob, 
    "70% of plan has finished even how much expen", 
    "publisher.png"
)
# John create a project "clean air for all"
project_clean_air = Project(
    "clean air for all",
    "health",
    "image",
    "11-4-2023",
    user_john,
    3300
)
project_clean_air.project_detail = "A project by a guy who is passionate about the environment. Let's save lives by improving the air we breath."
# Green Energy for All
project_green_energy = Project(
    "Green Energy for All",
    "Technology",
    "green-energy.jpg",
    "5/1/2023 - 12/31/2023",
    user_john,
    7500
)
project_green_energy.project_detail = "Join us in our mission to create sustainable energy solutions for everyone. Our team of experts is developing innovative technologies that will revolutionize the way we generate and consume energy."

system.launch_project(project_green_energy)

# Artificial Intelligence for Business
project_ai_business = Project(
    "Artificial Intelligence for Business",
    "Business",
    "ai-business.jpg",
    "6/1/2023 - 11/30/2023",
    user_alice,
    3200
)

system.add_project(project_ai_business)
project_ai_business = "Artificial intelligence is changing the game for businesses of all sizes. Our team of experienced developers and consultants is creating cutting-edge AI solutions that will help companies streamline operations, increase efficiency, and unlock new revenue streams."

system.launch_project(project_ai_business)

# Music Festival in the Park
project_music_festival = Project(
    "Music Festival in the Park",
    "Music",
    "music-festival.jpg",
    "7/15/2023 - 7/17/2023",
    user_bob,
    8800
)
project_music_festival.project_detail = "Join us for a weekend of live music, food, and fun in the park! Our lineup features local and national acts across a variety of genres, and all proceeds will go towards supporting the park's maintenance and community programs."

system.launch_project(project_music_festival)

# Open Source Educational Software
project_oss_edu = Project(
    "Open Source Educational Software",
    "Education",
    "oss-edu.jpg",
    "8/1/2023 - 12/31/2023",
    user_jame,
    6540
)
project_oss_edu.project_detail = "We believe that education should be accessible to everyone. That's why we're developing a suite of open source educational software that anyone can use, modify, and share. Join us in our mission to democratize learning!"

system.launch_project(project_oss_edu)

# Sustainable Clothing Line
project_sustainable_clothing = Project(
    "Sustainable Clothing Line",
    "Fashion",
    "sustainable-clothing.jpg",
    "9/1/2023 - 2/28/2024",
    user_alice,
    3500
)
project_sustainable_clothing.project_detail = "Fast fashion is taking a toll on our planet. That's why we're launching a sustainable clothing line made from eco-friendly materials and manufactured using ethical practices. Help us make fashion more sustainable!"

system.launch_project(project_sustainable_clothing)

# Community Garden
project_community_garden = Project(
    "Community Garden",
    "Food",
    "community-garden.jpg",
    "10/1/2023 - 12/31/2023",
    user_bob,
    7700
)
project_community_garden.project_detail = "We're transforming an empty lot in the heart of the city into a vibrant community garden. Our vision is to create a space where anyone can come to grow, learn, and connect with their neighbors. Join us in creating a more sustainable and connected community!"

system.launch_project(project_community_garden)

# Mental Health Chatbot
project_mental_health_chatbot = Project(
    "Mental Health Chatbot",
    "Health",
    "mental-health-chatbot.jpg",
    "11/1/2023 - 4/30/2024",
    user_bob,
    1234
)
project_mental_health_chatbot.project_detail = "Mental health is just as important as physical health, but many people still struggle to access the care they need. That's why we're creating a chatbot that provides personalized mental health support and resources to anyone who needs it. Help us break down barriers to care!"

system.launch_project(project_mental_health_chatbot)

# John added a reward
project_clean_air.add_reward(150, "Oxygen Tank", "It's large", 100, "20-4-2023", ["Bankok", "A", "B", "C"])

# John lauched the project
system.launch_project(project_clean_air)

# country, cvc, expiration, card number
user_jame.add_payment_method("Thailand", "000", "06/25", "420694206928")
user_jame.add_payment_method("Thailand", "001", "06/25", "320694206928")
user_jame.add_payment_method("Thailand", "002", "06/25", "220694206928")

user_jame.back_project(project_clean_air, user_jame.payment_methods[0], project_clean_air.pledge_rewards[0],1000)


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

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
                "creator":project.project_creator.name
            }
        )
    return projects_detail

@app.get("/view_project_list", tags=["View Project"])
async def get_project_list() -> list:
    projects = system.project_list
    return projects


@app.get("/view_backed_project", tags=["Backed Project"])
async def get_backed_project(user_id: int) -> list:
    # SD: View Backed Project??
    current_user = system.get_user_from_id(user_id)
    projects = current_user.get_backed_project()
    projects_detail = []
    for project in projects:
        projects_detail.append(
            {
                "id": project.id,
                "name": project.project_name,
                "image": project.project_image,
                "detail": project.project_detail,
                "category": project.category,
                "creator":project.project_creator.name
            }
        )
    return projects_detail

@app.get("/view_project/{project_id}", tags=["View Project"])
async def get_project(project_id: int) -> dict:
    # SD: View Project
    # User select a project
    #edittttttttttttttttttttttttttttttttt
    selected_project = system.get_project_in_project_list_from_id(project_id)
    project_detail = selected_project.get_project_detail()
    return project_detail

#edittttttttttttt
@app.get("/get_my_project/{user_id}", tags=["Project"])
async def get_my_project(user_id: int) -> list:
    my_projects = system.get_my_projects(user_id)
    return my_projects

@app.get("/search_project", tags=["View Project"])
async def search_project(
    keyword: Union[str, None] = "", category: Union[str, None] = "all"
) -> list:
    # SD: Search Project
# async def search_project(input: dict) -> list:
#     keyword = input["keyword"]
#     category = input["category"]
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

@app.get("/pledge_reward/{project_id}", tags=["Pledge Reward"])
async def get_pledge_reward(project_id: int) -> list:
    #editttttttttttttttttt
    project = system.get_project_in_project_list_from_id(project_id)
    rewards = project.pledge_rewards
    return rewards
    #reward_detail = project.get_pledge_reward_detail()
    #return reward_detail

@app.get("/view_all_project/{project_id}/get_reward_id", tags=["Pledge Reward"])
async def get_reward_id(project_id: int) -> dict:
    #edittttttttttttttt
    project = system.get_project_in_project_list_from_id(project_id)
    return {"id": str(len(project.pledge_rewards) + 1)}

@app.get("/get_last_project")
async def get_last_project():
    project = system.project_list
    #editttttttttt
    return {
        "id": project[-1].id,
        "detail": project[-1].get_project_detail()
    }

#editttttttttttt
@app.get("/get_last_reward_id/{project_id}", tags = ["Pledge reward"])
async def get_last_reward_id(project_id: int) -> dict:
    project = system.get_project_in_project_list_from_id(project_id)
    last_reward_id = project.get_last_reward().id
    return {"id": last_reward_id}

#editttttttttt
@app.get("/get_creditcard", tags=['creditcard'])
async def get_creditcard(user_id: int) -> list:
    user = system.get_user_from_id(user_id)
    creditcard = user.get_all_credit_card()
    return creditcard

@app.get("/get_project_credit_card/{project_id}", tags=["Project"])
async def get_project_credit_card(project_id: int):
    project = system.get_project_in_project_list_from_id(project_id)
    return project.credit_card

@app.post("/add_project", tags=["Add Project"])
async def add_the_project(project_dict: dict) -> str:
    #SD Start Project
    project = Project(
                        project_dict["project_name"], 
                        project_dict["category"],
                        project_dict["project_image"],
                        project_dict["project_duration"],
                        system.get_user_from_id(project_dict["creator_id"]),
                        project_dict["pledge_goal"]
                    )
    system.add_project(project)
    return "Success"

@app.post("/edit_project/{project_id}/add_pledge_reward", tags=["Pledge Reward"])
async def add_pledge_reward(project_id: int, pledge_reward: dict) -> str:
    #edittttttttttttttttttt
    project = system.get_project_in_project_list_from_id(project_id)
    project.add_reward(
        pledge_reward["_PledgeReward__reward_goal"],
        pledge_reward["_PledgeReward__reward_name"], 
        pledge_reward["_PledgeReward__reward_detail"], 
        pledge_reward["_PledgeReward__reward_left"], 
        pledge_reward["_RewardShipping__estimated_delivery"],
        pledge_reward["_RewardShipping__ships_to"]
    )

    return f"Add reward to project id {project_id}"

@app.put("/edit_project/{project_id}/add_credit_card/{user_id}", tags=["Project"])
async def add_credit_card(project_id: int, user_id: int, credit_card: dict) -> str:
    #SD Set Payment Detail
    project = system.get_project_in_project_list_from_id(project_id)
    user = system.get_user_from_id(user_id)
    credit_cards = user.get_all_credit_card()
    project.credit_card = credit_cards[credit_card["idx"]]
    return "yess"


@app.put("/set_description/{id}", tags=["Edit Project"])
async def set_project_desscription(id: int, new_description: str) -> str:
    #SD Set Description เค้ายุบไปรวมกับ Edit Project
    project = system.get_project_from_id(id)
    project.project_detail = new_description
    return f"The project with id {id} was edited!"
    
@app.put("/edit_project/{project_id}", tags=["Project"])
async def edit_project(project_id: int, new_project: dict) -> str:
    #SD Edit Project
    #editttttttttttttttttttttttttttttt
    print(new_project)
    project = system.get_project_in_project_list_from_id(project_id)
    project.project_name = new_project["name"]
    project.category = new_project["category"]
    project.project_image = new_project["image"]
    project.project_duration = new_project["project_duration"]
    project.project_detail = new_project["detail"]
    project.pledge_goal = new_project["pledge_goal"]
    return f"The project with id {project_id} was edited!"

@app.put("/edit_project/{project_id}/add_pledge_reward/{reward_id}", tags=["Pledge Reward"])
async def edit_reward(project_id: int, reward_id: int, new_reward: dict) -> str:
    #edittttttttttttttt
    project = system.get_project_in_project_list_from_id(project_id)
    reward = project.get_reward_from_id(reward_id)
    reward.reward_goal = int(new_reward["_PledgeReward__reward_goal"])
    reward.reward_name = new_reward["_PledgeReward__reward_name"]
    reward.reward_detail = new_reward["_PledgeReward__reward_detail"]
    reward.reward_include = new_reward["_PledgeReward__reward_include"]
    reward.reward_backers = int(new_reward["_PledgeReward__reward_backers"])
    reward.max_reward_backers = int(new_reward["_PledgeReward__reward_left"])
    reward.reward_shipping = RewardShipping(
                    new_reward["_RewardShipping__estimated_delivery"],
                    new_reward["_RewardShipping__ships_to"]
                    )
    return "yessssssss"
    
@app.post("/launch_project", tags=["Launch Project"])
async def launch_project(id: int) -> str:
    # SD: Launch Project
    project = system.get_project_from_id(id)
    system.launch_project(project)
    return f"The project with id{id} was launched"

#editttttttttttttttttttt
@app.delete("/edit_project/{project_id}/delete_reward/{reward_id}", tags=["Pledge Reward"])
async def edit_reward(project_id: int, reward_id: int) -> str:
    project = system.get_project_in_project_list_from_id(project_id)
    project.delete_reward(reward_id)
    return f"The pledge rewards with id {reward_id} of project with id {project_id} was delete"





