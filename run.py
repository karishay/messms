from flask import Flask, request, redirect
from twilio.rest import TwilioRestClient
import twilio.twiml
import os

app = Flask(__name__)

# PORT IN USE??? port 8000 in place of THE_PORT_NUMBER
# lsof -t -i tcp:THE_PORT_NUMBER | xargs kill


# if getting variables from config py file use:
# app.config.from_pyfile('path/to/config/config.py')

# if using variables from environment variables
print os.environ.keys()
client = TwilioRestClient(os.environ['ACCOUNT_SID'], os.environ['AUTH_TOKEN'])

shannon = os.environ['SHANNON']
nic = os.environ['NIC']
twilio_number_uk = os.environ['TWILIO_NUMBER_UK']
twilio_number_us = os.environ['TWILIO_NUMBER_US']

@app.route("/", methods=['GET', 'POST'])
def forwardMessages():
    """Forwards texts from Shannon (US) to Nic (UK) through Twilio API.
    Useful for those without international texting"""

    sender = request.values.get("From")
    sms_body = request.values.get("Body")

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

    resp = twilio.twiml.Response()
    print str(resp)
    return str(resp)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    print "Magic happenin' on port %d" % port
    app.run(host='0.0.0.0', port=port)
    app.run(debug=True)
