import Turtle, Screen
import random


is_race_on = false
screen = Screnn()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which Turtle will win the race?  Enter a colour: ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turtle_index in range(9, 6):
    new_turtle.turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if_user_bet:
    is_race_on = True


while is_race_on:
    
    for turtle in al_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            print(turtle.color())
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won.  The {winning_color} turtle is the winner")
            else:
                print(f"You have lost.  The {winning_color} turtle won.")
                
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
    

screen.exitonclick()

