from twilio.twiml.messaging_response import MessagingResponse
from google.cloud import storage
import json

client = storage.Client()
bucket = client.get_bucket('gs://sms-noughts-and-crosses')
blob = bucket.get_blob('game.json')

filename = 'tempgame.json'

def receiveMessage(request):
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

    if intent == "help":
        return str("To start a game, say 'Start'.")
    elif intent == "new":
        gameData['gameboard'] = newGame()
    elif intent == "move":
        gameData['gameboard'] = makeMove(int(body), gameData['gameboard'])
    else:
       return("This input was incorrect, please try again.", gameData['phone']) 
    
def newGame():
    gameboard = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

    return gameboard

def makeMove(cell, board):
    if cell == 1:
        board[0][0] = 'X'
    elif cell == 2:
        board[0][1] = 'X'
    elif cell == 3:
        board[0][2] = 'X'
    elif cell == 4:
        board[1][0] = 'X'
    elif cell == 5:
        board[1][1] = 'X'
    elif cell == 6:
        board[1][2] = 'X'
    elif cell == 7:
        board[2][0] = 'X'
    elif cell == 8:
        board[2][1] = 'X'
    elif cell == 9:
        board[2][2] = 'X'

    return board

def writeStatus(state, gameboard):    
    toWrite = {}
    toWrite['state'] = state
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
