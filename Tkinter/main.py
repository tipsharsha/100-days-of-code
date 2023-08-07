import tkinter

window = tkinter.Tk()
window.title("GUI")
window.minsize(width = 500,height = 300)

labels = tkinter.Label(text = "I am label",font = ("Arial",20,"italic"))
labels.pack(expand = True)

window.mainloop()
