from address import Address
import json
import requests
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/address-detail", tags=['address'])
async def get_address() -> dict:
    return {"Data": addresses}

@app.post("/address-detail", tags=['address'])
async def add_address(address: dict) -> dict:

    addresses.append(address)
    return {
        "data": 'An address is Added!'
    }