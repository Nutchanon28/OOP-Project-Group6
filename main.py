from fastapi import FastAPI
from typing import Union
from fastapi.middleware.cors import CORSMiddleware

from project import Project
from pledge_reward import PledgeReward
from reward_shipping import RewardShipping
from system import System
from user import User
from credit_card_transaction import CreditCardTransaction
from update import Update
from notification import Notification

import json
from datetime import datetime

system = System()
user_jame = User(
    "Jame@gmail.com",
    "1234",
    "Jame",
    "https://1734811051.rsc.cdn77.org/data/images/full/393261/discord-avatars-now-usable-for-premium-nitro-tier-subscribers-plus-scheduled-events-feature.jpg",
    "Thailand",
    "Just a simple guy",
    "jame_project.com",
)
system.add_user(user_jame)
user_john = User(
    "John@gmail.com",
    "2345",
    "John",
    "https://cdn.nerdschalk.com/wp-content/uploads/2023/02/why-is-discord-avatar-blurry.png",
    "Founder of clean air for all",
    "Thailand",
    "clean_air.com",
)
system.add_user(user_john)

user_alice = User(
    "Alice@gmail.com",
    "3456",
    "Alice",
    "https://pbs.twimg.com/tweet_video_thumb/DBBAK32XkAA-VCz.jpg",
    "Lover of all things tech",
    "Thailand",
    "alice.tech",
)
system.add_user(user_alice)

user_bob = User(
    "Bob@gmail.com",
    "4567",
    "Bob",
    "https://cdn.siasat.com/wp-content/uploads/2021/05/Discord.jpg",
    "Adventurer and storyteller",
    "Thailand",
    "bobadventures.com",
)
system.add_user(user_bob)

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
    "https://i.ibb.co/rbmNB2R/virtual-reality-game.jpg",
    "12-4-2023",
    user_alice,
    10000,
)
project_vr_game.project_detail = "abcdef"

system.add_project(project_vr_game)

thailand = RewardShipping("20-4-2023", ["Bankok", "A", "B", "C"])
project_vr_game.add_reward(
    50,
    "Early Access",
    "Be one of the first to play our game!",
    200,
    "20-4-2023",
    ["Bankok", "A", "B", "C"],
)
project_vr_game.add_reward(
    100,
    "Custom Character",
    "Create your own character to use in the game!",
    100,
    "20-4-2023",
    ["Bankok", "A", "B", "C"],
)

project_vr_game.add_faq(
    "Will this game have multiplayer?:Yes, we always intend to make our game playable by many people, and this game is no different."
)

project_vr_game.add_faq(
    "Wil you release the game soundtracks?:That depends on John William."
)

project_vr_game.add_faq("Do you like Calculas?:no")

system.launch_project(project_vr_game)

project_travel_blog = Project(
    "Around the World Travel Blog",
    "Publishing",
    "https://www.connollycove.com/wp-content/uploads/2022/01/vibrant-flowers-and-bicycle-bike-on-a-bridge-of-amsterdam-at-early-evening-twilight-on-SBI-336667208-1024x683.jpg",
    "15-5-2023",
    user_bob,
    5000,
)
project_travel_blog.project_detail = "Follow our journey around the world as we share stories, photos, and tips for traveling on a budget!"
project_travel_blog.add_reward(
    25,
    "Travel Tips Ebook",
    "Learn our secrets for budget travel!",
    500,
    "20-4-2023",
    ["Bankok", "A", "B", "C"],
)
project_travel_blog.add_reward(
    50,
    "Personalized Postcard",
    "Get a postcard from us during our travels!",
    100,
    "20-4-2023",
    ["Bankok", "A", "B", "C"],
)
system.launch_project(project_travel_blog)

