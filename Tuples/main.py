from turtle import Turtle,Screen, hideturtle,colormode

import random
tim = Turtle()
tim.color('white')
colormode(255)
colors = ['red','yellow','white','blue','green','pink']
screen = Screen()
screen.bgcolor('black')

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    ra = (r,g,b)
    return ra
tim.speed(0)
for n in range (0,50):
    tim.color(random_color())
    tim.right(7.2)
    tim.circle(30)

screen.exitonclick()