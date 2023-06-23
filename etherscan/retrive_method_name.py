import requests

def get_transaction_details(tx_hash, api_key):
    url = f"https://api.etherscan.io/api?module=proxy&action=eth_getTransactionReceipt&txhash={tx_hash}&apikey={api_key}"
    
    # Send the API request
    response = requests.get(url)
    data = response.json()
    
    # Check if the API request was successful
    if data["status"] == "1" and data["result"] is not None:
        # Retrieve the contract address and input data from the transaction receipt
        contract_address = data["result"]["contractAddress"]
        input_data = data["result"]["input"]
        
        return contract_address, input_data
    else:
        return None

def get_method_name(contract_address, input_data, api_key):
    url = f"https://api.etherscan.io/api?module=contract&action=getabi&address={contract_address}&apikey={api_key}"
    
    # Send the API request
    response = requests.get(url)
    data = response.json()
    
    # Check if the API request was successful
    if data["status"] == "1" and data["result"] is not None:
        abi = data["result"]
        
        # Find the method name from the ABI based on the input data
        for entry in abi:
            if "name" in entry and "type" in entry and entry["type"] == "function":
                method_signature = entry["name"] + "(" + entry["inputs"] + ")"
                method_id = Web3.sha3(text=method_signature)[:10].hex()
                
                if method_id == input_data[:10]:
                    return entry["name"]
        
    return None

# Specify the transaction hash for which you want to retrieve the method name
transaction_hash = "0xee4789561a207c81e4e207b32b35cec6e8733d033e0fc71a719b72bcc6acba6f"

# Provide your Etherscan API key
api_key = "A17TNTXIJF2ZIM9U11SGFUUWA3X3IAWDV8"

# Call the functions to retrieve the contract address and input data
contract_address, input_data = get_transaction_details(transaction_hash, api_key)

if contract_address is None:
    print("Unable to retrieve contract address and input data.")
else:
    # Call the function to retrieve the method name
    method_name = get_method_name(contract_address, input_data, api_key)
    
    if method_name is None:
        print("Unable to retrieve method name.")
    else:
        print(f"Method Name: {method_name}")
