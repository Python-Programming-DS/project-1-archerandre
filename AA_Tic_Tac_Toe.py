#Author: Andre Archer
#Project 1: Tic Tac Toe Game
#Date: 09-25-2025

"""

This file contains functions and main function to play a game of Tic-Tac-Toe. 
By running this file, a new game will be started that alternates between players X and O
and allows them to choose their position on the grid. The game will end when a player wins or the board is full.

This file is able to:
- Print the game board
- Reset the game board
- Validate user entry for column and row
- Update the game board with the player's move
- Check if the board is full
- Check if there is a win condition on the board
- Allow the user to play again if desired

"""

def printBoard(board):
    # Print the board as shown in the document/example
    print("-----------------")
    print("|R/C| 0 | 1 | 2 |")
    print("-----------------")
    # Print each row of the board with its new inputs
    for i in range(3):
        print(f"| {i} |", end="")
        for j in range(3):
            print(f" {board[i][j]} |", end="")
        print("\n-----------------")

def resetBoard():
    """
    Resets the board every time a new game is started
    """
    board = [[" " for _ in range(3)] for _ in range(3)] # creates a 3x3 blank board to start the game
    return board

def validateFormat(entry):
    """
    Check valid entry format for row and column
    If valid, the entry will be of lngth 3, in the format #,#
    """
    if len(entry) == 3 and entry[1] == ',' and entry[0].isdigit() and entry[2].isdigit():
        return True
    else:
        print("Invalid format: try again.")
        print("Entry must be in the format row,column (e.g., 0,1).")
        return False

def validateEntry(entry):
    """
    Check valid entry format for row and column
    """
    validFlag = validateFormat(entry) #need to check if the format is valid
    if not validFlag:
        return None
    
    row, col = map(int, entry.split(",")) #get the row and columns as integers from entry
    if 0 <= row < 3 and 0 <= col < 3: # make sure the entry values are within range
        return (row, col)
    else:
        print("Invalid entry: try again.") # print statement to let user know invalid entry
        print("Row & column numbers must be either 0, 1, or 2.")
    return None

def updateBoard(board, row, col, player):
    """
    Update the board with the player's move. 
    If the cell requested is full, then return False and try again
    """
    #check if the cell is empty
    if board[row][col] == " ":
        board[row][col] = player
        return True
    else:
        print("That cell is already taken. \n Please make another selection.")
        return False

def checkFull(board):
    """
    Checking if every cell in the board is taken. Then the game will be over
    """
    for row in board:
        if " " in row:
            return False
    return True

def checkWin(board):
    """
    Check if there is a win condition on the board. 
    This is done in 3 ways: checking rows, columns, and diagonals.
    If any row, column or diagonal has the same value (not empty " "), then the game is won.
    """
    # Check the rows and columns of the board
    for i in range(3):
        # Check if rows are the same, but not empty
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        # Check if columns are the same, but not empty
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True 
    # Check the diagonals of the board
    if board[0][0] == board[1][1] == board[2][2] != " ": # Bottom left to top right
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ": # Top left to bottom right
        return True
    return False

def checkEnd(board):
    """
    Check if either of the two end conditions are met:
    1. The game is won
    2. The game board is full, but no winner
    """
    # If the game is won, the game will end
    # Checking the win condition must be first, since a win can occur on the last move
    if checkWin(board):
        return True
    # If the game is full, the game will also end
    if checkFull(board):
        return True
    # If neither full or won, then the game continues
    return False

def playGame():
    """
    This function contains the loop and calls to play the tic tac toe game. 
    """

    print("New Game: X Goes First\n")
    board = resetBoard()        # Reset the board to start the game
    printBoard(board)           # Print the blank board
    game_over = False
    current_player = "X"        # X always goes first
    while not game_over:
        print(f"{current_player}'s Turn.")      # Say whos turn it is, this will change every turn
        print(f"Where do you want your {current_player} placed?")
        entry = input("Please enter row and column number separated by a comma: ")
        position = validateEntry(entry)         # check if entry is of valid format
        if position:                            # if position is not None, then it is valid
            row, col = position
            print(f'You have entered row #{row} \n\t\tand column #{col}.')
            if updateBoard(board, row, col, current_player): # update the board and check if the cell is taken
                printBoard(board)     # print board with new input
                if checkEnd(board):   # check if the game is over by checking win or full
                    game_over = True
                    if checkWin(board):
                        print(f"Player {current_player} wins!")
                    else:
                        print("It's a draw!")
                current_player = "O" if current_player == "X" else "X"  # change players every turn

def main():
    new_game = 'y'
    while new_game.lower() == 'y':
        playGame()  # play the game, this is a more compact way to have this in main than the whole function
        new_game = input("Another game? Enter Y or y for yes. ")

if __name__ == "__main__":
    main()