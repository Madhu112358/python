
import string
def drawGame(count,ttt):
  print (" --- --- ---")
  for x in range(count):
    for y in range(count):
      print("|",ttt[x][y],end=" ")
    print("|")
    print (" --- --- ---")

def getInput(ttt):
  class Error(Exception):
   """Base class for other exceptions"""
   pass
  class InvalidValues(Error):
   """Raised when the input value is not valid"""
   pass
  class CellTaken(Error):
   """Raised when the input value is not valid"""
   pass
  while True:
    try:
      user_input = input("Enter row and col :")
      [row,col] = str.split(user_input,",")
      if (row not in ["1","2","3"]) or (col not in ["1","2","3"]):
        raise InvalidValues
      else:
        row = int(row)
        col = int(col)
        if ttt[row-1][col-1] != 0:
          raise CellTaken
        else:    
         return row,col
    except ValueError:
      print("Please enter in format 'row,column'")
    except InvalidValues:
      print("Row and Column should be between 1,2 or 3")
    except CellTaken:
      print("Please enter different coordinates. Cell already holds: ",ttt[row-1][col-1] )


def checkTable(x,y,player_1,player_2):
  if ttt[x][y] == "X":
    player_1 = player_1+1
  elif  ttt[x][y] == "@":
    player_2 = player_2+1
  return player_1,player_2

def checkWinner(player_1,player_2):
  won = 0
  if player_1 == 3:
    print("Player 1 won the game")
    won = 1
  elif player_2 == 3 :
    print("Player 2 won the game")
    won = 1
  return won

def checkWin():
  for x in range(3):
    player_1 = player_2 =0
    for y in range(3):  
      [player_1,player_2] = checkTable(x,y,player_1,player_2)   
    won = checkWinner(player_1,player_2) 
    if won:return won  

  if not won:  
    for x in range(3):
      player_1 = player_2 =0
      for y in range(3):  
        [player_1,player_2] = checkTable(y,x,player_1,player_2)    
      won = checkWinner(player_1,player_2) 
      if won:return won
 
  if not won:
    player_1 = player_2 =0
    for x in range(3):
      [player_1,player_2] = checkTable(x,x,player_1,player_2)
    won = checkWinner(player_1,player_2)
    return won


print("Welcome to Tic Tac Toe!")
count = 3
ttt = [[0 for x in range (3)] for y in range(3)] 
drawGame(count,ttt)
turn = 1
won = 0
while turn <=9 and not won :  
  if turn%2 != 0: #PLAYER 1
    print("Enter coords - Player1(X) for turn ",turn)
    [row,col] = getInput(ttt)
    ttt[row-1][col-1] = "X"   
    drawGame(count,ttt)
    turn = turn +1
    won = checkWin()
  elif turn%2 == 0 and not won: #PLAYER 2
    print("Enter coords for Player2(O) for turn ",turn)
    [row,col] = getInput(ttt)
    ttt[row-1][col-1] = "@"
    drawGame(count,ttt)
    turn = turn + 1
    won = checkWin()
