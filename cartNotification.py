import base64
import json
import os
import urllib
from urllib import request, parse
 
 
TWILIO_SMS_URL = "https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json"
TWILIO_ACCOUNT_SID = "ACef3608a9615df025b60da162d0ad8590"
TWILIO_AUTH_TOKEN = "8f07c5adf7bca8cfc305e2a2b25decb8"
 
 
def lambda_handler(event, context):
    to_number = event['to']
    from_number = event['from']
    body = event['body']
 
    if not TWILIO_ACCOUNT_SID:
        return "Unable to access Twilio Account SID."
    elif not TWILIO_AUTH_TOKEN:
        return "Unable to access Twilio Auth Token."
    elif not to_number:
        return "The function needs a 'To' number in the format +12023351493"
    elif not from_number:
        return "The function needs a 'From' number in the format +19732644156"
    elif not body:
        return "The function needs a 'Body' message to send."
 
    # insert Twilio Account SID into the REST API URL
    populated_url = TWILIO_SMS_URL.format(TWILIO_ACCOUNT_SID)
    post_params = {"to": to_number, "from": from_number, "body": body}
 
    # encode the parameters for Python's urllib
    data = parse.urlencode(post_params).encode()
    req = request.Request(populated_url)
    print(req)
 
    # add authentication header to request based on Account SID + Auth Token
    authentication = "{}:{}".format(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    base64string = base64.b64encode(authentication.encode('utf-8'))
    req.add_header("Authorization", "Basic %s" % base64string.decode('ascii'))
 
    try:
        # perform HTTP POST request
        with request.urlopen(req, data) as f:
            print("Twilio returned {}".format(str(f.read().decode('utf-8'))))
    except Exception as e:
        # something went wrong!
        return e
 
    return "SMS sent successfully!"
