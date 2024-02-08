from tkinter import *

def doSomething(event):
    #print("You pressed: "+event.keysym)
    label.config(text=event.keysym)

window = Tk()
window.geometry('900x150')

window.bind("<Key>", doSomething)

label = Label(window, font=('Helvetica', 50))
label.pack()

window.mainloop()