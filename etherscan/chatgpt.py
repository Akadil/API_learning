import requests

def retrieve_transactions(address, api_key):
    # Specify the Etherscan API endpoint for retrieving transactions
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&apikey={api_key}"
    url2 = "https://api.etherscan.io/api"

    # Prepare the query parameters

    try:
        # Send a GET request to the Etherscan API
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Extract the transactions from the response
            transactions = response.json()["result"]
            
            # Process the transactions
            for tx in transactions:

                # Print the transaction details
                print(f"Transaction Hash: {tx['hash']}")
                print(f"Timestamp: {tx['timeStamp']}")
                print(f"Value: {tx['value']}")
                print(f"From address: {tx['from']}")
                print(f"To address: {tx['to']}")
                print(f'Method ID: {tx["methodId"]}')
                if (tx["methodId"] == "0x"):
                    print(f'Method Name: transfer')
                elif (tx["methodId"] == "0xb6b55f25"):
                    print(f'Method Name: deposit')
                elif (tx["methodId"] == "0x095ea7b3"):
                    print(f'Method Name: approve')
                elif (tx["methodId"] == "0xa9059cbb"):
                    print(f'Method Name: transfer')
                elif (tx["methodId"] == "0x5ae401dc"):
                    print(f'Method Name: multicell')
                elif (tx["methodId"] == "0x745400c9"):
                    print(f'Method Name: Request Withdraw')
                elif (tx["methodId"] == "0xf3fef3a3"):
                    print(f'Method Name: Withdraw')
                else:
                    print(f'Method Name: Unknown')

                print("----------------------")
            for elem in transactions[0]:
                print(f"{elem}, {transactions[0][elem]}")
        else:
            print(f"Error: {response.status_code} - {response.text}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Enter your Ethereum wallet address and Etherscan API key here
wallet_address = "0x8Fa3e40068aB20B74b94b83288E53cCdeDe79AE4"
api_key = "A17TNTXIJF2ZIM9U11SGFUUWA3X3IAWDV8"

# Call the function to retrieve transactions
retrieve_transactions(wallet_address, api_key)
