board=["-","-","-",
       "-","-","-",
       "-","-","-"]

currentPlayer = 'x'

gameRunning = True

winner = None


def printboard(board):
  print(board[0] + " | "+board[1] +" | "+board[2])
  print("----------")
  print(board[3] +" | "+board[4] +" | "+board[5])
  print("----------")
  print( board[6] +" | "+board[7] +" | "+board[8])


def playerInput(board2):
  inp = int(input("enter the number from 1-9 : "))
  if inp>=1 and inp<=9 and board[inp-1] =='-':
    board[inp-1]= currentPlayer
  else:
    print("ouch , already another player in the spot ")


def horizontal(board):
  global winner 
  if board[0]== board[1]==board[2] and board[1] != '-':
    winner=board[0]
    return True
  elif board[3]== board[4]==board[5] and board[4] != '-':
    winner=board[3]
    return True
  elif board[6]== board[7]==board[8] and board[7] != '-':
    winner=board[6]
    return True
  
def vertical(board):
  global winner 
  if board[0]== board[3]==board[6] and board[3] != '-':
    winner=board[0]
    return True
  elif board[1]== board[4]==board[7] and board[4] != '-':
    winner=board[1]
    return True
  elif board[2]== board[5]==board[8] and board[5] != '-':
    winner=board[2]
    return True
  
def diagonal(board):
  global winner 
  if board[0]== board[4]==board[8] and board[4] != '-':
    winner=board[0]
    return True
  elif board[2]== board[4]==board[6] and board[4] != '-':
    winner=board[2]
    return True
  
def checktie(board):
  global gameRunning
  if '-' not in board:
    printboard(board)
    print("game is tie now")
    gameRunning= False

def switchplayer():
  global currentPlayer
  if currentPlayer=='x':
    currentPlayer='o'
  else:
    currentPlayer='x'

def checkwin(board):
  global winner, gameRunning
  if horizontal(board) or vertical(board) or diagonal(board):
    print(f" the winner is {winner}")
    gameRunning= False

while(gameRunning):
  printboard(board)
  playerInput(board)
  checkwin(board)
  checktie(board)
  switchplayer()