from ebaysdk.trading import Connection as Trading
import os

EBAY_CLIENT_ID = os.getenv('EBAY_CLIENT_ID')
EBAY_CLIENT_SECRET = os.getenv('EBAY_CLIENT_SECRET')
EBAY_USER_TOKEN = os.getenv('EBAY_USER_TOKEN')

def get_orders():
    api = Trading(appid=EBAY_CLIENT_ID, token=EBAY_USER_TOKEN)
    response = api.execute('GetOrders', {'NumberOfDays': 1})
    return response.dict()
