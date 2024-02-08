from tkinter import *
from tkinter import messagebox

def click():
    #messagebox.showinfo(title="Info message box", message="This is Tkinter")
    #messagebox.showinfo(title="WARNING!!", message="Tactical nuke incoming!!")
    #messagebox.showerror(title="ERROR!!", message="Something went wrong")
    if messagebox.askokcancel(title="ask ok cancel", message="Do you want to do the thing?"):
        print("You did a thing")
    else:
        print("You canceled a thing")
    #askretrycancel
    #askyesno
    #askquestion
    #askyesnocancel

window = Tk()

button = Button(window, command=click, text="Click me!")
button.pack()

window.mainloop()