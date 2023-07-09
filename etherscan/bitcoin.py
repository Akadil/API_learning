import requests

# Bitcoin Address
address = "bc1qmtdfrpggskfkqnmxy5f5exuw3z8kdmlje70vvz"

# Blockchain.com API URL
url = f"https://blockchain.info/rawaddr/{address}"

# Send GET request to retrieve address data
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    transactions = data["txs"]
    
    for tx in transactions:
        # tx_hash = tx["hash"]
        # value = tx["result"]
        # confirmations = tx["confirmations"]
        
        # print("Transaction Hash:", tx_hash)
        # print("Value:", value)
        # print("Confirmations:", confirmations)
        print (tx)
        print("-------------------------")
else:
    print("Error:", response.status_code)
