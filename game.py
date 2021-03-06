"""A number-guessing game."""

from random import choice


def get_user_name():
    """Greet player and return their name input."""
    return input("Howdy, what's your name? > ")


def replay_game(name, best_score):
    """Prompts user to play again after completing a round of the game."""
    replay_prompt = input("Would you like to play again? (y/n) > ").lower()
    if replay_prompt == "y" or replay_prompt == "yes":
        guessing_game(name, best_score)

    else:
        print(f"Bye {name}!")


def guessing_game(name, best_score=None):
    """Run game where user guesses a randomly generated number."""

    guess_number = choice(range(1, 100))

    guess_counter = 0

    print(f"{name}, I'm thinking of a number between 1 and 100. \nTry to guess my number.")

    while True:
        player_guess = input("Your guess? > ")

        if player_guess.isnumeric() is False:
            print("Invalid guess. Please enter an integer from 1 to 100.")

        elif int(player_guess) < 1 or int(player_guess) >= 100:
            print("Please input an integer between 1 and 100.")

        else:
            player_guess = int(player_guess)
            guess_counter += 1

            if player_guess == guess_number:
                if best_score is None or guess_counter < best_score:
                    best_score = guess_counter
                print(f"Congrats {name}! You found my number in {guess_counter} tries! \n Best Score: {best_score}")
                break

            elif player_guess > guess_number:
                print("Your guess is too high, try again.")

            elif player_guess < guess_number:
                print("Your guess is too low, try again")

        if guess_counter >= 10:
            print("Maximum guesses reached!")
            break

    replay_game(name, best_score)


guessing_game(name=get_user_name())
