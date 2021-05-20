"""A number-guessing game."""

from random import choice

# Put your code here
def get_user_name():
    """Greet player and return their name input."""
    return input("Howdy, what's your name? >")

def guessing_game(name):
    """Run game where user guesses a randomly generated number."""

    guess_number = choice(range(1,100))

    print(f"{name}, I'm thinking of a number between 1 and 100. \n Try to guess my number.")

    while True:
        input