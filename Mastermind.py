# A game based on Mastermind.
# ABOUT MASTERMIND
# Mastermind will get you thinking while you try to crack a four colored code set by your partner in only 10 moves or fewer. 
# Cryptic clues are given to help you know which color in which position.
# Mastermind is only a two player game. Each game is different and with over 2,000 possible code combinations
# HOW TO WIN
# Solve your opponent's code in fewer turns than it takes your opponent to solve your code.

"""
To-Do:
    - Add additional colors to the game (Aim for 8 colors).
    - Add 1 vs. Computer mode.
    - Add Computer vs. Computer simulation mode.
    BONUS
        - Add a bulk simulation mode (10,000 games) to train a ML algorithm.
"""

import random
import sys
# May not need os and time. Importing os and time for now just in case.
import os
import time

def choose_players():
    # Choose 2 players or 1 player.
    print("Would you like to play against another player or against the computer?")
    print("1. Player vs. Player")
    print("2. Player vs. Computer")
    print("3. Computer vs. Computer")
    print("4. Exit Game")
    print("")
    choice = input("Enter your choice: ")
    if choice == "1":
        return 1
    elif choice == "2":
        return 2
    elif choice == "3":
        return 3
    else:
        return -1

def initialize():
    # Initialize the game.
    print("Welcome to Mastermind!")
    print("The game is simple: You have 10 turns to guess the code.")
    print("The code is four colored. Red, blue, green, and yellow.")
    print("The colors are represented by the following letters: R, B, G, and Y.")
    print("The code is randomly generated. You have to guess the code in 10 or less turns.")
    print("The clues are given to help you know which color in which position.")
    print("The game is only a two player game. Each game is different and with over 2,000 possible code combinations.")
    print("How to win: Solve your opponent's code in fewer turns than it takes your opponent to solve your code.")
    print("")
    print("Press enter to continue...")
    input()
    print("")


def expand_code(code):
    # Expands the code to include the color R, B, G, and Y.
    expanded_code = []
    for i in range(len(code)):
        if code[i] == "🔴":
            expanded_code.append("🔴 Red")
        elif code[i] == "🔵":
            expanded_code.append("🔵 Blue")
        elif code[i] == "🟢":
            expanded_code.append("🟢 Green")
        elif code[i] == "🟡":
            expanded_code.append("🟡 Yellow")
    return expanded_code

# Player selects a code of length 5 and returns it.
def generate_code(player):
    code = []
    while len(code) < 5:
        # Player chooses a color.
        print("")
        print(player + ": Choose a color.")
        print("1. Red")
        print("2. Blue")
        print("3. Green")
        print("4. Yellow")
        print("")
        choice = input("Enter your #" + str(len(code) + 1) + " choice: ")
        if choice == "1":
            code.append("🔴")
        elif choice == "2":
            code.append("🔵")
        elif choice == "3":
            code.append("🟢")
        elif choice == "4":
            code.append("🟡")
        else:
            print("")
            print("Invalid choice.")
            print("")
    # Show mastermind what they have chosen before continuing.
    print("")
    print(player + ", you have chosen the following code:")
    # Print expanded code in a more readable format.
    expanded_code = expand_code(code)
    for i in range(len(expanded_code)):
        print(str(i + 1) + ": " + expanded_code[i], end="   ")
    print("")
    print("Press enter to clear and continue...")
    input()
    print("\n" * 16)

    return code



def generate_random_code():
    # Generates a random code.
    code = []
    for i in range(5):
        code.append(random.choice(["🔴", "🔵", "🟢", "🟡"]))
    print("")
    return code


