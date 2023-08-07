"""maybe"""
import time
from turtle import Screen
from classes import Paddle,Ball,scoreboard

score = scoreboard()
score1 = 0
score2 = 0
screen = Screen()

screen.bgcolor('blue')
screen.setup(width = 600,height = 600)
screen.title("Pong")

P1 = Paddle(270)
P1.color("yellow")
P2 = Paddle(-270)
P2.color("green")
screen.tracer(0)

screen.listen()
ball = Ball()

screen.onkey(P1.go_up,"Up")
screen.onkey(P1.go_down,"Down")

screen.onkey(P2.go_up,"w")
screen.onkey(P2.go_down,"s")

IS_ON = True
while IS_ON:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor() <-280:
        ball.bouncey()
    if ball.xcor()>280 or ball.xcor() <-280:
        ball.bouncex()
    #detect collision
    if ball.distance(P1) <50 and ball.xcor() >260:
        ball.bouncex()
        score1 += 1
        score.change_score(score1,score2)
    if ball.distance(P2) <50 and ball.xcor() <-260:
        ball.bouncex()
        score2 += 1
        score.change_score(score1,score2)
screen.exitonclick()
