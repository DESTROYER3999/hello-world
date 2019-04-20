#print (theBoard)

def drawBoard(board):

  # This function prints out the board that it was passed.
  # "board" is a list of 10 strings representing the board (ignore index 0)

  print('|' + '---------------------------' + '|')

  print('|        |         |        |')
  print('|' + board[7] + '       |  ' + board[8] + '      | ' + board[9] + '      |')
  print('|        |         |        |')

  print('|' + '---------------------------' + '|')

  print('|        |         |        |')
  print('|' + board[4] + '       |  ' + board[5] + '      | ' + board[6] + '      |')
  print('|        |         |        |')

  print('|' + '---------------------------' + '|')


  print('|        |         |        |')
  print('|' + board[1] + '       |  ' + board[2] + '      | ' + board[3] + '      |')
  print('|        |         |        |')

  print('|' + '---------------------------' + '|')

def choosePlayerSide():
  side = ''
  while not (side == '*' or side == '+'):
    print('Do you want to be * or + ?')
    side = input()

    if side == '*':

      return ['*', '+']

    else:

      return ['+', '*']


def makeMove(board, side, move):

  board[move] = side





# This is where we will put our testing code as we go.
testing = True

while testing:
  theBoard = ['', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
  drawBoard(theBoard)
  side = choosePlayerSide()
  print(side)
  theBoard = [side,side,side, ' ', ' ', ' ', ' ', ' ', ' ', ' ']
  drawBoard(theBoard)
  move = 1

  result = makeMove(theBoard, side, move)

  testing = False