import json
from tkinter import *
import tkinter.messagebox

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "The word doesn't exist. "


root = Tk()
root.geometry('450x550')
root.title("Shohidul Polash Dictionary")
# root.configure(background="#09eb63")
# root.configure(background="#0a0a0a")
# root.configure(background="#34b7f1")
# root.configure(background="#3d4849")
root.configure(background="#b2beb5")
# root.configure(background="#cca8f0")


textin = StringVar()


def clk():
    entered = ent.get()
    res = ""
    output1 = translate(entered)
    if type(output1) == list:
        for item in output1:
            res = res + item
        textin = res
    else:
        textin = output1
    output.insert(0.0, textin)


def exitt():
    tkinter.messagebox.showinfo("Shohidul Dictionary", 'Thank you for using Shohidul Polash Dictionary !')
    exit()


def clr():
    textin.set("")


lab = Label(root, text='Enter the Word:', bg="#b2beb5", font=('none 20 bold'))
lab.place(x=120, y=0)

ent = Entry(root, width=28, font='none 18 bold', textvar=textin, bg='white')
ent.place(x=45, y=45)

but = Button(root, width=7, text='Submit', command=clk, bg='powder blue', font='none 18 bold')
but.place(x=130, y=90)

but4 = Button(root, text='Clear', font='none 18 bold', bg='powder blue', command=clr)
but4.place(x=250, y=90)

labb = Label(root, text='Results:', bg="#b2beb5", font='none 18 bold')
labb.place(x=170, y=160)

output = Text(root, width=30, height=10, font='Arial  16 bold', fg="black")
output.place(x=45, y=200)

but1 = Button(root, padx=2, pady=2, text='Exit', command=exitt, bg='powder blue', font='none 18 bold')
but1.place(x=200, y=470)

root.mainloop()
