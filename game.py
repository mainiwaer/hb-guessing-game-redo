"""A number-guessing game."""

from random import choice

# Put your code here
def get_user_name():
    """Greet player and return their name input."""
    return input("Howdy, what's your name? > ")

def guessing_game(name):
    """Run game where user guesses a randomly generated number."""

    guess_number = choice(range(1,100))

    guess_counter = 0

    print(f"{name}, I'm thinking of a number between 1 and 100. \n Try to guess my number.")

    while True:
        player_guess = int(input("Your guess? > "))
        guess_counter += 1

        if player_guess == guess_number:
            print(f"Congrats {name}! You found my number in {guess_counter} tries!")
            break

        elif player_guess > guess_number:
            print("Your guess is too high, try again.")
        
        elif player_guess < guess_number:
            print("Your guess is too low, try again")

