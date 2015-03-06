from flask import Flask, request, redirect
from twilio.rest import TwilioRestClient
import twilio.twiml
import os

# log to stderr
import logging
from logging import StreamHandler


app = Flask(__name__)
file_handler = StreamHandler()
app.logger.setLevel(logging.DEBUG)  # set the desired logging level here
app.logger.addHandler(file_handler)

# PORT IN USE??? port 8000 in place of THE_PORT_NUMBER
# lsof -t -i tcp:THE_PORT_NUMBER | xargs kill
# lsof -t -i tcp:8000 | xargs kill


# if getting variables from config py file use:
# app.config.from_pyfile('path/to/config/config.py')

# if using variables from environment variables
print "This is the account key value" + os.environ.get('ACCOUNT_SID')
print "This is the auth token key value" + os.environ.get('AUTH_TOKEN')
client = TwilioRestClient(os.environ['ACCOUNT_SID'], os.environ['AUTH_TOKEN'])

shannon = os.environ['SHANNON']
nic = os.environ['NIC']
twilio_number_uk = os.environ['TWILIO_NUMBER_UK']
twilio_number_us = os.environ['TWILIO_NUMBER_US']

@app.route("/", methods=['GET', 'POST'])
def forwardMessages():
    """Forwards texts from Shannon (US) to Nic (UK) through Twilio API.
    Useful for those without international texting"""
    app.logger.debug("We're in the home request")
    sender = request.values.get("From")
    sms_body = request.values.get("Body")

    if sender and sms_body:


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
      app.logger.debug("Response from Twilio: " + str(resp))
      return str(resp)

    else:
      return "Got your request"


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    print "Magic happenin' on port %d" % port
    app.run(host='0.0.0.0', port=port)
    app.run(debug=True)
