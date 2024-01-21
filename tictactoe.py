#Tic-Tac-Toe

# Step 1

# board shows x has won
def evaluate(board):
    # Check if the player with crosses (Xs) has won
    if 'xxx' in board:
        return 'X'  # Player with crosses (Xs) has won
    else:
        return '-'  # Game is still ongoing or a draw

# Example usage:
board_example = "xx-ooxxxo"
result = evaluate(board_example)

if result == 'X':
    print("Player with crosses (Xs) has won!")
else:
    print("Game is still ongoing or it's a draw.")


# board shows O has won
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


# Function that shows Both x and o cannot win. They are in a draw
    
def evaluate(board):
    # Check if the board is full and nobody has won
    if '-' not in board and 'xxx' not in board and 'ooo' not in board:
        return "The board is full, but nobody has won."
    else:
        return "Game is still ongoing or someone has won."

# Example usage:
board_example = "xxooxxoxo"
result = evaluate(board_example)

print(result)


# Function that shows game is at Rest and not finished.

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


# Step 2

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


# Step 3

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


# Step 4

import random

def pc_move(board):
    valid_moves = [i for i in range(len(board)) if board[i] == '-']

    if valid_moves:
        position = random.choice(valid_moves)
        mark = 'o'  # Assuming computer plays with 'o'

        # Update the board with the computer's move
        new_board = list(board)
        new_board[position] = mark

        return ''.join(new_board)
    else:
        # No valid moves left, return the original board
        return board

# Example usage:
initial_board = "-------------------"
updated_board = pc_move(initial_board)

print("Updated Board (Computer's Move):", updated_board)


# Step 5

def evaluate(board):
    # Check if the player with crosses (Xs) has won
    if 'xxx' in board:
        return 'X'  # Player with crosses (Xs) has won
    # Check if the player with noughts (Os) has won
    elif 'ooo' in board:
        return 'O'  # Player with noughts (Os) has won
    # Check if the board is full and nobody has won
    elif '-' not in board:
        return 'D'  # Draw (nobody has won, and the board is full)
    else:
        return '-'  # Game is still ongoing

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

    mark = 'X'  # Assuming player plays with 'X'

    # Update the board with the player's move
    new_board = list(board)
    new_board[position] = mark

    return ''.join(new_board)

def pc_move(board):
    valid_moves = [i for i in range(len(board)) if board[i] == '-']

    if valid_moves:
        position = random.choice(valid_moves)
        mark = 'O'  # Assuming computer plays with 'O'

        # Update the board with the computer's move
        new_board = list(board)
        new_board[position] = mark

        return ''.join(new_board)
    else:
        # No valid moves left, return the original board
        return board

def display_board(board):
    print("Current Board:")
    print(board[:5])
    print(board[5:10])
    print(board[10:15])
    print(board[15:])

def play_game():
    board = "-------------------"
    winner = '-'

    while winner == '-':
        display_board(board)

        # Player's move
        board = player_move(board)
        winner = evaluate(board)
        if winner != '-':
            break

        display_board(board)

        # Computer's move
        board = pc_move(board)
        winner = evaluate(board)

    display_board(board)

    if winner == 'X':
        print("Congratulations! You win!")
    elif winner == 'O':
        print("Computer wins! Better luck next time.")
    else:
        print("It's a draw!")

# Example usage:
import random

play_game()



# Step 6

def computer_strategy(board):
    # Check for an immediate win opportunity
    for i in range(len(board)):
        if board[i] == '-':
            test_board = list(board)
            test_board[i] = 'O'
            if evaluate(''.join(test_board)) == 'O':
                return i

    # Check for a blocking move (prevent player from winning)
    for i in range(len(board)):
        if board[i] == '-':
            test_board = list(board)
            test_board[i] = 'X'
            if evaluate(''.join(test_board)) == 'X':
                return i

    # If no immediate win or block, make a strategic move
    # For simplicity, this example chooses a random valid move
    valid_moves = [i for i in range(len(board)) if board[i] == '-']
    if valid_moves:
        return random.choice(valid_moves)

    return -1  # No valid moves left

def improved_pc_move(board):
    position = computer_strategy(board)

    if position != -1:
        mark = 'O'  # Assuming computer plays with 'O'
        # Update the board with the computer's move
        new_board = list(board)
        new_board[position] = mark
        return ''.join(new_board)
    else:
        # No valid moves left, return the original board
        return board