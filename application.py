# Import statements for flask
from flask import Flask
from flask import request

# Need to work with the twilio api
from twilio.rest import Client

# For accessing environment variables
import os

from marketstack import get_stock_info 

# Initialize the flask application
app = Flask(__name__)

# Fetch needed environment variables
ACCOUNT_ID = os.environ.get('TWILIO_ACCOUNT')
TWILIO_TOKEN = os.environ.get('TWILIO_TOKEN')

# Twilio number for sending messages
TWILIO_NUMBER = 'whatsapp:+14155238886'

# Initialize the twilio client with environment variables
client = Client(ACCOUNT_ID, TWILIO_TOKEN)

# Function used to send a message using the twilio api
def send_msg(msg, recipient):
    client.messages.create(
        from_=TWILIO_NUMBER,
        body=msg,
        to=recipient
    )

# Function needed for message processing
def process_msg(msg):
    response = ""

    if msg == 'Help':
        response = 'Hello, welcome to the MarketStackBot! '
        response += 'Type $<stock_symbol> to get the latest information on a stock'
    elif '$' in msg:
        data = msg.split('$')

        # Get just the stock symbol from the input "aapl"
        stock_symbol = data[1]

        # Use the imported function from the marketstack.py file by sending in the stock symbol
        stock_info = get_stock_info(stock_symbol)
        
        # Format our response for the user
        response = "$" + stock_info['symbol'] + " info:\n" \
            + "Open: " + stock_info['opening_price'] + "\n"\
            + "High: " + stock_info['high_price'] + "\n" \
            + "Low: " + stock_info['low_price'] + "\n" \
            + "Close: " + stock_info['closing_price'] + "\n" \
            + "Volume: " + stock_info['volume']

    else:
        response = 'Please type <Help> for instructions on how to run the MarketStackBot'
    return response

@app.route('/')
def hello():
    return "Hello World"

# The webhook that twilio routes messages to.
@app.route('/webhook', methods=["POST"])
def webhook():
    f = request.form

    # Get the message and number from the sender so that we can return
    # our response to them.
    msg = f['Body']
    sender = f['From']
    response = process_msg(msg)
    send_msg(response, sender)

    return 'OK', 200