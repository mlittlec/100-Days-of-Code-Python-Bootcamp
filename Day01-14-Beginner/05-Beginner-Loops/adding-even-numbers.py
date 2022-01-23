# Don't change the lines below:
student_scores = input("Input a list of student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# Don't change the code above here

# Write your code below here:

total = 0
for number in range(2, 101, 2):
    # Confirm that you only return even numbers
    print(number)
    total += number
print(total)

# Alternative solution:

total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number
print(total2)
