# Don't change the code below
row1 = ["X", "X", "X"]
row2 = ["X", "X", "X"]
row3 = ["X", "X", "X"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?")
# Don't change the code above

# Write your code below here
horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"

# Write your code above here
print(f"{row1}\n{row2}\n{row3}")
