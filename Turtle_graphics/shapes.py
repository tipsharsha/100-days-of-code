from turtle import Turtle,Screen, hideturtle,colormode
import random
tim = Turtle()
colormode(255)
colors = ['red','yellow','white','blue','green','pink']
screen = Screen()
screen.bgcolor('black')
def draw_shape(tu,n,l):
    angle = 360/n
    for _  in range (0,n):
        tu.forward(l)
        tu.right(angle)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    ra = (r,g,b)
    return ra
    
for shape in range (3,11):
    tim.color(random_color())
    draw_shape(tim,shape,45)

tim.hideturtle()
screen.exitonclick()