# John create a project "clean air for all"
project_clean_air = Project(
    "clean air for all",
    "Design & Tech",
    "https://i.ibb.co/Tct0n02/clean-air.jpg",
    "11-4-2023",
    user_john,
    3300,
)
project_clean_air.project_detail = "A project by a guy who is passionate about the environment. Let's save lives by improving the air we breath."
# Green Energy for All
project_green_energy = Project(
    "Green Energy for All",
    "Design & Tech",
    "https://i.ibb.co/hKDhXff/green-energy.jpg",
    "5/1/2023 - 12/31/2023",
    user_john,
    7500,
)
project_green_energy.project_detail = "Join us in our mission to create sustainable energy solutions for everyone. Our team of experts is developing innovative technologies that will revolutionize the way we generate and consume energy."

system.launch_project(project_green_energy)

# Artificial Intelligence for Business
project_ai_business = Project(
    "Artificial Intelligence for Business",
    "Design & Tech",
    "https://www.airswift.com/hubfs/3d-rendering-robot-learning-machine-education.png",
    "6/1/2023 - 11/30/2023",
    user_alice,
    3200,
)

system.add_project(project_ai_business)
project_ai_business = "Artificial intelligence is changing the game for businesses of all sizes. Our team of experienced developers and consultants is creating cutting-edge AI solutions that will help companies streamline operations, increase efficiency, and unlock new revenue streams."

system.launch_project(project_ai_business)

# Music Festival in the Park
project_music_festival = Project(
    "Music Festival in the Park",
    "Music",
    "https://i.ibb.co/WxMsFm5/music-festival.jpg",
    "7/15/2023 - 7/17/2023",
    user_bob,
    8800,
)
project_music_festival.project_detail = "Join us for a weekend of live music, food, and fun in the park! Our lineup features local and national acts across a variety of genres, and all proceeds will go towards supporting the park's maintenance and community programs."

system.launch_project(project_music_festival)

# Open Source Educational Software
project_oss_edu = Project(
    "Open Source Educational Software",
    "Design & Tech",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSN_7_vPx7I-_8uiLyxwPeGj0Jg_di0W2YBwQ&usqp=CAU",
    "8/1/2023 - 12/31/2023",
    user_jame,
    6540,
)
project_oss_edu.project_detail = "We believe that education should be accessible to everyone. That's why we're developing a suite of open source educational software that anyone can use, modify, and share. Join us in our mission to democratize learning!"

system.launch_project(project_oss_edu)

# Sustainable Clothing Line
project_sustainable_clothing = Project(
    "Sustainable Clothing Line",
    "Arts",
    "https://assets.bizclikmedia.net/668/677498f55ceb679934c22fa1555909a2:517f423e3e5afa70cf909078016b6ec8/packaging-900x-jpeg.webp",
    "9/1/2023 - 2/28/2024",
    user_alice,
    3500,
)
project_sustainable_clothing.project_detail = "Fast fashion is taking a toll on our planet. That's why we're launching a sustainable clothing line made from eco-friendly materials and manufactured using ethical practices. Help us make fashion more sustainable!"

system.launch_project(project_sustainable_clothing)

# Community Garden
project_community_garden = Project(
    "Community Garden",
    "Food & Craft",
    "https://i.swncdn.com/media/1600w/via/9367-flickr-faunggs-photos.webp",
    "10/1/2023 - 12/31/2023",
    user_bob,
    7700,
)
project_community_garden.project_detail = "We're transforming an empty lot in the heart of the city into a vibrant community garden. Our vision is to create a space where anyone can come to grow, learn, and connect with their neighbors. Join us in creating a more sustainable and connected community!"

system.launch_project(project_community_garden)

# Mental Health Chatbot
project_mental_health_chatbot = Project(
    "Mental Health Chatbot",
    "Design & Tech",
    "https://i0.wp.com/images-prod.healthline.com/hlcmsresource/images/July-18/8054-Mental_Health_Chat_Bots-1296X728-Header.jpg?w=1155&h=1528",
    "11/1/2023 - 4/30/2024",
    user_bob,
    1234,
)
project_mental_health_chatbot.project_detail = "Mental health is just as important as physical health, but many people still struggle to access the care they need. That's why we're creating a chatbot that provides personalized mental health support and resources to anyone who needs it. Help us break down barriers to care!"

