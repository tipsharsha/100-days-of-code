"""An Time management program"""
from tkinter import *
#CONSTANSTS#
FONT = "Proxima Nova"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
window = Tk()
window.title("Pomodoro")
window.config(padx = 50,pady = 50,bg = YELLOW)
label= Label(text="Timer",fg = GREEN,bg = YELLOW,font=(FONT,26,"bold"))
label.grid(column=1,row=0)
can = Canvas(width = 210,height =224,bg= YELLOW,highlightthickness=0)
x = PhotoImage(file = "Pomodoro/tomato.png")
start_button = Button(text="start",highlightthickness=0)
start_button.grid(column=0,row=3)
stop_button = Button(text="stop",highlightthickness=0)
stop_button.grid(column=2,row=3)
can.create_image(105,100,image = x)
can.create_text(103,110,text = "00:00",fill = "white",font = (FONT,36,"bold"))
can.grid(column=1,row=1)
check_ark = Label(text = "✓",bg = YELLOW)
check_ark.grid(column=1,row= 3)


window.mainloop()
