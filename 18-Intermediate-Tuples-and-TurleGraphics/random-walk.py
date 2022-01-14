import turtle as t
import random

tim = t.Turtle()

# RGB Colour Calculator : w3schools.com/colors/colors_rgb.asp
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fast")

for _ in range(200):
    tim.color(random.choice(colours)))
    tim.forward(30)
    tim.setheading(random.choice(directions))
    
