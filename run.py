from flask import Flask, request, redirect
from twilio.rest import TwilioRestClient
import twilio.twiml

app.config.from_pyfile('config.py')

client = TwilioRestClient(account_sid, auth_token)

app = Flask(__name__)

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
      #forward to nic
    else:
      # if it's from not shannon
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
