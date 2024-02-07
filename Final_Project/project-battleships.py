#Step 1
# the custom function create_ships_grid takes a list of coordinate pairs as input and returns a 10x10 grid with ships placed at the specified coordinates. The grid is represented using 'O' for empty spaces and 'X' for spaces occupied by a ship. The function also handles invalid coordinates by printing a message and ignoring them.

def create_ships_grid(ship_coordinates):
    # Initialize a 10x10 grid with all empty spaces
    grid = [['O' for _ in range(10)] for _ in range(10)]

    # Place ships on the grid
    for coordinate in ship_coordinates:
        x, y = coordinate
        # Check if the coordinate is within the grid
        if 0 <= x < 10 and 0 <= y < 10:
            grid[x][y] = 'X'  # 'X' represents a ship at that coordinate
        else:
            print(f"Ignoring invalid coordinate: {coordinate}")

    return grid

# For instance:
ships_coordinates = [(1, 2), (3, 4), (7, 9)]
ships_grid = create_ships_grid(ships_coordinates)

# Print the grid
for row in ships_grid:
    print(" ".join(row))

# Step 2

# In the below code the select_ship_positions function prompts the user to enter the coordinates for each ship. It then checks for valid input (numeric values within the range of 0-9) and ensures that the position is not already taken. The function returns a list of the selected ship positions.After obtaining the user's ship positions, the code uses the create_ships_grid function to create and print the corresponding map.

def select_ship_positions(num_ships):
    ship_positions = []

    for i in range(num_ships):
        while True:
            try:
                x = int(input(f"Enter x-coordinate for Ship {i + 1} (0-9): "))
                y = int(input(f"Enter y-coordinate for Ship {i + 1} (0-9): "))

                # Check if the entered coordinates are within the valid range
                if 0 <= x < 10 and 0 <= y < 10:
                    # Check if the position is already taken
                    if (x, y) not in ship_positions:
                        ship_positions.append((x, y))
                        break
                    else:
                        print("Position already taken. Try again.")
                else:
                    print("Invalid coordinates. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    return ship_positions

# For instance:
num_ships = 3
user_ship_positions = select_ship_positions(num_ships)

# Create and print the grid using the create_ships_grid function
ships_grid = create_ships_grid(user_ship_positions)
for row in ships_grid:
    print(" ".join(row))

# Step 3
# In this case my custom randomly_place_computer_ships function generates random coordinates for each computer ship, checks if the position is not already taken, and appends the new position to the list of computer ship positions and it does not display the board to the player but returns the list of computer ship positions.

import random

def randomly_place_computer_ships(num_ships):
    computer_ship_positions = []

    for _ in range(num_ships):
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)

            # Check if the position is not already taken by another ship
            if (x, y) not in computer_ship_positions:
                computer_ship_positions.append((x, y))
                break

    return computer_ship_positions

# for instance:
num_computer_ships = 3
computer_ship_positions = randomly_place_computer_ships(num_computer_ships)

# Number 3 
# Below are two functions, one for the player and the other for the computer, that take input from the respective players and check if the opponent's ship was destroyed. If a ship is destroyed, it removes the corresponding coordinates from the list.
# These functions can be used in a game loop where players take turns until all the opponent's ships are destroyed. one just needs to make sure to update the opponent_ship_positions list accordingly based on whether the player or the computer is the opponent in a given turn.

import random

