import random
from turtle import Turtle,Screen

colors = ['red','yellow','white','blue','green','pink']
screen = Screen()
screen.setup(width = 1000,height = 700)
def get_set(turtle,uo):
    """hehe"""
    turtle.shape('turtle')
    turtle.color(random.choice(colors))
    turtle.penup()
    turtle.goto(x = -450, y = uo)
def 
tim = Turtle()
get_set(tim,0)
tom = Turtle()
get_set(tom,30)
jess = Turtle()
get_set(jess,-30)
jake = Turtle()
get_set(jake,60)
screen.exitonclick()
