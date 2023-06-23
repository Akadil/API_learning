import requests
import json
import time
import sys
import os

# Fill in your token
my_project_token=os.environ["blockmate_token"]

# Create a user
r = requests.post("https://api.blockmate.io/v1/users", json={"name": "test-user"}, headers={"X-API-KEY": my_project_token})
user_uuid = r.json()["uuid"]
print(f"We got user with id: {user_uuid}")

# Authenticate the user
r = requests.get(f"https://api.blockmate.io/v1/users/{user_uuid}/auth", headers={"X-API-KEY": my_project_token})
user_jwt_token = r.json()["token"]
print(f"We got JWT token for the user")

# Connect a binance (account) to user
r = requests.post("https://api.blockmate.io/v1/exchange/binance/connect", json={"description": "My test btc address", "api_key": "JZUkR95EMN8o8IELANDPNGAxXRCnrBfUi36echtEl8nTDSkWREP6usGrNoEHdmRX", "api_secret":"z5VjEJonX5J7WKehxAdUQNPM2VPzaIy9moz4I7WH2WcxwPDsjKvx9NBPYDeoJQt8"}, headers={"Authorization": f"Bearer {user_jwt_token}"})
print(r.json())
account_id = r.json()["id"]
print(f"We connected an account to user with id: {account_id}")
