print("Welcome to the rollercoaster")
height = int(input("What is your height (in cm)?"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child tickets are £5.00")
    elif age <= 18:
        bill= 7
        print("Youth tickets are £7.00")
    elif 45 <= age <= 55:
        print("Mid-life crisis tickets are free.  Have a free ride on us...")
    else:
        bill = 12
        print("Adult tickets are £12.00")

    wants_photo = input("Do you want a photo taken? Y or N")
    if wants_photo == "Y":
        # Add £3 to their bill
        bill += 3
    print(f"Your total bill will be £{bill} please")

else:
    print("Sorry, you have to grow taller before you can ride.")
