from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turle")
# timmy_the_turtle.color("red")

for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)

for _ in range(15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()

screen = Screen()
screen.exitonclick()
