# Don't change the code below:
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights[n])
  student_heights[n] = int(student_heights[n])
print(student_heights)
# Don't change the code above
               
# Write your code below this line:
print(len(student_heights))

# Something you could use that makes this super easy is (however we need to use a Loop):
#total_height = sum(student_heights)
#number_of_students = len(student_heights)
#average_height = round(total_height / number_of_students)
#print(average_height)

# Calculate the Sum() of the heights
total_height = 0
for height in student_heights:
  total_height += height

print(total_height)

# Calculate the Len() of the students List (ie: the number):
number_of_students = 0
for student in student_heights:
  number_of_students += 1

print(number_of_students)

average_height = round(total_height / number_of_students)
#print(average_height)
