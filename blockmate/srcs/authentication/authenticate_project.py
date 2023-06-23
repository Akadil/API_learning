import requests
import os

"""
    Check if the token is right. Check if user exist
"""

my_token = os.environ["blockmate_token"]

url = "https://api.blockmate.io/v1/auth"

headers = {"accept": "application/json", "X-API-KEY": my_token}

response = requests.get(url, headers=headers)

print(response.text)
