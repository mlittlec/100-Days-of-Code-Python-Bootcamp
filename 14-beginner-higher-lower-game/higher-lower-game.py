from art import logo
from art import vs
from game-data import data
import random

def format_data(account:
    '''Format the account data into a printable format'''
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
   return f"{account_name}, a {account_descr}, from {account_country}"

# display art
print(logo)

# Generate a random account from the game data
account_a = random.choice(data)
account_b = random.choice(data)

if account_a == account_b:
    account_b = random.choice(data)
    
print(f"Compare A: {format_data(account_a)}")
print(vs)
print(f"Against B: {format_data(account_b)}")


# Ask the user for a guess.


# Check if the user is correct.
## Get follower count of each account
## Use if statement to check if the user is correct


# Give user feedback on their guess.


# Score keeping

# Make the game repeatable.


# Make the account at position B become the next account at position A.


# Clear the screen between iterations...