system.launch_project(project_mental_health_chatbot)

# John added a reward
project_clean_air.add_reward(
    150, "Oxygen Tank", "It's large", 100, "20-4-2023", ["Bankok", "A", "B", "C"]
)

# John lauched the project
system.launch_project(project_clean_air)

# country, cvc, expiration, card number
user_jame.add_payment_method("Thailand", "000", "06/25", "420694206928")
user_jame.add_payment_method("Thailand", "001", "06/25", "320694206928")
user_jame.add_payment_method("Thailand", "002", "06/25", "220694206928")

user_jame.back_project(
    project_clean_air,
    user_jame.payment_methods[0],
    project_clean_air.pledge_rewards[0],
    1000,
)
user_jame.back_project(
    project_green_energy,
    user_jame.payment_methods[1],
    project_clean_air.pledge_rewards[0],
    1000,
)
user_jame.back_project(
    project_music_festival,
    user_jame.payment_methods[2],
    project_clean_air.pledge_rewards[0],
    1000,
)

app = FastAPI()

origins = ["http://localhost:3000", "localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/view_user", tags=["View User"])
async def get_user(userId: Union[int, None] = 1) -> dict:
    user = system.get_user_from_id(userId)
    user_detail = {
        "gmail": user.gmail,
        "password": user.password,
        "name": user.name,
        "avatar": user.avatar,
        "biography": user.biography,
        "website": user.website,
    }
    return user_detail


@app.get("/view_all_project", tags=["View Project"])
async def get_all_project() -> dict:
    # SD: View All Project
    projects = system.launched_projects
    # projects_detail = [project.get_project_detail() for project in projects]
    projects_detail = []

    projects_funded = sum([1 for project in projects if project.pledge_received > 0])
    total_money = sum([project.pledge_received for project in projects])
    number_of_pledges = sum([project.number_of_backings() for project in projects])

    for project in projects:
        projects_detail.append(
            {
                "id": project.id,
                "name": project.project_name,
                "image": project.project_image,
                "detail": project.project_detail,
                "category": project.category,
                "percent": int((project.pledge_received / project.pledge_goal) * 100),
                "creator": project.project_creator.name,
            }
        )
    return {
        "projects_detail": projects_detail,
        "projects_funded": projects_funded,
        "total_money": total_money,
        "number_of_pledges": number_of_pledges,
    }


@app.get("/view_project_list", tags=["View Project"])
async def get_project_list() -> list:
    projects = system.project_list
    return projects


@app.get("/get_project_credit_card/{project_id}", tags=["Project"])
async def get_project_credit_card(project_id: int):
    project = system.get_project_in_project_list_from_id(project_id)
    return project.credit_card


@app.get("/view_backed_project", tags=["Backed Project"])
async def get_backed_project(user_id: int) -> list:
    # SD: View Backed Project??
    current_user = system.get_user_from_id(user_id)
    projects_id = current_user.get_backed_project_id()
    projects = []
    for project_id in projects_id:
        project = system.get_project_from_id(project_id)
        projects.append(project)
    projects_detail = []
    for project in projects:
        projects_detail.append(
            {
                "id": project.id,
                "name": project.project_name,
                "image": project.project_image,
                "detail": project.project_detail,
                "category": project.category,
                "creator": project.project_creator.name,
            }
        )
    return projects_detail


@app.get("/view_notifications/{user_id}", tags=["Notifications"])
async def get_user_notifications(user_id: int) -> list:
    # SD: View Backed Project??
    current_user = system.get_user_from_id(user_id)
    notifications = current_user.notifications

    return notifications


