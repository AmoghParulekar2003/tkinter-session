from tkinter import *

def display():
    if(x.get()=="yes"):
        print("You passed the Vibe check :)")
    else:
        print("You didn't passed the Vibe check :(")

window = Tk()

x = StringVar()
photo = PhotoImage(file="reddit.png")

check_button = Checkbutton(window,
                           text="Vibe Check",
                           variable=x,
                           onvalue="yes",
                           offvalue="no",
                           command=display,
                           font=("Arial", 20),
                           fg="red",
                           bg="gray",
                           activeforeground="red",
                           activebackground="gray",
                           padx=25,
                           pady=10,
                           image=photo,
                           compound=LEFT)

check_button.pack()

window.mainloop()