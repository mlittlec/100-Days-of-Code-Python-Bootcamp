from art import logo
from art import vs
from game-data import data
import random

def format_data(account:
    '''Format the account data and returns the printable format'''
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
   return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    '''Take the user guess and follower counts and returns if they got it right.'''
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# Make the game repeatable.
while game_should_contine:
    # Generate a random account from the game data
    # Make the account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")


    # Ask the user for a guess.
    guess = input("Who has the more followers? Type 'A' or 'B': ").lower()
                

    # Check if the user is correct.
    ## Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    ## Use if statement to check if the user is correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the screen between iterations...
    clear()
    print(logo)

    # Give user feedback on their guess.
    if is_correct:
        # Score keeping
        score += 1
        print(f"You're right.  Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, you're wrong.  Your final score is: {score}")
