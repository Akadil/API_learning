from requests import get, RequestException
from datetime import datetime

class   etherscan:
    BASE_URL = "https://api.etherscan.io/api"
    ETHER_VALUE = 10 ** 18

    def __init__(self, address, api_key = "A17TNTXIJF2ZIM9U11SGFUUWA3X3IAWDV8"):
        self.api_key = api_key
        self.address = address

    def make_api_url(self, module, action, address, **kwargs):
        url = self.BASE_URL + f"?module={module}&action={action}&address={address}&apikey={self.api_key}"

        for key, value in kwargs.items():
            url += f"&{key}={value}"

        return url
    
    def make_transaction(self, data, **kwargs):
        transaction = {}
        transaction["hash"] = data["hash"]
        transaction["time"] = datetime.fromtimestamp(int(data["timeStamp"]))
        transaction["from"] = data["from"]/mnt/nfs/homes/akalimol/my_git/side_frenchTax/srcs/etherscan/main.py
        transaction["to"] = data["to"]
        if ("methodId" in data.keys()):
            transaction["method"] = data["methodId"]
        else:
            transaction["method"] = None
        transaction["value"] = int(data["value"]) / self.ETHER_VALUE
        transaction["fee"] = int(data["gasPrice"]) * int(data["gasUsed"]) / self.ETHER_VALUE
        transaction["price"] = None

        if transaction["from"] == self.address:
            transaction["direction"] = "in"
        else:
            transaction["direction"] = "out"
        
        if (transaction["method"] is None):
            transaction["method"] = "Undefined"
        elif (transaction["method"] == "0x"):
            transaction["method"] = "transfer"
        elif (transaction["method"] == "0xb6b55f25"):
            transaction["method"] = "deposit"
        elif (transaction["method"] == "0x095ea7b3"):
            transaction["method"] = "approve"
        elif (transaction["method"] == "0xa9059cbb"):
            transaction["method"] = "transfer"
        elif (transaction["method"] == "0x5ae401dc"):
            transaction["method"] = "multicall"
        elif (transaction["method"] == "0x745400c9"):
            transaction["method"] = "Request Withdraw"
        elif (transaction["method"] == "0xf3fef3a3"):
            transaction["method"] = "Withdraw"
        else:
            transaction["method"] = "Undefined"


        if (transaction["value"] != 0):
            if "name" in kwargs.keys():
                transaction["name"] = kwargs["name"]
            else:
                transaction["name"] = "ethereum"
            if "symbol" in kwargs.keys():
                transaction["symbol"] = kwargs["symbol"]
            else:
                transaction["symbol"] = "ETH"
        else:
            if "name" in kwargs.keys():
                transaction["name"] = kwargs["name"]
            else:
                transaction["name"] = None
            if "symbol" in kwargs.keys():
                transaction["symbol"] = kwargs["symbol"]
            else:
                transaction["symbol"] = None
        
        return transaction
    


    def get_account_balance(self):
        
        balance_url = self.make_api_url("account", "balance", self.address, tag="latest")
        
        try:
            response = get(balance_url)
            if response.status_code == 200:
                data = response.json()

                value = int(data["result"]) / self.ETHER_VALUE
                return value
            else:
                 print(f"Error: Request failed with status code {response.status_code}")

        except RequestException as e:
            print(f"Error: {str(e)}")

        return -1
    
    def get_transactions(self):

        transactions_url = self.make_api_url("account", "txlist", self.address, 
				                        startblock=0, 
				                        endblock=99999999, 
					                    page=1, 
					                    offset=10000, 
					                    sort="asc")

        data = []
        try:
            response = get(transactions_url)
            data = response.json()["result"]
            new_data = []
            for tx in data:
                new_data.append(self.make_transaction(tx))
            data = new_data
        except  RequestException as e:
            print(f"Error: {str(e)}")
        

        internal_tx_url = self.make_api_url("account", "txlistinternal", self.address, 
                                            startblock=0, 
                                            endblock=99999999, 
                                            page=1, 
                                            offset=10000, 
                                            sort="asc")

        data2 = []
        try:
            response2 = get(internal_tx_url)
            data2 = response2.json()["result"]
            new_data = []
            for tx in data2:
                new_data.append = self.make_transaction(tx)
            data2 = new_data
        except RequestException as e:
            print(f"Error: {str(e)}")

        data.extend(data2)


        transactions_url = self.make_api_url("account", "tokentx", self.address, 
                                            startblock=0, 
                                            endblock=99999999, 
                                            page=1, 
                                            offset=10000, 
                                            sort="asc")
        
        tokens = []
        try:
            response = get(transactions_url)
            tokens = response.json()["result"]
        except RequestException as e:
            print(f"Error: {str(e)}")

        # for key, value in tokens[0].items():
        #     print(key, " -> ", value)

        for tx in data:
            if int(tx["value"]) == 0:
                my_token = self.get_proper_token(tokens, tx["hash"])
                if my_token is not None:
                    tx["value"] = int(my_token["value"]) / self.ETHER_VALUE
                    tx["name"] = my_token["tokenName"]
                    tx["symbol"] = my_token["tokenSymbol"]
                    tokens.remove(my_token)

        for tx in tokens:
            data.append(self.make_transaction(tx, name=tx["tokenName"], symbol=tx["tokenSymbol"]))

        data = sorted(data, key=lambda x: x["time"])

        return data


    def get_proper_token(self, tokens, hash):
        for token in tokens:
            if token["hash"] == hash:
                return token
        return None
