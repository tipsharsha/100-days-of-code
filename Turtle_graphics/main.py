"""Art"""
from turtle import Turtle,Screen

timmy = Turtle()

def alt():
    """does"""
    timmy.forward(15)
    timmy.penup()
    timmy.forward(15)
    timmy.pendown()
    timmy.forward(15)
screen = Screen()
screen.bgcolor('black')
timmy.shape('classic')
timmy.color('green')
alt()
timmy.left(90)
alt()
timmy.left(90)
alt()
timmy.left(90)
alt()
timmy.left(90)
heidi = Turtle()
heidi.color('red')

heidi.backward(90)

heidi.hideturtle()
timmy.hideturtle()


screen.exitonclick()
