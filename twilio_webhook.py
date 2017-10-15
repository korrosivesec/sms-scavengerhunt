from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import sheets

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    key = int(request.values.get('Body', None))

    # Start our TwiML response
    resp = MessagingResponse()

    # # # Determine the right reply for this message
    if 10000 <= key <= 20000:
        note = sheets.lookupKey('player1', key)
    elif 30000 <= key <= 40000:
        note = sheets.lookupKey('player2', key)

    resp.message(note)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)