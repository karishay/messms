from flask import Flask, request, redirect
from twilio.rest import TwilioRestClient
import twilio.twiml

app = Flask(__name__)

app.config.from_pyfile('/Users/shannon/src/twilio/config/config.py')
client = TwilioRestClient(app.config['ACCOUNT_SID'], app.config['AUTH_TOKEN'])

shannon = app.config['SHANNON']
nic = app.config['NIC']
twilio_number_uk = app.config['TWILIO_NUMBER_UK']
twilio_number_us = app.config['TWILIO_NUMBER_US']

@app.route("/", methods=['GET', 'POST'])

def forwardMessages():
    """Forwards texts from Shannon (US) to Nic (UK) through Twilio API.
    Useful for those without international texting and/or dumbphones"""

    sender = request.values.get("From")
    sms_body = request.values.get("Body")


    # save the from number
    if sender == shannon:
    # if it's from Shannon
      forward_number = nic
      from_number = twilio_number_uk
      #forward to NIC
    else:
      # if it's from not SHANNON
      forward_number = shannon
      from_number = twilio_number_us
      # forward to Shannon
    forward_message = client.sms.messages.create(to=forward_number, from_=from_number, body=sms_body)

    #TODO: Ask why they need a response to be returned.
    resp = twilio.twiml.Response()
    # resp.message(sms_body)
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
