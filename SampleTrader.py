import alpaca_trade_api as tradeapi
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
APCA_API_BASE_URL = os.getenv('AAPCA_API_BASE_URL')

api = tradeapi.REST(API_KEY, API_SECRET, api_version='v2') # or use ENV Vars shown below
account = api.get_account()
print(account)
print(api.list_positions())