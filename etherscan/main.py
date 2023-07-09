import etherscan as es
import requests
from datetime import datetime 

ether = es.etherscan("0x8Fa3e40068aB20B74b94b83288E53cCdeDe79AE4")

transactions = ether.get_transactions()

def get_crypto_price(crypto_symbol, datetime):
    # Reformat datetime
    formatted_datetime = datetime.strptime(str(datetime), "%Y-%m-%d %H:%M:%S").timestamp()

    url = f"https://min-api.cryptocompare.com/data/pricehistorical?fsym={crypto_symbol}&tsyms=USD&ts={formatted_datetime}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if crypto_symbol not in data.keys():
            return "None"
        data = data[crypto_symbol]
        if 'USD' in data:
            price = data['USD']
            return price
    return "None"

# print(str(transactions[0]["time"])[:10])
# print(transactions[0]["time"])

print("-----------------------------------------------------------------------------------------------------------------")
print("| {:9} | {:20} | {:20} | {:12} | {:20} | {:7} | {:3} |".format("method", "time", "fee", "name", "value", "price", "dir"))
print("-----------------------------------------------------------------------------------------------------------------")
for tx in transactions:
    if (tx["method"] == "approve" or tx["method"] == "Request Withdraw"):
        continue
    # print(tx["method"], tx["name"], tx["value"], "\n")
    # print(tx, "\n")
    print("| {:9} | {:20} | {:<20} | {:12} | {:20} | {:7} | {:3} |".format(tx["method"], str(tx["time"]), 
                                                                    str(tx["fee"]), tx["name"], 
                                                                    str(tx["value"]), get_crypto_price(tx["symbol"], tx["time"]), tx["direction"]), end="")
    print(" ", tx["symbol"], end="")
    # print(" ", get_crypto_price(tx["symbol"], tx["time"]), end="")
    print()
print("-----------------------------------------------------------------------------------------------------------------")