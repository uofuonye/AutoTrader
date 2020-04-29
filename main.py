import alpaca_trade_api as tradeapi
from src.Account import Account
from src.Market import Market

API_KEY = 'PKMT6EBLX6VRI2CYZDHW'
API_SECRET = 'pqZqANLoxjj7KOz01NZOaTCrwv7Guun8jeitIiG7'
APCA_API_BASE_URL = 'https://paper-api.alpaca.markets'
VERSION = 'v2'

def main():
    api = tradeapi.REST(API_KEY, API_SECRET, APCA_API_BASE_URL, VERSION)
    myAccount = Account(api)
    market = Market()
    market.Run(myAccount)    

if __name__ == "__main__": 
    main()