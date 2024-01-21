# evaluate function - create at least 5 different tests for the behavior of the 

import tictactoe

# test that shows player x has won
def test_evaluate_board():
    def evaluate(board):
     # Example usage:
        board_example = "xx-ooxxxo"
        result = evaluate(board_example)
        
        if result == 'X':
            print("Player with crosses (Xs) has won!")
        else:
            print("Game is still ongoing or it's a draw.")


# Test that shows player o has won
def test_evaluate_board():
     def evaluate(board):
    # Check if the player with noughts (Os) has won
        if 'ooo' in board:
            return 'O'  # Player with noughts (Os) has won
        else:
            return '-'  # Game is still ongoing or a draw

# Example usage:
board_example = "xx-oxxooo"
result = evaluate(board_example)

if result == 'O':
    print("Player with noughts (Os) has won!")
else:
    print("Game is still ongoing or it's a draw.")


# Test that shows board is full and no one has won
def test_evaluate_board():
     def evaluate(board):
    # Check if the board is full and nobody has won
        if '-' not in board and 'xxx' not in board and 'ooo' not in board:
            return 'D'  # Draw (nobody has won, and the board is full)
        else:
            return '-'  # Game is still ongoing or someone has won

# Example usage:
board_example = "xxooxxoxo"
result = evaluate(board_example)

if result == 'D':
    print("The game is a draw!")
else:
    print("Game is still ongoing or someone has won.")


# Test that shows Rest
def test_evaluate_board():
    def evaluate(board):
    # Check if the game is not finished
        if '-' in board or 'xxx' in board or 'ooo' in board:
            return "Rest"  # Game is not finished
        else:
            return "The game is finished."

# Example usage:
board_example = "xxooxxox-"
result = evaluate(board_example)

print(result)


# Another test type
import pytest

import tictactoe

def test_evaluate_failure():
    with pytest.raises(ValueError):
        tictactoe.board_evaluate('XO!-')


# move function - create at least 2 different tests
        
import tictactoe

def test_move_to_position_mark():
    def move(board, position, mark):
    # Check if the position is valid
        if 0 <= position < len(board) and board[position] == '-':
        # Valid move, update the board
            new_board = list(board)
        new_board[position] = mark
        return ''.join(new_board)
    else:
# Invalid move, return the original board
return board

# Example usage:
initial_board = "-------------------"
new_board = move(initial_board, 5, 'x')

print("Initial Board:", initial_board)
print("New Board:", new_board)


def test_move_to_position_mark():
    def player_move(board):
        valid_move = False
    while not valid_move:
        try:
            position = int(input("Enter the position (0-19) where you want to play: "))
            if 0 <= position < len(board) and board[position] == '-':
                valid_move = True
            else:
                print("Invalid move. Please choose an unoccupied position within the valid range.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    mark = input("Enter 'x' or 'o' for your move: ")

    # Update the board with the player's move
    new_board = list(board)
    new_board[position] = mark

    return ''.join(new_board)

# Example usage:
initial_board = "-------------------"
updated_board = player_move(initial_board)

print("Updated Board:", updated_board)


# Another move test
import pytest

import tictactoe

def test_move_failure():
    with pytest.raises(ValueError):
        tictactoe.computer_move('0-19')

# a module is like a box that contains codes that are ready to use or in other words ready-made codes
# a package is a module that has sub-modules in it

# what are side effects? A side effect is when the module is doing something, or writing something into the file or asks the user to do something. a module should give us a function to use in our code and not to do it instead.
from math import sqrt # if this prints the square root instead then I would say it has a side effect

# What are exceptions? In other words i could say exceptions are errors e.g. when you try to open a file that doesnt exist python throws up an error like: ( FileNotFoundError )
# to resolve errors raised by third party codes, you can use try/except block. 

# Using which keywords can you create, throw and catch your new custom Exception? try, else, finally

# Give examples of some benefits of testing? it gives us proof that the code works properly and is without errors.