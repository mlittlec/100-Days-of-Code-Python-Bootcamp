import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    retrun random_color

# RGB Colour Calculator : w3schools.com/colors/colors_rgb.asp
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fast")

for _ in range(200):
    # tim.color(random.choice(colours)))
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
    
