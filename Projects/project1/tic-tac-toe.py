# TASK - Build a 3 x 3 TIC-TAC-TOE Game
# Create the board
# Access the board
# Check for win or draw
# Switche player
# check for win

# prerequisite
# list comprehension
# spliting string
# converting list of characters into spring

# Revision
# List comprehension
# print list of even numbers from 0 to 10
# print([item for item in range(0, 11, 2)])

# # spliting strings
# str = "Hello!"
# print([*str])

# str = "Hi, Mrs. Jacobin, welcome to TAAcodeep"
# print(str.split(' '))
# print(str.split(' ', 1))
# print(str.split(' ', 0))
# print(str.split())
# print(str.split('e'))

# # To join (attach) something to an existing one
# print('$'.join(["10 ", "20 ", "30 ", "40 "]))
# print(" $ ".join(["10", "20", "30", "40"]))
# print(" ".join(["10 ", "20 ", "30 ", "40 "]))

# board = [
#     "-", "-", "-",
#     "-", "-", "-",
#     "-", "-", "-",
# ]

board = ['-' for _ in range(9)]

current_player = 'X'
winner = None
game_running = True

# Show board
# def showBoard(board):
#     print(board[0] + " | " + board[1] + " | " + board[2])
#     print("----------")
#     print(board[3] + " | " + board[4] + " | " + board[5])
#     print("----------")
#     print(board[6] + " | " + board[7] + " | " + board[8])
#     print("----------")

# showBoard(board)

def showBoard(board):
    for row in[board[i*3: (i+1)*3]for i in range(3)]:
        print(" | ".join(row)) # {" | ".join(["-", "-", "-"])}

# Take user input
# select a number from 1 - 9, number must not be already taken
def playerInput(board):
    inputVal = int(input("Enter a number 1 - 9: "))
    if(inputVal >= 1 and inputVal <= 9 and board[inputVal -1] == "-"):
        board[inputVal -1] = current_player
    else:
        print("wrong input/Player already choose this space")

# Check for  WIN
# Horizontal win
# def checkHoriz(board):
#     global winner
#     if(board[0] == board[1] == board[2] and board[0] != "-"):
#         winner = board[0]
#         return True
#     elif(board[3] == board[4] == board[5] and board[3]!= "-"):
#         winner = board[3]
#         return True
#     elif(board[6] == board[7] == board[8] and board[6] != "-"):
#         winner = board[6]
#         return True

def checkHoriz(boardArr):
    global winner
    for item in range(3):
        if(len({i for i in boardArr[item]}) == 1):
            return True


# Horizontal win
def checkHoriz(board):
    global winner
    if(board[0] == board[3] == board[6] and board[0] != "-"):
        winner = board[0]
        return True
    elif(board[1] == board[4] == board[7] and board[1]!= "-"):
        winner = board[1]
        return True
    elif(board[2] == board[5] == board[8] and board[2] != "-"):
        winner = board[2]
        return True

def checkHoriz(boardArr):
    global winner
    for item in range(3):
        if(len({row[item] for row in boardArr}) == 1 and [row[item] for row in boardArr][0] != "-" ):
            winner = [row[item] for row in boardArr][0]
            return True

# Check Diagonal
def checkDiagonal(board):
    global winner
    if(board[0] == board[4] == board[8] and board[0] != "-"):
        winner = board[0]
        return True
        
    elif(board[2] == board[4] == board[6] and board[2] != "-"):
        winner = board[2]
        return True

def checkDiagonal(boardArr):
    global winner
    if(len({boardArr[p][p] for p in range(3)}) == 1 and [boardArr[p][p] for p in range(3)][0] != "-"):
        winner = [boardArr[p][p] for p in range(3)][0]
        return True
    elif(len({boardArr[-p-1][p] for p in range(3)}) == 1 and [boardArr[-p-1][p] for p in range(3)][0] != "-"):
        winner = [boardArr[-p-1][p] for p in range(3)][0]
        return True

# Check Winner
def checkWinner():
    global game_running
    if(checkHoriz([board[i*3: (i+1)*3]for i in range(3)])):
        showBoard(board)
        print(f"The winner is {winner}")
        game_running = False
    elif(checkHoriz([board[i*3: (i+1)*3]for i in range(3)])):
        showBoard(board)
        print(f"The winner is {winner}")
        game_running = False
playerInput(board)
showBoard(board)
