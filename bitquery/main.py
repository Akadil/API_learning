import requests

url = "https://graphql.bitquery.io"
query = """
query {
  bitcoin {
    transactions(
      limit: 10,
      offset: 0,
      sender: { is: "YOUR_WALLET_ADDRESS" }
    ) {
      transaction {
        hash
        timestamp {
          isoDate
        }
        value
        fee
      }
    }
  }
}
"""

headers = {
    "Content-Type": "application/json",
    "X-API-Key": "YOUR_API_KEY"
}

response = requests.post(url, json={"query": query}, headers=headers)

if response.status_code == 200:
    data = response.json()
    # Process the transaction data as needed
    transactions = data["data"]["bitcoin"]["transactions"]
    for tx in transactions:
        tx_hash = tx["transaction"]["hash"]
        timestamp = tx["transaction"]["timestamp"]["isoDate"]
        value = tx["transaction"]["value"]
        fee = tx["transaction"]["fee"]
        print(f"Transaction Hash: {tx_hash}")
        print(f"Timestamp: {timestamp}")
        print(f"Value: {value}")
        print(f"Fee: {fee}")
        print("-----------------------------")
else:
    print("Error:", response.status_code)
