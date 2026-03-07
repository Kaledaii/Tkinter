# Validation demo

import tkinter as tk

def debug_validate(action, index, char, current_value, proposed_value):
    print("Action:", action)          # %d → 1=insert, 0=delete, -1=focus change
    print("Index:", index)            # %i → position of change
    print("Char typed:", char)        # %S → the character being inserted/deleted
    print("Current value:", current_value)  # %s → value before change
    print("Proposed value:", proposed_value) # %P → value after change
    print("-" * 30)
    return True   # Always allow the change

root = tk.Tk()
root.title("Validation Demo")

vcmd = (root.register(debug_validate), "%d", "%i", "%S", "%s", "%P")

entry = tk.Entry(root, validate="key", validatecommand=vcmd)
entry.pack(padx=20, pady=20)

root.mainloop()