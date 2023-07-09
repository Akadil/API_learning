import requests

wallet_address = "0x5f399f953875b24610e97a89fbee61117433cc90"
blockchain = "binance-smart-chain" 
network = "mainnet"


url = "https://rest.cryptoapis.io"
endpoint = f"/blockchain-data/{blockchain}/{network}/addresses/{wallet_address}/transactions"

query_params = {
    "context":"yourExampleString"
}

headers = {
    "Content-Type": "application/json",
    "X-API-Key": "68720905b83ee6123f090243981d67f2c753f013"
}

response = requests.get(url + endpoint, headers=headers)
if response.status_code == 200:
    # Successful response
    data = response.json()
    # Process the data as needed
    print(data)
else:
    # Handle the error case
    print("Error:", response.status_code)




# import http.client

# conn = http.client.HTTPConnection("https://rest.cryptoapis.io")
# print("I was here")
# querystring = {"limit": 50, "offset": 0}
# headers = {
#   'Content-Type': "application/json",
#   'X-API-Key': "68720905b83ee6123f090243981d67f2c753f013"
# }

# conn.request("GET", "blockchain-data,bitcoin,testnet,addresses,mho4jHBcrNCncKt38trJahXakuaBnS7LK5,transactions", headers=headers, params=querystring )

# res = conn.getresponse()