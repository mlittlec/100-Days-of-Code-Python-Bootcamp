# Use this website to generate the word fonts used for the entry screen:
# http://patorjk.com/software/taag

# Choose a random number between 1 and 100
from random inport randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer):
    if guess > answer:
        print("Too high")
    elif guess < answer:
        print("Too low")
    else:
        print(f"You got it - the answer was {answer}")

# Make a function to set the difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return = EASY_LEVEL_TURNS
    else:
        return = HARD_LEVEL_TURNS

answer = randint(1, 100)

print(Welcome to the Guessing Game2)
print("I'm thinking of a number between 1 and 100 - can you tell me what it is?")


# Let the user guess a number

guess = int(input("Make a guess"))
turns = set_difficulty()
print(f"You have {turns} remaining to guess the number.")


# Function to check user's guess actual actual answer




# Track the number of turns and reduce by 1 if they get it wrong


# Repeat the guessing section until total number of guesses used

