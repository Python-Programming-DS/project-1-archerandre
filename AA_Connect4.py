#Author: Andre Archer
#Project 1: Connect 4 Game
#Date: 09-25-2025

"""

This file contains functions and main function to play a game of Connect 4. 
By running this file, a new game will be started that alternates between players X and O
and offers the available positions to choose from. The game will end when a player wins or the board is full.

This file is able to:
- Print the game board
- Reset the game board
- Check available positions (and remove full columns from available positions)
- Validate user entry for column and row
- Update the game board with the player's move
- Check if the board is full
- Check if there is a win condition on the board

"""

def printBoard(board):
    """
    Prints the current state of the board with row and column labels.
    """

    for i in range(len(board)):
        print("| " + str(6 - i), end=" ")
        row = board[-1-i]
        for j in range(len(row)):
            print("| " + row[j], end=" ")
        print("|")
        print("---------------------------------")
    print("|R/C| a | b | c | d | e | f | g |")
    print()

def resetBoard():
    """
    Resets the board every time a new game is started
    """
    board = [[" " for _ in range(7)] for _ in range(6)] # creates a 6x7 blank board to start the game
    return board

def availablePositions(board):
    """
    Check available positions in the selected column
    In each column, the lowest available row is where the piece will go
    0 is the top row, 6 is the bottom row
    if the column is full, then do not return any positions for that column
    """
    positions = []
    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    rows = ['1', '2', '3', '4', '5', '6'] 
    for col_idx in range(7):
        for row_idx in range(6):
            if board[row_idx][col_idx] == " ":
                positions.append(f"{columns[col_idx]}{rows[row_idx]}") #append the available position in desired format to print
                break
    return positions

def validateEntry(entry, board):
    """
    Check valid entry format for column only
    """
    if entry in availablePositions(board):
        col, row = entry[0], entry[1]
        col_index = ord(col) - ord('a') #converts letter to number, a=0, b=1, c=2 based on format of board
        row_index = int(row)  # Convert to 0-indexed and invert for display
        return (row_index, col_index)
    else:
        print("\nInvalid entry: try again.")
        print("Column must be a-g and row must be 1-6. \n")
    return None

def updateBoard(board, col, player):
    """
    Update the board with the player's move in the lowest available row in the selected column.
    """
    for row in range(7):
        if board[row][col] == " ":
            board[row][col] = player
            return True
    return False

def checkFull(board):
    """
    Check if every space on the board is full, then end game if true. 
    If any space is empty, return False and continue the game.
    """

    for col in range(7):
        for row in range(6):
            if board[row][col] == " ":
                return False
    return True

def checkWin(board):
    """
    Need to check if there is a win during the game. This can be done in 4 ways:
        - Check every column
        - check every row
        - check diagonal (lower left to upper right)
        - check diagonal (upper left to lower right)
    If any row, column or diagonal has the same value (not empty " "), then the game is won.
    """
    for r in range(6):
        for c in range(4):
            if board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3] != " ": # check rows
                return True
    for c in range(7):
        for r in range(3):
            if board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c] != " ": # check columns
                return True
    for r in range(3):
        for c in range(4):
            if board[r][c] == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3] != " ": # check diagonal (lower left to upper right)
                return True
    for r in range(3, 6):
        for c in range(4):
            if board[r][c] == board[r-1][c+1] == board[r-2][c+2] == board[r-3][c+3] != " ": # check diagonal (upper left to lower right)
                return True
    return False

def checkEnd(board):
    """
    Check if the game has ended by either a win or a full board.
    If the game is won, print the winner message.
    If the game is a draw (full board), print the draw message.
    If the game is still ongoing, return None.
    """
    if checkWin(board): # must check win first, since last move can be a win
        print("Game Over: We have a winner!")
        return True
    elif checkFull(board): # check if the board is full
        print("Game Over: It's a draw!")
        return True
    else:
        print("Game is still ongoing.")
        return None

def playGame():
    """
    This function contains the loop and calls to play the Connect 4 game.
    This also alternates between players every turn and will print the winner.
    """

    print("New Game: X Goes First\n")
    board = resetBoard() # Reset the board to start the game
    printBoard(board) # Print the blank board
    game_over = False
    current_player = "X" # X always goes first

    while not game_over:
        print(f"{current_player}'s Turn.") # Say whos turn it is, this will change every turn
        print(f"Where do you want your {current_player} placed?")
        open_positions = availablePositions(board)
        print(f"Available positions: {open_positions} \n")
        entry = input("Please enter column-letter and row-number (e.g., a1): ")
        print("Thank you for your selection,")
        position = validateEntry(entry, board) # check if entry is of valid format and available

        if position: # if position is not None, then it is valid

            row, col = position
            print(f'You have entered column {entry[0]} \n\t\tand row #{row}.')
            if updateBoard(board, col, current_player): # update the board and check if the cell is taken, if None, then try again
                printBoard(board) # print board with new input

                if checkEnd(board): # check if the game is over by checking win or full
                    game_over = True
                    if checkWin(board):
                        print(f"Player {current_player} wins!")
                    else:
                        print("It's a draw!")
                current_player = "O" if current_player == "X" else "X" # this is how the turn switches players every turn

def main():
    new_game = 'y'
    while new_game.lower() == 'y':
        playGame()
        new_game = input("Another game (y/n): ")
    print("Thank you for playing!")

if __name__ == "__main__":
    main()


