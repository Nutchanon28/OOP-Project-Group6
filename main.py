from system import System
from user import User
from address import Address
from project import Project
from credit_card_transaction import CreditCardTransaction
import json
import requests
from typing import Optional
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

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


system = System()

@app.get("/view_all_project", tags=["View Project"])
async def get_all_project() -> list:
    projects = system.launched_projects
    return projects

@app.get("/get_user", tags=['user'])
async def get_user(user_id: int):
    user = system.get_user_from_id(user_id)
    return user

@app.put("/add_profile", tags=['profile'])
async def add_profile(user_id: int, user: dict) -> str:
    print(user)
    the_user = system.get_user_from_id(user_id)
    the_user.edit_profile(user["name"], user["avatar"], user["biography"], user["location"], user["website"])
    return "edit profile success"

@app.put("/add_account", tags=['account'])
async def add_account(user_id: int, user: dict) -> str:
    print(user)
    the_user = system.get_user_from_id(user_id)
    the_user.edit_account(user["gmail"], user["password"])
    return "edit account success"

@app.get("/get_payment_method", tags=['creditcard'])
async def get_creditcard(user_id: int) -> list:
    user = system.get_user_from_id(user_id)
    creditcard = user.payment_methods
    return creditcard

@app.post("/add_payment_method", tags=['creditcard'])
async def add_creditcard(user_id: int, creditcard: dict) -> str:
    user = system.get_user_from_id(user_id)
    user.add_payment_method(creditcard["country"], creditcard["cvc"], creditcard["expiration"], creditcard["card_number"])
    return "add payment method success"

@app.delete("/delete_payment_method")
async def delete_creditcard(user_id: int, creditcard_id: int) -> str:
    user = system.get_user_from_id(user_id)
    user.delete_payment_method(creditcard_id)
    return "delete payment method success"

@app.get("/get_shipping_address", tags=['address'])
async def get_address(user_id: int) -> list:
    user = system.get_user_from_id(user_id)
    addresses = user.addresses
    return addresses

@app.post("/add_shipping_address", tags=['address'])
async def add_address(user_id: int, address: dict) -> str:
    user = system.get_user_from_id(user_id)
    user.create_address(address["country"], address["address_nickname"], address["full_name"], address["address"], address["city"], address["phone_number"])
    return "add address success"

@app.delete("/delete_address")
async def delete_address(user_id: int, address_id: int) -> str:
    user = system.get_user_from_id(user_id)
    user.delete_address(address_id)
    return "delete address success"

@app.delete("/delete_project")
async def delete_project(project_id: int) -> str:
    system.delete_project(project_id)
    return "delete project success!"