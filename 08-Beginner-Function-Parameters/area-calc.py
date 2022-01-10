# Write your code below this line
import math


def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You'll needs {num_of_cans} of paint.")


# Write your code above line

# Don't change the code below here:
test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
