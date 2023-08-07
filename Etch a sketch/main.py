from turtle import Turtle,Screen

timmy = Turtle()
timmy.color('yellow')
screen = Screen()
screen.bgcolor('black')
def move_forwards():
    """h"""
    timmy.setheading(90)
    timmy.forward(10)
def move_backwards():
    """moves backwards"""
    timmy.setheading(270)
    timmy.forward(10)
def turn_left():
    "moves up"
    timmy.setheading(180)
    timmy.forward(10)
def turn_right():
    """right turn"""
    timmy.setheading(0)
    timmy.forward(10)
IS_ON = True
while IS_ON:
    screen.listen()
    screen.onkey(key = "w",fun = move_forwards)
    screen.onkey(key = "d",fun = turn_right)
    screen.onkey(key = "a",fun = turn_left)
    screen.onkey(key = "s",fun = move_backwards)
screen.exitonclickonclick()