# Choose mode.
def mode_choose():
    choice = choose_players()
    if choice == 1:
        print("")
        print("You have chosen to play against another player.")
        print("")
        print("Press enter to continue...")
        input()
        # Ask for both player names
        print("")
        print("Enter player 1's name: ")
        player1 = input()
        if player1 == "":
            player1 = "Player 1"
        print("Enter player 2's name: ")
        player2 = input()
        if player2 == "":
            player2 = "Player 2"
        print("")
        print("Press enter to continue...")
        input()
        print("")
        print("Good luck " + player1 + " and " + player2 + "!")
        print("The game begins.")
        print("")
        two_player_game(player1, player2)
    if choice == 2:
        print("")
        print("You have chosen to play against the computer.")
        print("")
        print("Press enter to continue...")
        input()
        # Ask for player name
        print("")
        print("Enter player 1's name: ")
        player1 = input()
        if player1 == "":
            player1 = "Player 1"
        print("")
        print("Press enter to continue...")
        input()
        print("")
        print("The game begins.")
        print("")
    if choice == 3:
        print("")
        print("You have chosen to let the computer try and beat the computer. Weird.")
        print("")
        print("Press enter to continue...")
        input()
        print("")
        print("The game begins.")
        print("")
    if choice == -1:
        # Exit the game.
        print("")
        print("You have chosen to exit the game.")
        print("")
        print("Goodbye!")
        print("")
        terminate()

