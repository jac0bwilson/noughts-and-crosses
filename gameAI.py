def move(board):
    #board = 3x3 array
    #[[1,2,3]]
    #[[4,5,6]]
    #[[7,8,9]]
    #
    #0:0,1,2
    #1:0,1,2
    #2:0,1,2
    #
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

def printBoard(board):
    return (board[0][0] + "|" + board[0][1] + "|" + board[0][2] + "\n" + "-----" + "\n" + 
            board[1][0] + "|" + board[1][1] + "|" + board[1][2] + "\n" + "-----" + "\n" +
            board[2][0] + "|" + board[2][1] + "|" + board[2][2])