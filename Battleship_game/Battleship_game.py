from random import randint                                                                  #import randint from random module to generate a random integer

board = []                                                                                  #create an empty list for the game board

print ("Welcome to the Battleship Game!")
print()
print ("Game Rules:")
print ("1. The ocean is of dimension 5X5, i.e, the rows are from 1 to 5 and the columns are from 1 to 5.")
print ("2. Any other values out of this range will be considered as out of the ocean.")
print ("3. The user will get 5 chances to guess the location of the battleship in the ocean.")
print()

for x in range(5):                                                                          #create the board
  board.append(["O"] * 5)

def print_board(board):                                                                     #function to print the board
  for row in board:
    print (" ".join(row))

print_board(board)

def random_row(board):                                                                      #function to generate the row of the ship
  return randint(0, len(board) - 1)

def random_col(board):                                                                      #function to generate the column of the ship
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)


for turn in range(5):                                                                       #to provide 5 chances
  print ()
  print ("Turn", turn+1)

  guess_row = int(input("Guess Row: "))                                                     #take row input from the user
  guess_row = guess_row -1
  guess_col = int(input("Guess Column: "))                                                  #take column input from the user
  guess_col = guess_col -1

  if guess_row == ship_row and guess_col == ship_col:                                       #to check if the input matches the actual location of the ship
    print ("Congratulations! You sunk my battleship!")
    break
  else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):                #to warn if the input is out of the ocean's range
      print ("Oops! That's not even in the ocean.")
    elif(board[guess_row][guess_col] == "X"):                                               #to warn if the input is repeated
      print ("You guessed that one already.")
    else:                                                                                   #to warn if the input doesn't matches the actual location
      print ("You missed my battleship!")
      board[guess_row][guess_col] = "X"
    print_board(board)
    
    if turn == 4:                                                                           #to provide ending message
      print ()
      print ("Game Over!")
      print ("The battleship was at row " + str(ship_row+1) + " and column " + str(ship_col+1))
 
    turn+1
    
