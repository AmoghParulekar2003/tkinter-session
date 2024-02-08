from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HTML file",".html"),
                                        ("All files",".*"),
                                    ],
                                    initialdir="C:\\Users\\Amogh Parulekar\\OneDrive\\Desktop\\tkinter")
    if file is None:
        return
    #filetext = str(text.get(1.0, END))
    filetext = input("Enter some text i guess: ")
    file.write(filetext)
    file.close()

window = Tk()

button = Button(text='Save', command=saveFile)
button.pack()

text = Text(window)
text.pack()

window.mainloop()