import Turtle, Screen


screen = Screnn()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which Turtle will win the race?  Enter a colour: ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]


for turtle_index in range(9, 6):
    tim.turtle(shape="turtle")
    turtle.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=230, y=y_positions[turtle_index])





screen.exitonclick()

