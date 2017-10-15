import pygsheets

client = pygsheets.authorize(service_file='client_secret.json')

def lookupKey(player, key):
# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
	if player == 'player1':
		sheet = client.open("NoteGame_Player1").sheet1
	elif player == 'player2':
		sheet = client.open("NoteGame_Player2").sheet1

	key_cell = sheet.find(str(key))
	note_cell = key_cell[0].neighbour('right')

	# Format cells to denote notes that have been found.
	key_cell[0].color = (0.956, 0.258, 0.874, 0.5)
	note_cell.color = (0.956, 0.258, 0.874, 0.5)

	note = note_cell.value

	return note