@app.get("/view_project/{project_id}", tags=["View Project"])
async def get_project(project_id: int) -> dict:
    # SD: View Project
    # User select a project
    selected_project = system.get_project_in_project_list_from_id(project_id)
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
async def send_comment(project_id: int, input: dict) -> dict:
    # SD: Send Comment
    user_id = input["user_id"]
    text = input["text"]
    current_user = system.get_user_from_id(user_id)
    selected_project = system.get_project_from_id(project_id)
    selected_project.create_comment(datetime.now(), text, current_user)
    return {"response": "successful"}


@app.post("/show_payment_requirements", tags=["Back the Project"])
async def show_payment_requirements(input: dict) -> dict:
    # SD: Back the Project
    user_id = int(input["user_id"])
    project_id = int(input["project_id"])
    current_user = system.get_user_from_id(user_id)
    selected_project = system.get_project_from_id(project_id)
    project_detail = selected_project.get_project_detail()

    # This returns an entire CreditCardTransaction class, not sure if it will work
    payment_methods = current_user.payment_methods
    return {"project_detail": project_detail, "payment_methods": payment_methods}


@app.post("/back_the_project", tags=["Back the Project"])
async def back_the_project(input: dict) -> dict:
    # SD: Back the Project
    user_id = input["user_id"]
    project_id = input["project_id"]
    credit_card_id = input["credit_card_id"]
    reward_id = input["reward_id"]
    bonus_cost = input["bonus_cost"]

    current_user = system.get_user_from_id(user_id)
    selected_project = system.get_project_from_id(project_id)
    credit_card = current_user.get_credit_card_from_id(credit_card_id)
    reward = selected_project.get_reward_from_id(reward_id)
    response = current_user.back_project(
        selected_project, credit_card, reward, bonus_cost
    )

    reward_goal = 0
    if reward != "reward not found":
        reward_goal = reward.reward_goal

    backer_message = f"You have pledge {reward_goal + bonus_cost} Baht for {selected_project.project_name}"
    creator_message = f"You have received {reward_goal + bonus_cost} Baht for {selected_project.project_name} from {current_user.name}"

    if reward != "reward not found":
        backer_message += f", for the reward of {reward.reward_name}"
        creator_message += f", who are waiting for {reward.reward_name}"

    backer_notification = Notification("Backing", backer_message)
    creator_notification = Notification("Receiving", creator_message)

    current_user.add_new_notification(backer_notification)
    selected_project.project_creator.add_new_notification(creator_notification)
    return {"response": response}


@app.get("/pledge_reward/{project_id}", tags=["Pledge Reward"])
async def get_pledge_reward(project_id: int) -> list:
    project = system.get_project_in_project_list_from_id(project_id)
    rewards = project.pledge_rewards
    return rewards
    # reward_detail = project.get_pledge_reward_detail()
    # return reward_detail


@app.get("/view_all_project/{project_id}/get_reward_id", tags=["Pledge Reward"])
async def get_reward_id(project_id: int) -> dict:
    project = system.get_project_in_project_list_from_id(project_id)
    return {"id": str(len(project.pledge_rewards) + 1)}


@app.get("/get_last_project")
async def get_last_project():
    project = system.project_list
    return {"id": project[-1].id, "detail": project[-1].get_project_detail()}


@app.get("/get_last_reward_id/{project_id}", tags=["Pledge reward"])
async def get_last_reward_id(project_id: int) -> dict:
    project = system.get_project_in_project_list_from_id(project_id)
    last_reward_id = project.get_last_reward().id
    return {"id": last_reward_id}


@app.get("/get_my_project/{user_id}", tags=["Project"])
async def get_my_project(user_id: int) -> list:
    my_projects = system.get_my_projects(user_id)
    return my_projects


@app.post("/add_project", tags=["Add Project"])
async def add_the_project(project_dict: dict) -> str:
    # SD Start Project
    project = Project(
        project_dict["project_name"],
        project_dict["category"],
        project_dict["project_image"],
        project_dict["project_duration"],
        system.get_user_from_id(project_dict["creator_id"]),
        project_dict["pledge_goal"],
    )
    system.add_project(project)
    return "Success"


