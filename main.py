from project import Project
from system import System
from user import User
from pledgereward import PledgeReward
from rewardshipping import RewardShipping
from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
    "Virtual Reality Game1",
    "gaming",
    "image",
    12,
    "description1",
    user_alice,
)
system.add_project(project_vr_game)
system.launch_project(project_vr_game)

project_vr_game2 = Project(
    "Virtual Reality Game2",
    "gaming",
    "image",
    13,
    "description2",
    user_alice,
)
system.add_project(project_vr_game2)
system.launch_project(project_vr_game2)

project_vr_game3 = Project(
    "Virtual Reality Game3",
    "gaming",
    "image",
    14,
    "description3",
    user_alice,
)
system.add_project(project_vr_game3)
system.launch_project(project_vr_game3)

project_vr_game4 = Project(
    "Virtual Reality Game4",
    "gaming",
    "image",
    15,
    "description4",
    user_alice,
)
system.add_project(project_vr_game4)
system.launch_project(project_vr_game4)

project_travel_blog = Project(
    "Around the World Travel Blog",
    "travel",
    "image",
    16,
    "description2",
    user_bob,
)
system.add_project(project_travel_blog)
system.launch_project(project_travel_blog)

# John create a project "clean air for all"
project_clean_air = Project(
    "clean air for all",
    "health",
    "image",
    17,
    "description3",
    user_john,
)
system.add_project(project_clean_air)
# John lauched the project
system.launch_project(project_clean_air)

project_clean_air.set_description("descriptionnnnnnnnnnnnnnnnnn")

project_clean_air.add_reward(PledgeReward(50, "Namprig Nangngam", "made with love by Nawat", [{"name": "Namprig", "quantity": 3}, {"name": "Serum", "quantity": 5}], 0, 10, RewardShipping({"month": 1, "year": 2024}, "", "", 20)))
project_clean_air.add_reward(PledgeReward(50, "Namprig Nangngam", "made with love by Nawat", [{"name": "Namprig", "quantity": 3}, {"name": "Serum", "quantity": 5}], 0, 10, RewardShipping({"month": 1, "year": 2024}, "", "", 20)))

project_clean_air.print_project()

user_ann = User(
    "Ann",
    "face_photo",
    "Tranformation leader",
    "New York",
    "jkn.com",
)

system.add_user(user_ann)

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

@app.get("/get_user", tags=["User"])
async def get_all_user() -> list:
    users = system.user_list
    return users

@app.get("/view_all_project", tags=["View Project"])
async def get_all_project() -> list:
    # SD: View All Project
    projects = system.launched_projects
    return projects

@app.get("/view_project_list", tags=["View Project"])
async def get_project_list() -> list:
    projects = system.project_list
    return projects


@app.get("/view_all_project/{id}", tags=["View Project"])
async def get_project(id: int):
    project = system.get_project_from_id(id)
    return project

@app.get("/view_my_project/{creator_id}", tags=["View Project"])
async def get_my_project(creator_id: int) -> list:
    #เดี๋ยวเอาไว้ทำ luanch project
    my_projects = system.get_my_projects(creator_id)
    return my_projects

@app.get("/pledge_reward/{project_id}", tags=["Pledge Reward"])
async def get_pledge_reward(project_id: int) -> list:
    project = system.get_project_from_id(project_id)
    rewards = project.pledge_rewards
    return rewards
    #reward_detail = project.get_pledge_reward_detail()
    #return reward_detail

@app.get("/project_id", tags=["Project"])
async def get_lastest_id() -> dict:
    return {"id": str(Project.id_counter - 1)}

@app.get("/view_all_project/{project_id}/get_reward_id", tags=["Pledge Reward"])
async def get_reward_id(project_id: int) -> dict:
    project = system.get_project_from_id(project_id)
    return {"id": str(len(project.pledge_rewards) + 1)}

@app.get("/get_last_project")
async def get_last_project():
    project = system.project_list
    return project[-1]

@app.post("/add_project", tags=["Add Project"])
async def add_the_project(project_dict: dict) -> int:
    #SD Start Project
    """
    {
    "project_name": "project101",
    "category": "art",
    "project_image": "image",
    "project_duration": "09-09-2029",
    "project_detail": "do not touch my hair!",
    "creator_id": 3
    }
    """
    project = Project(
                        project_dict["project_name"], 
                        project_dict["category"],
                        project_dict["project_image"],
                        project_dict["project_duration"],
                        project_dict["project_detail"],
                        system.get_user_from_id(project_dict["creator_id"])
                    )
    system.add_project(project)
    return project.id

