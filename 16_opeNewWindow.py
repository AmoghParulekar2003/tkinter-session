from tkinter import *

# Toplevel() = new window 'on top' of other windows, linked to a 'bottom' window
# Tk() = new independent window

def create_window():
    new_window = Tk()
    #new_window = Toplevel()
    old_window.destroy() # close older window

old_window = Tk() # bottom window

Button(old_window, text='create new window', command=create_window).pack()

old_window.mainloop()