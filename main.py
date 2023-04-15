from system import System
from user import User
from address import Address
from project import Project
from creditcardtransaction import CreditCardTransaction
import json
import requests
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

system = System()
pang = User("Janipang@gmail.com", "12345", "Pang", "pang.jpg", "Hello, my name is Pang.", "Bangkok, Thailand", "www.janipang.com")
system.add_user(pang)
pang_project = Project("Virtual Reality Game", "gaming", "image", "12-4-2023", "description1", pang,)
system.add_project(pang_project)
system.launch_project(pang_project)

user = system.get_user_by_id(1)
user.create_address("Thailand", "Home1", "Pang", "123 street", "Bangkok", "0987789876")
user.create_address("Thailand", "Home2", "Pang", "678 street", "Bangkok", "0987789876")

user.create_creditcard("Thailand", "123", "20230101", "12341234122413")
user.create_creditcard("USA", "143", "20230101", "12341234122413")

@app.get("/view_all_project", tags=["View Project"])
async def get_all_project() -> list:
    projects = system.launched_projects
    print("test")
    print(projects)
    return projects

@app.get("/get_creditcard", tags=['creditcard'])
async def get_creditcard(user_id: int) -> list:
    user = system.get_user_by_id(user_id)
    creditcard = user.get_all_creditcard()
    return creditcard

@app.post("/add_creditcard", tags=['creditcard'])
async def add_creditcard(user_id: int, creditcard: dict) -> str:
    user = system.get_user_by_id(user_id)
    user.create_creditcard(creditcard["country"], creditcard["cvc"], creditcard["expiration"], creditcard["card_number"])
    return "add creditcard success"

@app.delete("/delete_creditcard")
async def delete_creditcard(user_id: int, creditcard_id: int) -> str:
    user = system.get_user_by_id(user_id)
    user.delete_creditcard(creditcard_id)
    return "delete creditcard success"

@app.get("/get_shipping_address", tags=['address'])
async def get_address(user_id: int) -> list:
    user = system.get_user_by_id(user_id)
    addresses = user.get_all_address()
    return addresses

@app.post("/add_shipping_address", tags=['address'])
async def add_address(user_id: int, address: dict) -> str:
    user = system.get_user_by_id(user_id)
    user.create_address(address["country"], address["address_nickname"], address["full_name"], address["address"], address["city"], address["phone_number"])
    return "add address success"

@app.delete("/delete_address")
async def delete_address(user_id: int, address_id: int) -> str:
    user = system.get_user_by_id(user_id)
    user.delete_address(address_id)
    return "delete address success"

@app.delete("/delete_project")
async def delete_project(project_id: int) -> str:
    system.delete_project(project_id)
    return "delete project success!"