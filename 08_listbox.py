from tkinter import *

# listbox = A listing of selectable text items within it's own container

def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    print("You have ordered: ")
    #print(listbox.get(listbox.curselection()))
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())
    entryBox.delete(0, END)

def delete():
    #listbox.delete(listbox.curselection())
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,
                  bg='#f7ffde',
                  font=("Constantia", 35),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, "Pizza")
listbox.insert(2, "Burger")
listbox.insert(3, "Vadapav")
listbox.insert(4, "Noodles")
listbox.insert(5, "Daabeli")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window, text="SUBMIT", command=submit)
submitButton.pack()

addButton = Button(window, text="ADD", command=add)
addButton.pack()

deleteButton = Button(window, text="DELETE", command=delete)
deleteButton.pack()

window.mainloop()