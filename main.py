import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def convert(event=None):
    try:
        miles=float(number.get())
        km=miles*1.609
        result.set(f"{km:.2f} km")
    except ValueError:
        result.set("Invalid input")
def only_numbers(P):
    if P=='' or P.replace('.','',1).isdigit():
        return True
    return False

window=ttk.Window(themename='superhero')
window.resizable(True,True)
window.title("Miles to Kilometers Converter")

WIDTH=500
HEIGHT=250
window.geometry(f"{WIDTH}x{HEIGHT}")
title_label=ttk.Label(window,text="Miles to Kilometers Converter",font="Arial 20 bold italic",bootstyle='primary')
title_label.pack()

# input frame
input_frame=ttk.Frame(window)
number=tk.StringVar()
vcmd=(window.register(only_numbers),"%P")
entry=ttk.Entry(input_frame,textvariable=number,validate="key",validatecommand=vcmd,bootstyle='success')
entry.focus()
button=ttk.Button(input_frame,text="Convert",cursor='hand2',command=convert,bootstyle='warning-outline')
entry.pack(side='left',padx=10,fill='x',expand=True)
button.pack(side='left')
input_frame.pack(pady=20,fill='x',expand=True)

#output frame
output_frame=ttk.Frame(window)
result=tk.StringVar()
output_label=ttk.Label(output_frame,text="Output",font="Arial 20 italic",textvariable=result,bootstyle='success')
output_label.pack(pady=20)
output_frame.pack(fill='both',expand=True)

window.bind('<Return>', lambda event: convert())  
window.bind('<Escape>', lambda event: window.destroy())
window.mainloop()