@app.post("/edit_project/{project_id}/add_pledge_reward", tags=["Pledge Reward"])
async def add_pledge_reward(project_id: int, pledge_reward: dict) -> str:
    project = system.get_project_in_project_list_from_id(project_id)
    project.add_reward(
        pledge_reward["_PledgeReward__reward_goal"],
        pledge_reward["_PledgeReward__reward_name"],
        pledge_reward["_PledgeReward__reward_detail"],
        pledge_reward["_PledgeReward__reward_left"],
        pledge_reward["_RewardShipping__estimated_delivery"],
        pledge_reward["_RewardShipping__ships_to"],
    )

    return f"Add reward to project id {project_id}"


@app.put("/edit_project/{project_id}/add_credit_card/{user_id}", tags=["Project"])
async def add_credit_card(project_id: int, user_id: int, credit_card: dict) -> str:
    # SD Set Payment Detail
    project = system.get_project_in_project_list_from_id(project_id)
    user = system.get_user_from_id(user_id)
    credit_cards = user.payment_methods
    project.credit_card = credit_cards[credit_card["idx"]]
    return "yess"


@app.put("/set_description/{id}", tags=["Edit Project"])
async def set_project_desscription(id: int, new_description: str) -> str:
    # SD Set Description เค้ายุบไปรวมกับ Edit Project
    project = system.get_project_in_project_list_from_id(id)
    project.project_detail = new_description
    return f"The project with id {id} was edited!"


@app.put("/edit_project/{project_id}", tags=["Project"])
async def edit_project(project_id: int, new_project: dict) -> str:
    # SD Edit Project
    print(new_project)
    project = system.get_project_in_project_list_from_id(project_id)
    project.project_name = new_project["_Project__project_name"]
    project.category = new_project["_Project__category"]
    project.project_image = new_project["_Project__project_image"]
    project.project_duration = new_project["_Project__project_duration"]
    project.project_detail = new_project["_Project__project_detail"]
    project.pledge_goal = new_project["_Project__pledge_goal"]
    return f"The project with id {project_id} was edited!"


@app.put(
    "/edit_project/{project_id}/add_pledge_reward/{reward_id}", tags=["Pledge Reward"]
)
async def edit_reward(project_id: int, reward_id: int, new_reward: dict) -> str:
    project = system.get_project_in_project_list_from_id(project_id)
    reward = project.get_reward_from_id(reward_id)
    reward.reward_goal = int(new_reward["_PledgeReward__reward_goal"])
    reward.reward_name = new_reward["_PledgeReward__reward_name"]
    reward.reward_detail = new_reward["_PledgeReward__reward_detail"]
    reward.reward_include = new_reward["_PledgeReward__reward_include"]
    reward.reward_backers = int(new_reward["_PledgeReward__reward_backers"])
    reward.max_reward_backers = int(new_reward["_PledgeReward__max_reward_backers"])
    reward.reward_shipping = RewardShipping(
        new_reward["_RewardShipping__estimated_delivery"],
        new_reward["_RewardShipping__ships_to"],
    )
    return "yessssssss"


@app.post("/launch_project", tags=["Launch Project"])
async def launch_project(id: int) -> str:
    # SD: Launch Project
    project = system.get_project_in_project_list_from_id(id)
    system.launch_project(project)
    return f"The project with id{id} was launched"


@app.delete(
    "/edit_project/{project_id}/delete_reward/{reward_id}", tags=["Pledge Reward"]
)
async def edit_reward(project_id: int, reward_id: int) -> str:
    project = system.get_project_in_project_list_from_id(project_id)
    project.delete_reward(reward_id)
    return f"The pledge rewards with id {reward_id} of project with id {project_id} was delete"


