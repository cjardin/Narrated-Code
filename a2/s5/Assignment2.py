# Author: William Cerros
# Class: CS 351 Tuesday Thursday 2:30pm
# Program Description: Program simulates a maze for the user to complete. The Kanren library is used
# to define parent child relationships which serve as a path in the maze
from kanren import var, facts, Relation, run

# Declaring a relation, maze_path
maze_path = Relation()

# Defining a path on a maze
# Relation object from Kanren library is used to define different paths
# Maze starts at 1, and the finish line is 9
# Path to finish is 1->2->5->6->9
facts(maze_path, (1, 2), (1, 3),
                 (2, 8), (2, 5),
                 (3, 1), (3, 4),
                 (5, 6), (5, 1),
                 (1, 4), (3, 7),
                 (7, 4), (4, 8),
                 (2, 7), (5, 7),
                 (6, 9), (8, 1))


# Function will work its way back from the finish (9) to the start (1) by using the run function
# Run function recursively finds the parent of current_position until we reach base case
# Once base case is reached, we reverse our string since we traveled from finish to start
# String is then printed to user
def finish_maze(current_position, path):
    x = var()
    if current_position == 1:
        path = path[::-1]
        print(path)
    else:
        current_position = run(1, x, maze_path(x, current_position))[0]
        path += ">-%d" % current_position
        finish_maze(current_position, path)


# Function displays start menu for user
def start_menu():
    print("*** Welcome to the Maze ***")
    print("Minimum number of steps to complete maze: 4")
    print("Good luck!\n")


# Function takes in current position as parameter
# Function then prints to user a tuple of possible choices
# If statement checks for an invalid entry from user
# Inside the if statement is a while loop that will execute until the user enters a valid choice
# Function returns the updated current_position after user choice
def valid_answer(current_position):
    x = var()
    possible_choices = run(10, x, maze_path(current_position, x))
    print(possible_choices)
    choice = eval(input("Please make a selection: "))

    if choice not in possible_choices:
        while True:
            print("Invalid choice, please try again.")
            print(possible_choices)
            choice = eval(input("Please make a selection: "))

            if choice in possible_choices:
                return choice

    return choice


# Start_game function will simulate the maze game to user
# A while loop will execute until current_position equals 9, which is the finish
# Once 9 is reached the user will have their score (number of choices) printed
# If user achieves a new high score (fewest amount of choices) the user will be notified
# User has the option to play again or end the game
# Once the user has played 3 games, and has not reached the high score of 4, user is offered the solution to the game
def start_game(high_score, num_of_games):
    start_menu()
    if num_of_games > 2 and high_score > 4:
        choice = input("Would you like the solution to the maze? (Y/N): ")
        if choice.lower() == "y":
            finish_maze(9, "9")
            print("\n")
    score = 0
    x = var()
    current_position = 1
    while current_position != 9:
        current_position = valid_answer(current_position)
        score = score + 1
    if score < high_score:
        high_score = score
        print("New High Score: %d" % high_score)

    num_of_games = 1 + num_of_games
    print("Score: %d" % score)
    print("Number of games played: %d" % num_of_games)
    answer = input("Would you like to play again? (Y/N) ")
    if answer.lower() == 'y':
        print("\n")
        start_game(high_score, num_of_games)
    else:
        print("Game Over")


# Starting game
start_game(100, 0)









