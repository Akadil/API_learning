import requests
import os

# The inputs:
my_token = os.environ["my_token"]
name = None

# Request
url = "https://api.blockmate.io/v1/users"
payload = {"name": name}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "X-API-KEY": my_token
}
response = requests.post(url, json=payload, headers=headers)

# Response
for elem in response.text:
    print(elem)