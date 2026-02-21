import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.title("Demo")
HEIGHT=400
WIDTH=400
window.geometry(f"{WIDTH}x{HEIGHT}")
title_label=tk.Label(master=window,text="Yo Wassup Dawg",font="Algerian 20",fg='blue',bg='pink',padx=10,pady=10,borderwidth=5,relief=tk.GROOVE,cursor="heart")
title_label.pack()

window.mainloop()