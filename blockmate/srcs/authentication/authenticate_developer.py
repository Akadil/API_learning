import requests
import os

"""
    Check if the token is right. Check if user exist
"""

my_token = os.environ["blockmate_token"]

url = "https://api.blockmate.io/v1/auth/developer"

headers = {
    "accept": "application/json",
    "X-API-KEY": my_token
}

response = requests.get(url, headers=headers)

print(response.text)

# eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODcxODQxNzQsImlhdCI6MTY4NzE4MzI3NCwibmJmIjoxNjg3MTgzMjc0LCJwcm9qZWN0X2lkIjo2ODAyLCJ0eXBlIjoidXNlciIsInVzZXJfdXVpZCI6ImJjNGM0YjlmLWEzZWEtNGUzOS1iOTc1LWNiMWE2OWNhZTcwYyJ9.zdgusiJVNSfwA9-gvPVxlu1zIUusQQc8Uc9YzPVbL9wPx2v9fnsYVzCcJEsvgwDikg52n4cOXKPp2nqnU5RQAQ