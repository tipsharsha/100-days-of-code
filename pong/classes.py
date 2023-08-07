"""What"""
from turtle import Turtle

class Paddle(Turtle):
    """maybe"""
    def __init__(self,given) -> None:
        super().__init__()
        self.shape('square')
        self.penup()
        self.goto(given,0)
        self.color('white')
        self.shapesize(stretch_len=1,stretch_wid=5)
    def go_up(self):
        """up"""
        x = self.xcor()
        y = self.ycor()
        self.goto(x,(y + 20))
    def go_down(self):
        """Helps go down"""
        x = self.xcor()
        y = self.ycor()
        self.goto(x,(y - 20))
class Ball(Turtle):
    """the ball"""
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.color("white")
        self.penup()
        self.shapesize(stretch_len= 0.5 ,stretch_wid=0.5)
        self.movex = 10
        self.movey = 7
    def move(self):
        """moves"""
        new_x = self.xcor() + self.movex
        new_y = self.ycor() + self.movey
        self.goto(new_x,new_y)
    def bouncey(self):
        """he"""
        self.movey *= -1
    def bouncex(self):
        """he"""
        self.movex *= -1
class scoreboard(Turtle):
    """shows score"""
    def __init__(self) -> None:
        super().__init__()
        self.color('Black')
        self.penup()
        self.hideturtle()
        self.goto(-100,200)
        self.write(0,align = "center",font = ("Arial",80,"normal"))
        self.goto(100,200)
        self.write(0,align = "center",font = ("Arial",80,"normal"))
    def change_score(self,score1,score2):
        """hello"""
        self.clear()
        self.goto(-100,200)
        self.write(score2,align = "center",font = ("Arial",80,"normal"))
        self.goto(100,200)
        self.write(score1,align = "center",font = ("Arial",80,"normal"))
