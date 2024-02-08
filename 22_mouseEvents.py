from tkinter import *

def doSomething(event):
    print("You clicked mouse at: "+str(event.x)+","+str(event.y))

window = Tk()

window.bind("<Button-1>",doSomething)
# Button-2, Button-3, ButtonRelease, Enter, Leave, Motion

window.mainloop()