def two_player_game(player1, player2):
    # initialize variables
    turn = 1 # turn counter, starts at 1
    player1_turn = False # True if player 1 is the guesser, false if player 2's turn to guess.
    player1_code = [] # Holds the code GENERATED BY PLAYER 1
    player2_code = [] # Holds the code GENERATED BY PLAYER 2
    player1_clues = [] # Holds the clues GIVEN TO PLAYER 1.
    player2_clues = [] # Holds the clues GIVEN TO PLAYER 2.
    player1_guess = [] # Holds the guesses of player 1.
    player2_guess = [] # Holds the guesses of player 2.
    player1_score = -1 # Will be used to track who solved the code faster by comparing to player2_score
    player2_score = -1 # Will be used to track who solved the code faster by comparing to player1_score


    # Mastermind generates a code.
    # For now, player 1 is always mastermind first.
    if player1_turn == False:
        print(player1 + " will generate a code first.")
        player1_code = generate_code(player1)
    else:
        print(player2 + " will generate a code first.")
        player2_code = generate_code(player2)
    
    print("The code has been selected by the Mastermind.")
    print("")
    print(player2 + ": Press enter to continue...")
    input()
    print("")
    # The game begins.
    while (turn <= 10 and (player1_score == -1 or player2_score == -1)):
        if player1_turn == True: # If player 1 is the guesser.
            """
            Turn flow
            1. Guessing Player generates a guess.
            2. Game checks if the guess is correct.
                > If the guess is correct, the Guessing Player recieves score based on turn variable.
                > If the guess is incorrect, the Mastermind gives the guessing player a clue.
            3. Repeat step 1 and 2 until the guess is correct or the turn counter reaches 10.
            """
            # Allow player 1 to guess code.
            player1_guess = guess_code(player1, player1_clues, player1_turn, player1_guess)
            print(player1 + " guessed " + str(expand_code(player1_guess)))
            # Check if player 1 has guessed correctly
            # This should be moved to a function.
            if player1_guess == player2_code:
                print("")
                print("#" * 64)
                print((" " * 10) + player1 + " has guessed correctly!")
                print("#" * 64)
                print("")
                print(player2 + ": Press enter to continue...")
                input()
                print("")
                print(player1 + " has guessed correctly in " + str(turn) + " turns!")
                print("")
                player1_score = turn
                if player2_score == -1:
                    print(player2 + " must guess the code in " + str(turn) + " turns or less!")
                    turn = 0
                    # Player 1 becomes Mastermind.
                    print("")
                    print(player1 + " is the Mastermind!")
                    print("")
                    print(player1 + " needs to set the code.")
                    print("")
                    print(player1 + ": Press enter to continue...")
                    input()
                    print("")
                    player1_code = generate_code(player1)
                    player1_turn = False
                else:
                    determine_winner(player1, player2, player1_score, player2_score)
                print("")
            else: # Player 1 did not guess correctly.
                print("")
                print("#" * 64)
                print((" " * 10) + player2 + " has guessed incorrectly!")
                print("#" * 64)
                print("")
                print(player1 + ": Press enter to give a clue...")
                input()
                print("")
                player1_clues = give_clue(player1_guess, player2_code)
                print(player2 + " gave " + player1 + " the following clues: " + str(player1_clues))
                print("")
                print(player1 + ": Press enter to continue...")
                input()
                print("")

                
        else: # If player 2 is the guesser...
            # Allow player 2 to guess code.
            """
            Turn flow
            1. Guessing Player generates a guess.
            2. Game checks if the guess is correct.
                > If the guess is correct, the Guessing Player recieves score based on turn variable.
                > If the guess is incorrect, the Mastermind gives the guessing player a clue.
            3. Repeat step 1 and 2 until the guess is correct or the turn counter reaches 10.
            """
            player2_guess = guess_code(player2, player2_clues, player1_turn, player2_guess)
            # print that player 2 has guessed player2_guess in a string format.
            print(player2 + " guessed")
            expanded_code = expand_code(player2_guess)
            for i in range(len(expanded_code)):
                print(str(i + 1) + ": " + expanded_code[i], end="   ")
            # Check if player 2 has guessed correctly
            if player2_guess == player1_code:
                print("")
                print("#" * 64)
                print((" " * 10) + player2 + " has guessed correctly!")
                print("#" * 64)
                print("")
                print(player1 + ": Press enter to continue...")
                input()
                print("")
                print(player2 + " has guessed correctly in " + str(turn) + " turns!")
                print("")
                player2_score = turn
                if player1_score == -1:
                    print(player1 + " must guess the code in " + str(turn) + " turns or less!")
                    turn = 0
                    # Player 2 becomes Mastermind.
                    print("")
                    print(player2 + " is the Mastermind!")
                    print("")
                    print(player2 + " needs to set the code.")
                    print("")
                    print(player2 + ": Press enter to continue...")
                    input()
                    print("")
                    player2_code = generate_code(player2)
                    player1_turn = True
                else:
                    determine_winner(player1, player2, player1_score, player2_score)
            else: # If the guess was incorrect...
                print("")
                print("#" * 64)
                print((" " * 10) + player2 + " has guessed incorrectly!")
                print("#" * 64)
                print("")
                print(player1 + ": Press enter to give a clue...")
                input()
                print("")
                # Give player 2 clues.
                player2_clues = give_clue(player2_guess, player1_code)
                print(player1 + " gave " + player2 + " the following clues: " + str((player2_clues)))
                print("")
                print(player2 + ": Press enter to continue...")
                input()
                print("")
        turn += 1 # Increment turn counter.
        turn = check_out_of_turns(turn, player1_turn, player1, player2)

        # switches who the mastermind is if neccessary. 
        if (turn > 10 and (player1_score == -1 and player2_score == -1)):
            turn = 1
            if (player1_turn == False):
                player2_score = 11 # Set score to 11 to indicate that the player had not guessed correctly.
                # Player 2 becomes Mastermind.
                print(player2 + " is the Mastermind!")
                print(player2 + " needs to set the code.")
                print("")
                print(player2 + ": Press enter to continue...")
                input()
                print("")
                player2_code = generate_code(player1)
            elif (player1_turn == True):
                player1_score = 11 # Set score to 11 to indicate that the player had not guessed correctly.
                # Player 1 becomes Mastermind.
                print(player1 + " is the Mastermind!")
                print(player1 + " needs to set the code.")
                print("")
                print(player1 + ": Press enter to continue...")
                input()
                print("")
                player1_code = generate_code(player2)
            else:
                print("Something went wrong! Error code: Granny Smith Apples")
                terminate()
        elif (turn > 10):
            if (player1_turn == False):
                player1_score = 11
            elif(player1_turn == True):
                player2_score = 11
            determine_winner(player1, player2, player1_score, player2_score)

        print("")
        print("Turn: " + str(turn))
        print("")
        if player1_turn == False and turn != 0:
            player2_guess = display_and_clear_guesses(player2_guess)
            player2_clues = displayer_and_clear_clues(player2_clues)
        elif player1_turn == True and turn != 1:
            player1_guess = display_and_clear_guesses(player1_guess)
            player1_clues = displayer_and_clear_clues(player1_clues)
    determine_winner(player1, player2, player1_score, player2_score)

