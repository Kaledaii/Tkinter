import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.title("Demo")
HEIGHT=200
WIDTH=500
window.geometry(f"{WIDTH}x{HEIGHT}")
title_label=tk.Label(window,text="Miles to Kilometers Converter",font="Arial 20 italic bold underline",fg='black',padx=10,pady=10,borderwidth=5,relief=tk.RIDGE,cursor='plus')
title_label.pack()

# input frame
input_frame=tk.Frame(window)
entry=tk.Entry(input_frame)
button=tk.Button(input_frame,text="Convert")
entry.pack(side='left',padx=10)
button.pack(side='left')
input_frame.pack(pady=20)

# output frame
output_frame=tk.Frame(window)
output_label=tk.Label()

window.mainloop()