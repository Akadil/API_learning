import requests

API_KEY = 'G___MwqgquWJK7Qk6VmouJ7qv28wYG20'

def get_transactions(wallet_address):
    url = f"https://api.blockchair.com/ethereum/dashboards/address/{wallet_address}"
    params = {'key': API_KEY}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        transactions = data['data'][wallet_address]['calls']
        
        for transaction in transactions:
            transaction_hash = transaction['transaction_hash']
            value = transaction['value']
            recipient = transaction['recipient']
            
            if value == 0:
                token_info = get_token_info(transaction_hash)
                token_name = token_info.get('token_name')
                token_symbol = token_info.get('token_symbol')
                token_value = token_info.get('token_value')
                print(f"Token Transfer: {token_name} ({token_symbol}), Value: {token_value}")
            else:
                print(f"Ether Transfer: Value: {value}, Recipient: {recipient}")
    else:
        print("Error occurred while fetching transactions.")

def get_token_info(transaction_hash):
    url = f"https://api.blockchair.com/ethereum/dashboards/transaction/{transaction_hash}"
    params = {'key': API_KEY}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        tokens = data['data'][transaction_hash]['contracts']
        
        if tokens:
            token = tokens[0]
            token_name = token.get('token_name')
            token_symbol = token.get('token_symbol')
            token_value = token.get('value')
            
            return {
                'token_name': token_name,
                'token_symbol': token_symbol,
                'token_value': token_value
            }
    return {}

# Replace 'YOUR_WALLET_ADDRESS' with the actual Ethereum wallet address
wallet_address = '0x8Fa3e40068aB20B74b94b83288E53cCdeDe79AE4'
get_transactions(wallet_address)
