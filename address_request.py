from address import Address
import json
import requests
from typing import Optional
from fastapi import FastAPI

addresses = [
    {
        "country": "Thailand",
        "address_nickname": "Home1",
        "full_name": "Pang Kumwan",
        "address": "123 Pang Village",
        "city": "Pang City",
        "phone_number": "0998887777",
    }
]

r = requests.post("http://127.0.0.1:8000/address-detail", data=json.dumps(addresses))
r = requests.post("http://127.0.0.1:8000/address-detail", data=json.dumps(addresses))
r = requests.post("http://127.0.0.1:8000/address-detail", data=json.dumps(addresses))
print(r)
print(r.json())