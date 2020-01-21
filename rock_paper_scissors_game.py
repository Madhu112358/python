'''Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)'''
#Print Message
print (" ---- Rock Paper Scissors ---- \n Choose one of the following options for 2 players and we  will tell you who the winner is!! \n 1. Rock \n 2. Paper \n 3. Scissors")

def game():  
  options = ['1','2','3']
  Player_1 = input("Enter your choice for Player 1 : ")
  Player_2 = input("Enter your choice for Player 2 : ")
  if (Player_1 == Player_2) and Player_1 in options and Player_2 in options:
    print ( "Game Draws!")
  elif (Player_1 == '1' and Player_2 == '3') or           (Player_1 == '2' and Player_2 == '1') or                (Player_1 == '3' and Player_2 == '2'):
      print ( "Player_1 Wins!")
  elif (Player_1 == '1' and Player_2 == '2') or           (Player_1 == '2' and Player_2 == '3') or                (Player_1 == '3' and Player_2 == '1'): 
      print ( "Player_2 Wins!") 
  else:
    print("Invalid Choices! Please enter options - 1 ,2 or 3")
  Play_Again = input("Do you want to Play again? - Y / N ")
  if (Play_Again == 'Y') or (Play_Again == 'y'):
     game()
  elif (Play_Again == 'N') or (Play_Again == 'n'):
    print ("Thanks for Playing !")      
  else:
    print("Invalid Option! Thanks for Playing!")
game()  


