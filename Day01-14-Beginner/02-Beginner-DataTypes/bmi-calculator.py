# don't alter the code on the lines below
height = input("Enter your height (in metres): ")
weight = input("Enter your weight (in kilograms): ")
# Don't change ther code above

# Write your code below this line:

bmi = float(weight)/(float(height)**2)

bmi_as_int = round(bmi, 2)

print("Your BMI is: " + str(bmi_as_int))

print(f"Your BMI score is: {bmi_as_int}")
