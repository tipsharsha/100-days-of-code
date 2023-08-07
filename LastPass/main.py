"""Password Manager"""
#IMPORTS
from cgitb import text
from  tkinter import *
from tkinter import messagebox
import random
import json
import pyperclip

#CONSTANTS
BGCOLOR = "black"
FGCOLOR = "white"
FONT = ("Roboto",10)
# ti = "LastPass/moon.png"
# pi = "LastPass/sun.png"
#theme
def change_theme():
    "changes theme"
    global BGCOLOR
    temp = BGCOLOR
    global FGCOLOR
    BGCOLOR = FGCOLOR
    FGCOLOR = temp
    # global ti
    # global pi
    # temp = ti
    # ti = pi
    # pi = temp
    window.config(bg=BGCOLOR)
    web.config(bg = BGCOLOR,fg =FGCOLOR)
    pas.config(bg = BGCOLOR,fg=FGCOLOR)
    mail.config(bg = BGCOLOR,fg=FGCOLOR)
    canvas.config(bg = BGCOLOR)
    # pik = PhotoImage(ti)
    # race.config(image=pik)

#Functioning
def search():
    """searches for old passwords"""
    with open("LastPass/data.json","r") as file:
        data = json.load(file)
        website = web_entry.get()
        if website in  data:
            pas_entry.delete(0,END)
            mail_entry.delete(0,END)
            word = data[website]["password"]
            mai= data[website]["email"]
            pas_entry.insert(0,word)
            mail_entry.insert(0,mai)
            messagebox.showinfo(title= website,message=f"Email: {mai}\nPassword: {word}")
            pyperclip.copy(word)
        else:
            messagebox.showinfo(title= "Oops",message= "Data isn't registered to this website")
def save():
    """saves the password"""
    website = web_entry.get()
    email = mail_entry.get()
    password = pas_entry.get()
    new_data = {website:
                {
                "email":email,
                "password":password,
                },
            }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?\n")
        if ok:
            try:
                with open("LastPass/data.json", "r") as file:
                    prev = json.load(file)                    
            except FileNotFoundError:
                with open("LastPass/data.json", "w") as file:
                    json.dump(new_data,file,indent=4)
            else:
                with open("LastPass/data.json", "w") as file:
                    prev.update(new_data)
                    json.dump(prev,file,indent=4)
            finally:
                web_entry.delete(0, END)
                pas_entry.delete(0, END)
#random password
def lazy():
    """what"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    lette = int(input ("How many letters do you need?"))
    sp_char = int(input ("How many sp chars do you need?"))
    numbe = int(input("How many numbers do you want in your password?"))
    my_list =[]
    for number in range(0,numbe):
        my_list.append(random.choice(numbers))
    for number in range(0,lette):
        my_list.append(random.choice(letters))
    for number in range(0,sp_char):
        my_list += random.choice(symbols)
    random.shuffle(my_list)
    password = ""
    for list in my_list:
        password += list
    pas_entry.insert(0,password)
    pyperclip.copy(password)
    messagebox.showinfo(title="message",message="Your password is copied to your clipboard")

#UI

    #Window
window = Tk()
window.title("Password Manager")
window.config(padx=10,pady=10,bg=BGCOLOR)
    
    #Labels
web = Label(text = "Website: ",fg=FGCOLOR,font = FONT)
web.config(bg = BGCOLOR)
web.grid(row = 1,column=0)
mail = Label(text = "Email/Username: ",fg=FGCOLOR,font=FONT)
mail.config(bg = BGCOLOR)
mail.grid(row=2,column=0)
pas = Label(text = "Password: ",fg = FGCOLOR,font = FONT)
pas.config(bg = BGCOLOR)
pas.grid(row = 3,column=0)

    #Entries
web_entry = Entry()

web_entry.grid(row = 1,column=1)
mail_entry = Entry()
mail_entry.grid(row=2,column=1)
mail_entry.insert(0,"someone@email.com")
pas_entry = Entry()
pas_entry.grid(row = 3,column=1)

    #Buttons
gen = Button(text="Password Generator",command = lazy)
gen.config(bg="lemon chiffon")
gen.grid(row = 3,column=2)
ad = Button(text = "Add",command=save)
ad.config(bg= "lemon chiffon")
ad.grid(row= 4,column=1)
# foto = PhotoImage(file =ti)
race = Button(text = "theme",command =change_theme)
race.config(bg="lemon chiffon")
race.grid(column=4,row = 3)
sea = Button(text = "Search",bg = "lemon chiffon",command=search)
sea.grid(row =1,column=2)

    #Canvas setup
lock = PhotoImage(file = "LastPass/icon.png")
canvas = Canvas(height = 300,width = 200)
canvas.config(bg = BGCOLOR,highlightthickness=0)
canvas.create_image(110,150,image = lock)
canvas.grid(row = 0,column= 1)


#End of TK
window.mainloop()
