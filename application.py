# Import statements for flask
from flask import Flask
from flask import request

# Import openai 
import openai

# Need to work with the twilio api
from twilio.rest import Client

# For accessing environment variables
import os

# Initialize the flask application
app = Flask(__name__)

# Fetch needed environment variables
ACCOUNT_ID = os.environ.get('TWILIO_ACCOUNT')
TWILIO_TOKEN = os.environ.get('TWILIO_TOKEN')

# OpenAI api key
openai.api_key = os.getenv("OPENAI_API_KEY")

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

def get_msg_resp(msg):
    print(msg)
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=msg + "\n",
    temperature=0.3,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return "OpenAI:\n" + response["choices"][0]['text']

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
    response = get_msg_resp(msg)
    send_msg(response, sender)

    return 'OK', 200