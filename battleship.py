from random import randint

size = 6
turns = 8

board = [["O" for _ in range(size)] for _ in range(size)]
# print(board)

# display board
for rows in board:
    print(" ".join(rows))
    
row_position = randint(0, len(board) - 1)
col_position = randint(0, len(board[0]) - 1)
print(row_position, col_position)

for turn in range(turns + 1):
    
    print("Turn: {}".format(turn))
    row_guessed = int(input("Guess a row: "))
    col_guessed = int(input("Guess a col: "))
    
    if row_guessed == row_position and col_guessed == col_position:
        print("Congrats you have sunk my battleship")
        break
    
    # if not found, proceed with the following
    else:
      # size -1 if not you will hit out of bounds error
        if (row_guessed < 0 or row_guessed > size - 1) or (col_guessed < 0 or col_guessed > size -1):
            print("Positions invalid")
        
        elif board[row_guessed][col_guessed] == 'X':
            print("You have already guessed this position")
        
        else:
            board[row_guessed][col_guessed] = 'X'
        
    
    if turn == 8:
        print("Game over, better luck next time!")
    