def check_out_of_turns(turn, player1_turn, player1, player2):
    if turn > 10:
        if player1_turn == False:
            print("")
            print("❗️ " + player1 + " You are out of turns!")
            print("")
            return 11 # Return 11 to indicate that the player did not guess in time.
        elif player1_turn == True:
            print("")
            print("❗️ " + player2 + " You are out of turns!")
            print("")
            return 11 # Return 11 to indicate that the player did not guess in time.
    else:
        return turn

def display_and_clear_guesses(guess):
    """
    This function displays guesses before clearing.
    """
    print("Your last guess:", end=" ")
    for i in range(len(guess)):
        print(guess[i], end="   ")
    print("")
    # reset guess to empty list.
    guess = []
    return guess

def displayer_and_clear_clues(clues):
    """
    This function displays clues before clearing.
    """
    print("Your last clue:", end=" ")
    for i in range(len(clues)):
        print(str(i + 1) + ": " + clues[i], end="   ")
    print("")
    # reset clues to empty list.
    clues = []
    return clues

def give_clue(guess, code):
    """
    Takes in a guess and a code to return a list of clues.
    """
    clues = []
    for i in range(len(guess)):
        if guess[i] == code[i]:
            clues.append("⚫️ Black")
        else:
            if guess[i] in code:
                clues.append("⚪️ White")
    return clues

def determine_winner(player1, player2, player1_score, player2_score):
    if player1_score < player2_score:
        print("")
        print(player1 + " took " + str(player1_score) + " turns to solve the code.")
        print(player2 + " took " + str(player2_score) + " turns to solve the code.")
        print("")
        print(player1 + " wins!")
        print("Press enter to end the game...")
        input()
        terminate()
    elif player1_score > player2_score:
        print("")
        print(player1 + " took " + str(player1_score) + " turns to solve the code.")
        print(player2 + " took " + str(player2_score) + " turns to solve the code.")
        print("")
        print(player2 + " wins!")
        print("Press enter to end the game...")
        input()
        terminate()
    else:
        print("")
        print(player1 + " took " + str(player1_score) + " turns to solve the code.")
        print(player2 + " took " + str(player2_score) + " turns to solve the code.")
        print("")
        print("It's a tie! You are both winners! Or losers, depending on your perspective.")
        print("Press enter to end the game...")
        input()
        terminate()



    
def guess_code(player, player_clues, player_turn, player_guess):
    # Show clues if there are any.
    if len(player_clues) > 0:
        print("")
        print(player + ": Here are the clues you have given so far:")
        print("")
        for clue in player_clues:
            print(clue)
        print("")
    # Player guesses the code.
    guess = []
    print(player + ": Enter your guess.")
    print("")
    # Ask for 5 guesses.
    for i in range(5):
        print("1. Red")
        print("2. Blue")
        print("3. Green")
        print("4. Yellow")
        print("")
        choice = input("Enter your #" + str(i + 1) + " choice: ")
        if choice == "1":
            guess = "🔴"
        elif choice == "2":
            guess = "🔵"
        elif choice == "3":
            guess = "🟢"
        elif choice == "4":
            guess = "🟡"
        else:
            print("")
            print("Invalid choice.")
            print("A random color will be chosen for you.")
            print("")
            guess = random.choice(["🔴", "🔵", "🟢", "🟡"])
        if player_turn == True:
            player_guess.append(guess)
        else:
            player_guess.append(guess)
    return player_guess







def terminate():
    # When the game is exited.
    print("#" * 64)
    print("Game terminated.")
    print("Created by: Jason Hertzog")
    print("#" * 64)
    sys.exit()


# Main
initialize()
mode_choose()


# This terminate function is called when the game is exited.
terminate()







