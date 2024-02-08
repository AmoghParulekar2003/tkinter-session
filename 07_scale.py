from tkinter import *

def submit():
    print("The temperature is: "+str(scale.get())+" degrees C")

window = Tk()

scale = Scale(window, 
              from_=100, 
              to=0,
              length=600,
              orient=VERTICAL, #orientation of scale
              font=("Consolas", 20),
              tickinterval=10, #adds numeric indicators for value
              #showvalue=0, #hide current value
              resolution=5,
              troughcolor='#69eaff',
              fg='#ff1c00',
              bg='#111111',
              )
scale.set((scale['from']-scale['to'])/2+scale['to'])
scale.pack()

button = Button(window, text="Submit", command=submit)
button.pack()

window.mainloop()