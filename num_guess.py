import random

lower_bound = 1
upper_bound = 1000
max_guess = 10

secret_number = random.randint(lower_bound, upper_bound)

def get_guess():
    while True:
        try:
            guess = int(input(f"Enter an integer between {lower_bound} and {upper_bound}: "))
            if lower_bound <= guess <= upper_bound:
                return guess
            else:
                print(f"Your guess must be between {lower_bound} and {upper_bound}")
        except ValueError:
            print("You must enter a valid integer")

def play_game():
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}")
    print(f"You have {max_guess} guesses to find it")
    for guess_count in range(1, max_guess + 1):
        guess = get_guess()
        if guess < secret_number:
            print("Higher...")
        elif guess > secret_number:
            print("Lower...")
        else:
            print(f"You guessed it in {guess_count} guesses")
            return
    print(f"Sorry, you've run out of guesses. The correct number was {secret_number}")

def play_game():
    attempt = 0
    won = False
    while attempt < max_guess:
        guess = get_guess()
        attempt += 1
        if guess < secret_number:
            print("Higher...")
        elif guess > secret_number:
            print("Lower...")
        else:
            won = True
            break
    else:
        print(f"Sorry, you've run out of guesses. The correct number was {secret_number}")

    if not won:
        print(f"Sorry you didn't guess the number. It was {secret_number}")
if __name__ == "__main__":
    print("Welcome to the number guessing game")
    play_game()