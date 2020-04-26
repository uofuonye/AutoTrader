import alpaca_trade_api as tradeapi
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
APCA_API_BASE_URL = os.getenv('AAPCA_API_BASE_URL')
MY_WATCHLIST_ID = os.getenv('MY_WATCHLIST_ID')

api = tradeapi.REST(API_KEY, API_SECRET, api_version='v2') # or use ENV Vars shown below
account = api.get_account()

print(api.get_watchlist(MY_WATCHLIST_ID))
print(account)
print(api.list_positions())
print(api.get_barset('AAPL', "1D", 1)) #Day stats of APPL stok