@app.post("/edit_project/{project_id}/add_pledge_reward", tags=["Pledge Reward"])
async def add_pledge_reward(project_id: int, pledge_reward: dict) -> str:
    project = system.get_project_from_id(project_id)
    """
    {
        "reward_goal": 99,
        "reward_name": "REWARD_NAME",
        "reward_detail": "REWARD_DETAIL",
        "reward_include": [{"name": "NAME1", "quantity": 2}, {"name": "NAME2", "quantity": 3}],
        "reward_backers": 0,
        "max_reward_backers": 100,
        "estimated_delivery": {"month": 9, "year": 2029},
        "ships_to": "Universe",
        "address": "JKN",
        "shipping_cost": 9999 

        
        "reward_goal": 90,
        "reward_name": "Namplara",
        "reward_detail": "made with love by Engfa",
        "reward_include": [
        {
        "name": "A",
        "quantity": 3
        },
        {
        "name": "B",
        "quantity": 9
        }
        ],
        "reward_backers": 0,
        "max_reward_backers": 10,
        "estimated_delivery": {
        "month": 9,
        "year": 2029
        },
        "ships_to": "Universe",
        "address": "JKN",
        "shipping_cost": 20,
    }
    """
    
    reward_shipping = RewardShipping(
        pledge_reward["_RewardShipping__estimated_delivery"],
        pledge_reward["_RewardShipping__ships_to"], 
        pledge_reward["_RewardShipping__address"], 
        pledge_reward["_RewardShipping__shipping_cost"]
    )
    reward = PledgeReward(
        pledge_reward["_PledgeReward__reward_goal"],
        pledge_reward["_PledgeReward__reward_name"], 
        pledge_reward["_PledgeReward__reward_detail"], 
        pledge_reward["_PledgeReward__reward_include"], 
        pledge_reward["_PledgeReward__reward_backers"], 
        pledge_reward["_PledgeReward__max_reward_backers"], 
        reward_shipping, 
        int(pledge_reward["reward_id"])
        )
    project.add_reward(reward)

    return f"Add reward to project id {project_id}"

@app.post("/edit_project/{project_id}/add_payment_detail", tags=["Payment Detail"])
async def add_payment_detail(project_id: int, detail: dict) -> str:
    #SD Set Payment Detail
    project = system.get_project_from_id(project_id)
    """
    {
        "legal_first_name": "Anne",
        "legal_last_name": "Jukrajuthatip",
        "email_address": "Anne@mou.ac.th",
        "date_of_birth": {"date": 1, "month": 1, "year": 2000},
        "home_address": "999/99",
        "city": "Newyork",
        "state": "USA",
        "postal_code": "65140",
        "phone_number": "0999999999",
        "account_number": "123456789",
        "bank": "muo bank"
    }
    """
    project.set_payment_detail(
        detail["legal_first_name"],
        detail["legal_last_name"],
        detail["email_address"],
        detail["date_of_birth"],
        detail["home_address"],
        detail["city"],
        detail["state"],
        detail["postal_code"],
        detail["phone_number"],
        detail["account_number"],
        detail["bank"]
        )
    return "yess"


@app.put("/set_description/{id}", tags=["Edit Project"])
async def set_project_desscription(id: int, new_description: str) -> str:
    #SD Set Description เค้ายุบไปรวมกับ Edit Project
    project = system.get_project_from_id(id)
    if id >= Project.id_counter:
        return f"The project with id {id} is not found."
    else:
        project.set_description(new_description)
        return f"The project with id {id} was edited!"
    
@app.put("/edit_project/{project_id}", tags=["Project"])
async def edit_project(project_id: int, new_project: dict) -> str:
    #SD Edit Project
    print(new_project)
    project = system.get_project_from_id(project_id)
    project.project_name = new_project["_Project__project_name"]
    project.category = new_project["_Project__category"]
    project.project_image = new_project["_Project__project_image"]
    project.project_duration = new_project["_Project__project_duration"]
    project.project_detail = new_project["_Project__project_detail"]
    project.pledge_goal = new_project["_Project__pledge_goal"]
    return f"The project with id {project_id} was edited!"

@app.put("/edit_project/{project_id}/add_pledge_reward/{reward_id}", tags=["Pledge Reward"])
async def edit_reward(project_id: int, reward_id: int, new_reward: dict) -> str:
    project = system.get_project_from_id(project_id)
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
                    new_reward["_RewardShipping__address"],
                    int(new_reward["_RewardShipping__shipping_cost"])
                )
    return "yessssssss"
    
@app.post("/launch_project", tags=["Launch Project"])
async def launch_project(id: int) -> str:
    # SD: Launch Project
    project = system.get_project_from_id(id)
    system.launch_project(project)
    return f"The project with id{id} was launched"

@app.delete("/edit_project/{project_id}/delete_reward/{reward_id}", tags=["Pledge Reward"])
async def edit_reward(project_id: int, reward_id: int) -> str:
    project = system.get_project_from_id(project_id)
    project.delete_reward(reward_id)
    return f"The pledge rewards with id {reward_id} of project with id {project_id} was delete"




