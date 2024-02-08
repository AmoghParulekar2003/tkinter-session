from tkinter import *

# frame = a rectangular container to group and hold widgets

window = Tk()

top_lineup_frame = Frame(window, bg='green', bd=5, relief=RAISED)
top_lineup_frame.pack()

Button(top_lineup_frame, text="Cristiano Ronaldo" , font=("Consolas", 15), width=20).pack(side=LEFT, padx=5)
Button(top_lineup_frame, text="Karim Benzema", font=("Consolas", 15), width=20).pack(side=LEFT, padx=5)
Button(top_lineup_frame, text="Gareth Bale", font=("Consolas", 15), width=20).pack(side=LEFT, padx=5)

middle_lineup_frame = Frame(window, bg='green', bd=5, relief=RAISED)
middle_lineup_frame.pack()

Button(middle_lineup_frame, text="Luka Modric", font=("Consolas", 15), width=20).pack(side=LEFT, padx=5)
Button(middle_lineup_frame, text="Casemiro", font=("Consolas", 15), width=20).pack(side=LEFT, padx=5)
Button(middle_lineup_frame, text="Toni Kroos", font=("Consolas", 15), width=20).pack(side=LEFT, padx=5)

bottom_lineup_frame = Frame(window, bg='green', bd=5, relief=RAISED)
bottom_lineup_frame.pack()

Button(bottom_lineup_frame, text="Marcelo", font=("Consolas", 15), width=20).pack(side=LEFT, padx=5)
Button(bottom_lineup_frame, text="Sergio Ramos", font=("Consolas", 15), width=20).pack(side=LEFT, padx=5)
Button(bottom_lineup_frame, text="Nacho Fernandez", font=("Consolas", 15), width=20).pack(side=LEFT, padx=5)
Button(bottom_lineup_frame, text="Marcelo", font=("Consolas", 15), width=20).pack(side=LEFT, padx=5)

goalkeeper_frame = Frame(window, bg='green', relief=RAISED)
goalkeeper_frame.pack()
Button(goalkeeper_frame, text="Keylor Navas", font=("Consolas", 15), width=20).pack(side=TOP, padx=5)

window.mainloop()
