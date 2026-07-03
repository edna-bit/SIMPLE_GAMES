import random
items = ["Rock", "Paper", "Scissors"]


def pick_tool():  # makes sure the player picks a valid tool
    while True:
        player_choice = input("Enter Rock, Paper, or Scissors: ").strip().capitalize()
        if player_choice in items:
            return player_choice
        print("Invalid input. Please enter Rock, Paper, or Scissors.")


def get_rounds():  # asks the player how many rounds they want to play and makes sure it is a positive whole number
    while True:
        try: #tries to convert the input into an integer and if it is a positive whole number, returns the number of rounds
            rounds = int(input("How many rounds do you want to play? ").strip())
            if rounds > 0:
                return rounds
        except ValueError: #excepts the error if the player does not enter a positive whole number and asks them to enter a positive whole number
            pass # moves on to the next line of code if the input is not a positive whole number
        print("Please enter a positive whole number.")


def choose(player_choice): # determines the outcome of a single round
    computer_choice = random.choice(items)

    if player_choice == computer_choice:
        print("It's a tie! Both chose", player_choice)
        return "tie"
    elif (player_choice == "Rock" and computer_choice == "Scissors"):
        print("You win! Rock beats Scissors")
        return "player"
    elif (player_choice == "Paper" and computer_choice == "Rock"):
        print("You win! Paper beats Rock")
        return "player"
    elif (player_choice == "Scissors" and computer_choice == "Paper"):
        print("You win! Scissors beats Paper")
        return "player"
    else:
        print("You lose!", computer_choice + " beats " + player_choice)
        return "computer"


def play(): # starts the game and loops through the number of rounds the player wants to play
    rounds = get_rounds()
    player_wins = 0
    computer_wins = 0
    ties = 0

    for round_num in range(1, rounds + 1): # loops through the number of rounds the player wants to play and prints the round number
        print(f"\nRound {round_num}")
        player_choice = pick_tool()
        result = choose(player_choice)

        # keeps track of the number of wins for the player, computer, and ties
        if result == "player":
            player_wins += 1
        elif result == "computer":
            computer_wins += 1
        else:
            ties += 1

    print("\nGame over!")
    print(f"Player wins: {player_wins}") # prints the number of rounds the player won
    print(f"Computer wins: {computer_wins}") # prints the number of rounds the computer won
    print(f"Ties: {ties}") # prints the number of rounds that ended in a tie

    if player_wins > computer_wins:# compares the number of wins for the player and computer and prints the overall winner
        print("You win the game!")
    elif player_wins < computer_wins:
        print("Computer wins the game!")
    else:
        print("It's a tie overall!")


play()