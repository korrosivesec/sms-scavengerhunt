import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

def lookupKey(player, key):
# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
	if player == 'player1':
		sheet = client.open("NoteGame_Player1").sheet1
	elif player == 'player2':
		sheet = client.open("NoteGame_Player2").sheet1

	keyCell = sheet.find(str(key))
	note = sheet.cell(keyCell.row, 2).value

	return note
