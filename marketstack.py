import os # for accessing environment variable 
import requests
import json

# Fetch the environment variable that holds the api key
API_KEY = os.environ.get('MARKETSTACK_KEY')

# base url needed for working with the marketstack api
BASE_URL = 'http://api.marketstack.com/v1/'

# Function for fetching the necessary data from marketstack.
def get_stock_info(stock_symbol):
    params = {
        'access_key': API_KEY
    }
    # Creating a string for end point URL
    end_point = ''.join([BASE_URL, 'tickers/', stock_symbol, '/eod/latest'])

    # Store the result from marketstack api for the specified stock
    api_result = requests.get(end_point, params)
    print(api_result)

    # Convert the api result to json
    json_result = json.loads(api_result.text)

    # Convert info to string values which are needed in the app.py file
    return {
        'symbol': str(json_result['symbol']),
        'opening_price': str(json_result['open']),
        'high_price': str(json_result['high']),
        'low_price': str(json_result['low']),
        'closing_price': str(json_result['close']),
        'volume': str(json_result['volume'])
    }