def player_turn(opponent_ship_positions):
    while True:
        try:
            x = int(input("Enter x-coordinate for your attack (0-9): "))
            y = int(input("Enter y-coordinate for your attack (0-9): "))

            # Check if the entered coordinates are within the valid range
            if 0 <= x < 10 and 0 <= y < 10:
                attack_position = (x, y)

                # Check if the attack hits an opponent's ship
                if attack_position in opponent_ship_positions:
                    print("You hit the opponent's ship!")
                    opponent_ship_positions.remove(attack_position)
                else:
                    print("You missed!")
                break
            else:
                print("Invalid coordinates. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def computer_turn(opponent_ship_positions):
    while True:
        x = random.randint(0, 9)
        y = random.randint(0, 9)

        attack_position = (x, y)

        # Check if the attack hits an opponent's ship
        if attack_position in opponent_ship_positions:
            print("Computer hit your ship!")
            opponent_ship_positions.remove(attack_position)
        else:
            print("Computer missed!")
        break

    # Number 4
    # Below is my implementation code of the main game loop that includes the setup of player and computer ships, and the turns where players guess the opponent's ship locations. The game continues until one of the players has no remaining ships.
    # Its a simple battleship game where the player places their ships, the computer places its ships randomly, and then the players take turns guessing the opponent's ship locations. The game ends when one of the players has no remaining ships. The player is informed of their success or failure, and the scores are displayed at the end.

    import random

def create_ships_grid(ship_coordinates):
    grid = [['O' for _ in range(10)] for _ in range(10)]

    for coordinate in ship_coordinates:
        x, y = coordinate
        if 0 <= x < 10 and 0 <= y < 10:
            grid[x][y] = 'X'
        else:
            print(f"Ignoring invalid coordinate: {coordinate}")

    return grid

def select_ship_positions(num_ships):
    ship_positions = []

    for i in range(num_ships):
        while True:
            try:
                x = int(input(f"Enter x-coordinate for Ship {i + 1} (0-9): "))
                y = int(input(f"Enter y-coordinate for Ship {i + 1} (0-9): "))

                if 0 <= x < 10 and 0 <= y < 10:
                    if (x, y) not in ship_positions:
                        ship_positions.append((x, y))
                        break
                    else:
                        print("Position already taken. Try again.")
                else:
                    print("Invalid coordinates. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    return ship_positions

def randomly_place_computer_ships(num_ships):
    computer_ship_positions = []

    for _ in range(num_ships):
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)

            if (x, y) not in computer_ship_positions:
                computer_ship_positions.append((x, y))
                break

    return computer_ship_positions

def player_turn(opponent_ship_positions):
    while True:
        try:
            x = int(input("Enter x-coordinate for your attack (0-9): "))
            y = int(input("Enter y-coordinate for your attack (0-9): "))

            if 0 <= x < 10 and 0 <= y < 10:
                attack_position = (x, y)

                if attack_position in opponent_ship_positions:
                    print("You hit the opponent's ship!")
                    opponent_ship_positions.remove(attack_position)
                else:
                    print("You missed!")
                break
            else:
                print("Invalid coordinates. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def computer_turn(opponent_ship_positions):
    while True:
        x = random.randint(0, 9)
        y = random.randint(0, 9)

        attack_position = (x, y)

        if attack_position in opponent_ship_positions:
            print("Computer hit your ship!")
            opponent_ship_positions.remove(attack_position)
        else:
            print("Computer missed!")
        break

def main():
    num_player_ships = 3
    num_computer_ships = 3

    print("Player, place your ships:")
    player_ship_positions = select_ship_positions(num_player_ships)

    print("\nComputer is placing its ships...")
    computer_ship_positions = randomly_place_computer_ships(num_computer_ships)

    player_grid = create_ships_grid(player_ship_positions)
    computer_grid = create_ships_grid([])  # Empty grid for the computer's ships (hidden from the player)

    player_score = 0
    computer_score = 0

    while player_ship_positions and computer_ship_positions:
        print("\nPlayer's turn:")
        player_turn(computer_ship_positions)
        player_score += 1

        if not computer_ship_positions:
            break

        print("\nComputer's turn:")
        computer_turn(player_ship_positions)
        computer_score += 1

    print("\nGame over!")

    if not player_ship_positions:
        print("Congratulations! You sank all the computer's ships.")
        print(f"Your score: {player_score}")
    else:
        print("Sorry! The computer sank all your ships.")
        print(f"Computer's score: {computer_score}")

if __name__ == "__main__":
    main()