@app.post("/add_update", tags=["Add Update"])
async def add_update(input: dict) -> dict:
    project_id = input["project_id"]
    user_id = input["user_id"]
    update_title = input["update_title"]
    update_detail = input["update_detail"]
    update_image = input["update_image"]
    # SD: Add Update
    current_user = system.get_user_from_id(user_id)
    selected_project = system.get_project_from_id(project_id)
    new_update = Update(update_title, current_user, update_detail, update_image)
    selected_project.add_update(new_update)

    unique_backer_ids = { 0 }
    notification = Notification("Update", f"New update on {selected_project.project_name}!")
    for backing in selected_project.backings:
        unique_backer_ids.add(backing.backer_id)

    for id in unique_backer_ids:
        backer = system.get_user_from_id(id)
        if backer == "user not found":
            continue
        backer.add_new_notification(notification)

    response = selected_project.get_project_detail()["updates"]
    return {"response": response}


@app.get("/get_user", tags=["user"])
async def get_user(user_id: int):
    user = system.get_user_from_id(user_id)
    return user


@app.put("/add_profile", tags=["profile"])
async def add_profile(user_id: int, user: dict) -> str:
    the_user = system.get_user_from_id(user_id)
    the_user.edit_profile(
        user["name"],
        user["avatar"],
        user["biography"],
        user["location"],
        user["website"],
    )
    return "edit profile success"


@app.put("/add_account", tags=["account"])
async def add_account(user_id: int, user: dict) -> str:
    the_user = system.get_user_from_id(user_id)
    the_user.edit_account(user["gmail"], user["old_password"], user["new_password"])
    return "edit account success"


@app.get("/get_payment_method", tags=["creditcard"])
async def get_creditcard(user_id: int) -> list:
    user = system.get_user_from_id(user_id)
    creditcard = user.payment_methods
    return creditcard


@app.post("/add_payment_method", tags=["creditcard"])
async def add_creditcard(user_id: int, creditcard: dict) -> str:
    user = system.get_user_from_id(user_id)
    user.add_payment_method(
        creditcard["country"],
        creditcard["cvc"],
        creditcard["expiration"],
        creditcard["card_number"],
    )
    return "add payment method success"


@app.delete("/delete_payment_method")
async def delete_creditcard(user_id: int, creditcard_id: int) -> str:
    user = system.get_user_from_id(user_id)
    user.delete_payment_method(creditcard_id)
    return "delete payment method success"


@app.get("/get_shipping_address", tags=["address"])
async def get_address(user_id: int) -> list:
    user = system.get_user_from_id(user_id)
    addresses = user.addresses
    return addresses


@app.post("/add_shipping_address", tags=["address"])
async def add_address(user_id: int, address: dict) -> str:
    user = system.get_user_from_id(user_id)
    user.create_address(
        address["country"],
        address["address_nickname"],
        address["full_name"],
        address["address"],
        address["city"],
        address["phone_number"],
    )
    return "add address success"


@app.delete("/delete_address")
async def delete_address(user_id: int, address_id: int) -> str:
    user = system.get_user_from_id(user_id)
    user.delete_address(address_id)
    return "delete address success"


@app.post("/add_faq", tags=["FAQ"])
async def add_faq(input: dict) -> dict:
    project_id = input["project_id"]
    question = input["question"]
    answer = input["answer"]

    selected_project = system.get_project_from_id(project_id)
    new_faq = str(question) + ":" + str(answer)
    selected_project.add_faq(new_faq)

    unique_backer_ids = { 0 }
    notification = Notification("Update", f"New faq on {selected_project.project_name}!")
    for backing in selected_project.backings:
        unique_backer_ids.add(backing.backer_id)

    for id in unique_backer_ids:
        backer = system.get_user_from_id(id)
        if backer == "user not found":
            continue
        backer.add_new_notification(notification)

    response = selected_project.get_project_detail()["faqs"]
    return {"response": response}
