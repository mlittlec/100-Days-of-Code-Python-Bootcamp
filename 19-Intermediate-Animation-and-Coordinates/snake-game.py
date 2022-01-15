from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, Height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

starting_position = [(0, 0), (-20, 0), (-40, 0)]


for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on = True
while game_is_on:
    for seg in segments:
        seg.forward(20)

# segment_2 = Turtle(shape="square")
# segment_2.color("white")
# segment_2.goto(-20, 0)


# segment_3 = Turtle(shape="square")
# segment_3.color("white")
# segment_3.goto(-40, 0)


screen.exitonclick()
