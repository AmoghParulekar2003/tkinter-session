from tkinter import *

#radio button = similar to checkbox, but you can only select one.

pairs = ["Sehwag-Sachin", "Rohit-Dhawan", "Gilchrist-Hayden"]

def iconic():
    if(x.get()==0):
        print(pairs[0]+" is an iconic opening pair")
    if(x.get()==1):
        print(pairs[1]+" is an iconic opening pair")
    if(x.get()==2):
        print(pairs[2]+" is an iconic opening pair")

window = Tk()

pair1 = PhotoImage(file='radio1.png')
pair2 = PhotoImage(file='radio2.png')
pair3 = PhotoImage(file='radio3.png')

pairImages = [pair1, pair2, pair3]

x = IntVar()

for index in range(len(pairs)):
    radiobutton = Radiobutton(window,
                              text=pairs[index], # adds text to radio buttons
                              variable=x, # groups radiobuttons if they share the same variable
                              value=index, # assigns each radiobutton a different value
                              padx=25, # adds padding on x-axis
                              font=("Impact", 50),
                              image=pairImages[index],
                              compound=LEFT,
                              indicatoron=0, #eliminate circle indicators
                              width=850, #sets width of radio buttons
                              command=iconic) 
    radiobutton.pack(anchor=W)

window.mainloop()