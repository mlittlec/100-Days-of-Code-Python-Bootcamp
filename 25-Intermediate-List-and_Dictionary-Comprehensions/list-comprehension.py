# List Comprehensions

name = "Angela"
leeters_list = [letter for letter in name]

print(letters_list)

range_list = [num * 2 for num in range(1,5)]

print(range_list)


# Conditional Lsit comprehensions

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor". "Feddie"]

short_names = [name for name in names if len(name) < 5]

print(short_names)


long_names = [name.upper() for name in names if len(name) > 5]

print(long_names)
