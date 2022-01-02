# If the bill was $150.00, split between 5 people, with a 12% tip applied.
# Each person should pay (150.000 / 5) * 1.12 = 33.6
# Round the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")

bill = float(input("what was the total bill? £")) 
tip = int(input("What percentage tip would you like to give 10, 12 or 15?"))
people = int(input("How many people to split the bill?"))

bill_with_tip = tip/ 100 * bill + bill
# or could use: bill_with_tip = bill * (1 + tip / 100)
bill_per_person = bill_with_tip / people

# final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: £{final_amount}")

