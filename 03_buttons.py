from tkinter import *

# button = you click 'em, action happen!

count = 0

def click():
    global count
    count+=1
    print(count)

window = Tk()

photo = PhotoImage(file='reddit.png')

button = Button(window,
                text="Click Me!!",
                command=click, # note that () is not used here
                font=("Comic Sans", 30), #totally a formal font
                fg="red",
                bg="gray",
                activeforeground="red",
                activebackground="gray",
                state=ACTIVE,
                image=photo,
                compound='bottom')
button.pack()

window.mainloop()