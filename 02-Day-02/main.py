two_digit_number = input("Type a two digit number: ")

print(type(two_digit_number))

# Get the first and second digits using subscripting then convert them to integers.
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

print(first_digit)
print(second_digit)

result = int(first_digit)+ int(second_digit)

print("The total is: " + str(result))