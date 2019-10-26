from twilio.twiml.messaging_response import MessagingResponse
from google.cloud import storage
import json

client = storage.Client()
bucket = client.get_bucket('gs://sms-noughts-and-crosses')

FileExists = False
try:
    blob = bucket.get_blob('game.json')
    FileExists = True
    

filename = 'tempgame.json'

def receiveMessage(request):
    if FileExists:
        blob.download_to_filename(filename)

    gameData = {}
    gameData = json.load(filename)

    request_json = request.get_json()
    request_args = request.args

    if request_json and 'Body' in request_json:
        body = request_json['Body']
    elif request_args and 'Body' in request_args:
        body = request_args['Body']
    else:
        body = 'Default'
    
    intent = identifyIntent(body)

    if intent == 'move' and (gameData['gameboard'] == 'X' or gameData['gameboard']):
        return str("You cannot play a move with this location, it has already been taken!")

    if intent == "help":
        return str("To start a game, say 'Start'.")
    elif intent == "new":
        gameData['gameboard'] = newGame()
        writeStatus(gameData['gameboard'])
    elif intent == "move":
        gameData['gameboard'] = makeMove(int(body), gameData['gameboard'])
        gameData['gameboard'] = AIMove(gameData['gameboard'])
        writeStatus(gameData['gameboard'])
        result = isWin(gameData['gameboard'])

        if result == 'X':
            return str("You win!")
        elif result == 'O':
            return str("You lose! Better luck next time!")
    else:
       return("This input was incorrect, please try again.", gameData['phone']) 
    
def newGame():
    gameboard = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

    return gameboard

def makeMove(cell, board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == cell:
                cell = 'X'

    return board

def AIMove(board):
    freeSpaces = []
    for row in freeSpaces:
        for elem in row:
            if (elem.isnumeric()) :
                freeSpaces.append(elem)
    

    if ((((board[0][1] == 'X') and (board[0][2] == 'X')) or ((board[1][0] == 'X') and (board[2][0] == 'X')) or ((board[2][2] == 'X') and (board[1][1] == 'X'))) and ('1' in freeSpaces)):
        return 1
    elif ((((board[0][0] == 'X') and (board[0][2] == 'X')) or ((board[1][1] == 'X') and (board[2][1] == 'X'))) and ('2' in freeSpaces)):
        return 2
    elif ((((board[0][0] == 'X') and (board[0][1] == 'X')) or ((board[1][2] == 'X') and (board[2][2] == 'X')) or ((board[2][0] == 'X') and (board[1][1] == 'X'))) and ('3' in freeSpaces)):
        return 3
    elif ((((board[1][1] == 'X') and (board[1][2] == 'X')) or ((board[0][0] == 'X') and (board[2][0] == 'X'))) and ('4' in freeSpaces)):
        return 4
    elif ((((board[1][0] == 'X') and (board[1][2] == 'X')) or ((board[0][1] == 'X') and (board[2][1] == 'X')) or ((board[2][2] == 'X') and (board[0][0] == 'X')) or ((board[0][2] == 'X') and (board[2][0] == 'X'))) and ('5' in freeSpaces)):
        return 5
    elif ((((board[1][0] == 'X') and (board[1][1] == 'X')) or ((board[0][2] == 'X') and (board[2][2] == 'X'))) and ('6' in freeSpaces)):
        return 6
    elif ((((board[2][1] == 'X') and (board[2][2] == 'X')) or ((board[0][0] == 'X') and (board[1][0] == 'X')) or ((board[0][2] == 'X') and (board[1][1] == 'X'))) and ('7' in freeSpaces)):
        return 7
    elif ((((board[2][0] == 'X') and (board[2][2] == 'X')) or ((board[0][1] == 'X') and (board[1][1] == 'X'))) and ('8' in freeSpaces)):
        return 8
    elif ((((board[2][0] == 'X') and (board[2][1] == 'X')) or ((board[0][2] == 'X') and (board[1][2] == 'X')) or ((board[0][0] == 'X') and (board[1][1] == 'X'))) and ('9' in freeSpaces)):
        return 9
    else: 
        return freeSpaces[0]

def isWin(board):
    if ((board[0][0] == 'X') and (board[0][1] == 'X') and (board[0][2] == 'X')):
        return 'X'
    elif ((board[1][0] == 'X') and (board[1][1] == 'X') and (board[1][2] == 'X')):
        return 'X'
    elif ((board[2][0] == 'X') and (board[2][1] == 'X') and (board[2][2] == 'X')):
        return 'X'
    elif ((board[0][0] == 'X') and (board[1][0] == 'X') and (board[2][0] == 'X')):
        return 'X'
    elif ((board[0][1] == 'X') and (board[1][1] == 'X') and (board[2][1] == 'X')):
        return 'X'
    elif ((board[0][2] == 'X') and (board[1][2] == 'X') and (board[2][2] == 'X')):
        return 'X'
    elif ((board[0][0] == 'X') and (board[1][1] == 'X') and (board[2][2] == 'X')):
        return 'X'
    elif ((board[0][2] == 'X') and (board[1][1] == 'X') and (board[2][0] == 'X')):
        return 'X'
    
    elif ((board[0][0] == 'O') and (board[0][1] == 'O') and (board[0][2] == 'O')):
        return 'O'
    elif ((board[1][0] == 'O') and (board[1][1] == 'O') and (board[1][2] == 'O')):
        return 'O'
    elif ((board[2][0] == 'O') and (board[2][1] == 'O') and (board[2][2] == 'O')):
        return 'O'
    elif ((board[0][0] == 'O') and (board[1][0] == 'O') and (board[2][0] == 'O')):
        return 'O'
    elif ((board[0][1] == 'O') and (board[1][1] == 'O') and (board[2][1] == 'O')):
        return 'O'
    elif ((board[0][2] == 'O') and (board[1][2] == 'O') and (board[2][2] == 'O')):
        return 'O'
    elif ((board[0][0] == 'O') and (board[1][1] == 'O') and (board[2][2] == 'O')):
        return 'O'
    elif ((board[0][2] == 'O') and (board[1][1] == 'O') and (board[2][0] == 'O')):
        return 'O'

    else:
        return 'No-one!'

def writeStatus(gameboard):    
    toWrite = {}
    toWrite['gameboard'] = gameboard

    with open(filename, 'w') as f:
        json.dump(toWrite, f)

    blob.upload_from_filename(filename)

def identifyIntent(message):
    if message.lower() == "help" or message.lower() == "hello" or message.lower() == "hi":
        return "help"
    elif "start" in message.lower():
        return "new"
    elif message.isnumeric():
        return "move"
    else:
        return "error"
