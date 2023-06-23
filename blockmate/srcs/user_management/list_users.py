import requests
import os

# User inputs
my_token = os.environ["blockmate_token"]

# Send a request
url = "https://api.blockmate.io/v1/users"
headers = {
    "accept": "application/json",
    "X-API-KEY": my_token
}
response = requests.get(url, headers=headers)

# Response
data = response.json()[0]
for elem in data:
    print(elem, data[elem])