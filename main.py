import alpaca_trade_api as tradeapi
from src.Account import Account
from src.Market import Market

API_KEY = 'PK0UL2ZY0EGTQMI1MF84'
API_SECRET = 'jdxvG/S1oCwKPiIXvBjwGYW00uLm1HejcsObk7UR'
APCA_API_BASE_URL = 'https://paper-api.alpaca.markets'
VERSION = 'v2'

def main():
    api = tradeapi.REST(API_KEY, API_SECRET, APCA_API_BASE_URL, VERSION)
    myAccount = Account(api)
    market = Market()
    market.Run(myAccount)    

if __name__ == "__main__": 
    main()