from tkinter import *

# widgets = GUI elements like: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk() # instantiate an instant of a window

window.geometry("420x420") # change the size of window
window.title("Tkinter first program") # change title of window

icon = PhotoImage(file='reddit.png') # convert to photo image (tkinter can only recognize photoimage)
window.iconphoto(True, icon) # change the icon of window 

window.config(background="black") # change the background color of window

window.mainloop() # place window on computer screen, listen for events