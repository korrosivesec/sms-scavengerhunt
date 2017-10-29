# ${1:Project Name}

These scripts can be used to setup a SMS based scavenger hunt or to enable basic covert communication between people.  See the usage section below for more details.

Using Google Sheets as the data source enables less technical people to participate once some initial configuration is done.  Adding or editing clues is as easy as editing a field in a spreadsheet.

## How it works

Twilio will listen for an incoming SMS message and then send a POST to an AWS API gateway that forwards the message on to the lookup script we'll host on AWS Lambda.

The lookup script checks queries the associated clue/note from Google Sheets and the clue/note is then passed back to the user.

## Requirements

# Modules
pygsheets - https://github.com/nithinmurali/pygsheets - Google Sheets API module
twilio - https://www.twilio.com/docs/libraries/python - Twilio module
Flask - http://flask.pocoo.org/ - Webhook listener
*Zappa - https://github.com/Miserlou/Zappa - Not technically required, but will make deployment a lot easier.

# Accounts/Services
Twilio SMS - https://www.twilio.com/sms - These are inexpensive and the Twilio API rocks.
Google Account with Sheets access
Amazon AWS account


## Installation

Ensure you have all the required python modules and service accounts configured.

1. Using the instructions located at https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html, configure a Google Drive API Service Account.  This method is prefered over OAuth authentication since you can just have other players give the service account email address access to their sheets.

2. Copy the client_secret.json file created in step one to your project root.

4. Create your Google Sheet.  As is, the code is setup for two players.  Only one can be used for scavenger hunt mode or addtional players can be added by modifying the scripts.  Sheets should be created in the format "NoteGame_Player1" and "NoteGame_Player2".

Each sheet should have two columns with headers "key" and "note".  Populate the sheet as desired.  It is recommended to randomize the keys to discourage simple iteration of the notes.


3. Inside the client_secret.json is a client_email key.  Note the associated email address and share your previously created Google Sheets with that email address.

4. Using the instructions in the Zappa README, initialize Zappa and configure it to work with your AWS.  Once initialized, deploy to AWS.



## Usage

# Scavenger Hunt Mode

Plan out your hunt and populate the associated Google Sheet with associated clue numbers and notes. Then give the players your configured Twilio number and the starting clue number.  One of the benefits of placing clue numbers instead of notes, is that you can alter clues on the fly should you need to adjust the challenge

# Note Swap Mode

Each player will need to create their own Google Sheet and use a predefined range of numbers as their designated range.  Then they add their range of numbers and note messages to the sheet.  Players can place paper notes with the numbers as they see fit and.  Once another player finds a slip, they text the agreed upon SMS number to retreive the note.  This mode is useful when you want to leave notes for someone, without exposing the specific content.  Should someone else happen to come across the note, they will just see the note number with no context regarding what it might represent.
