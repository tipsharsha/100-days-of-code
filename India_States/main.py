import turtle
import pandas
screen = turtle.Screen()
screen.title("Indian states")
image = "India_States\political-map.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("dat.csv")

data_dict = data.to_dict()
states = data_dict['states']
x = data_dict['x']
y = data_dict['y']

t = turtle.Turtle()
t.hideturtle()
t.penup()
guess = 0

while guess < 28:
    answer_state = screen.textinput(title = "Guess the State", prompt ="Hit exit to exit\nEnter the state's name?")
    for lock in states:
        if answer_state == states[lock]:
            gox = x[lock]
            goy = y[lock]
            t.goto(gox-5,goy)
            t.write(states[lock])
            guess += 1
        elif answer_state == 'exit':
            quit()
            

turtle.mainloop()
