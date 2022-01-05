import random
# Step 1

word_list = ["aardvark", "baboon", "camel"]



# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word
chosen_word = random.choice(word_list)

# Testing code:
print(f'Psst, the solution is {chosen_word}')

display = []

word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

guess = input("Guess a letter: ").lower()

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess.   Make guess lowercase.
for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter


# TODO-3 Check if the letter the user guessed (guess) is one of the letter in the chosen_word.
print(display)
