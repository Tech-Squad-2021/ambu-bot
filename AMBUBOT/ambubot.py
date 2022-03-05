from flask import Flask, request
from twilio.rest import Client
import scrapper
import json
import os

from dotenv import load_dotenv
load_dotenv()

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# Load available cities
CITIES = json.load(open('./cities.json'))
ambulance = "\U0001F691"
medical = "\U00002695"

intro = """
Hey! I'm AmbuBot! {} {}

Before that, please send me you current location.

e.g. type "Kolkata" and Press the Send Button
""".format(ambulance, medical)

# helper function
def send_msg(sender_number, reciever_number, message):
    client.messages.create(
        to=reciever_number,
        from_=sender_number,
        body=message,
    )
    return ('', 200)


@app.route('/', methods=['POST'])
def AmbuBot():

    sender_number = request.form['From']
    reciever_number = request.form['To']
    msg_body = request.form['Body']

    print(msg_body)

    if msg_body == 'hi':
        send_msg(reciever_number, sender_number, intro)

    if msg_body == "1":
        send_msg(reciever_number, sender_number, 'Location?')
        print(msg_body, 'OK')

    if msg_body in CITIES:
        data = scrapper.getData(3, msg_body)
        send_msg(reciever_number, sender_number, str(data))

    return ('', 200)


if __name__ == '__main__':
    app.run()
