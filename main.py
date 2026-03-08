import os
import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter.messagebox as msg

def change_theme(theme):
    window.style.theme_use(theme)

def convert(event=None):
    try:
        value=float(number.get())
        unit = unit_choice.get()
        if unit == "Miles → Km":
            output=f"{value * 1.609:.2f} km"
            #history_list.app
        elif unit == "Km → Miles":
            output=f"{value / 1.609:.2f} miles"
        elif unit=='Foot → Centimeters':
            output=f"{value * 30.48:.2f} cm"
        elif unit=='Inch → Centimeters':
            output=f"{value * 2.54:.2f} cm"
        elif unit=='Yard → Centimeters':
            output=f"{value * 91.44:.2f} cm"
        result.set(output)
        history_list.insert(0, f"{value} {unit} → {output}")
        
    except ValueError:
        output="Invalid input"
        result.set(output)
    
def only_numbers(P):
    if P=='' or P.replace('.','',1).isdigit():
        return True
    return False
def clear_history():
    history_list.delete(0, 'end')

window=ttk.Window(themename='cyborg')
image=tk.PhotoImage(file='assets/logo.png')
window.iconphoto(False, image)
window.resizable(True,True)
window.title("Unit Converter")


WIDTH=500
HEIGHT=500
window.geometry(f"{WIDTH}x{HEIGHT}")
title_label=ttk.Label(window,text="Unit Converter",font="Arial 20 bold italic",bootstyle='primary')
title_label.pack()

# menu bar
menubar=tk.Menu(window)
window.config(menu=menubar)

file_menu=tk.Menu(menubar,tearoff=0)
file_menu.add_command(label="Exit",command=window.destroy)
menubar.add_cascade(label="File",menu=file_menu)

theme_menu = tk.Menu(menubar, tearoff=0)
for theme in ["superhero", "darkly", "flatly", "cyborg", "minty"]:
    theme_menu.add_command(label=theme.capitalize(),
                           command=lambda t=theme: change_theme(t))
menubar.add_cascade(label="Themes", menu=theme_menu)

history_menu=tk.Menu(menubar,tearoff=0)
history_menu.add_command(label="Clear History",command=lambda: clear_history())
menubar.add_cascade(label="History",menu=history_menu)

help_menu=tk.Menu(menubar,tearoff=0)
help_menu.add_command(label="About",command=lambda: msg.showinfo("About","Unit Converter\nVersion 1.0",icon='info'))
menubar.add_cascade(label="Help",menu=help_menu)

# input frame
input_frame=ttk.Frame(window)
number=tk.StringVar()
vcmd=(window.register(only_numbers),"%P")
entry=ttk.Entry(input_frame,textvariable=number,validate="key",validatecommand=vcmd,bootstyle='success')
entry.focus()

unit_choice=ttk.Combobox(input_frame,values=['Miles → Km','Km → Miles','Foot → Centimeters','Inch → Centimeters','Yard → Centimeters'],state='readonly',bootstyle='info')
unit_choice.current(0)

button=ttk.Button(input_frame,text="Convert",cursor='hand2',command=convert,bootstyle='warning-outline')
entry.pack(side='left',padx=2,fill='x',expand=True)
unit_choice.pack(side='left',padx=10)
button.pack(side='left',padx=10)
input_frame.pack(pady=20,fill='both',expand=True)

#output frame
output_frame=ttk.Frame(window)
result=tk.StringVar()
output_label=ttk.Label(output_frame,text="Output",font="Arial 20 italic",textvariable=result,bootstyle='success')
output_label.pack(anchor='center',pady=20)
output_frame.pack(fill='both',expand=True)

# history frame
history_frame=ttk.Labelframe(window,text="Conversion History",bootstyle='secondary',padding=10)
history_list=tk.Listbox(history_frame,height=6)
history_list.pack(fill='both',expand=True)
history_frame.pack(fill='both',expand=True,padx=20,pady=10)

window.bind('<Return>', lambda event: convert())  
window.bind('<Escape>', lambda event: window.destroy())
window.mainloop()