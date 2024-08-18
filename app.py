import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import random

# Function to generate a random color in hexadecimal format
def random_color():
    r = lambda: random.randint(0, 255)
    return '#%02X%02X%02X' % (r(), r(), r())

# Function to change background color and update label text
def change_colour():
    color = random_color()
    root.config(bg=color)
    label.config(text=f"Background Color: {color}", background=color, foreground='white' if int(color[1:3], 16) > 127 else 'black')

# Create the main window
root = ThemedTk(theme='yaru')
root.config(bg='white')
root.geometry("700x500")
root.title('Color Flipper')

# Create and configure the button
btn = ttk.Button(root, text="Change Colour", command=change_colour)
btn.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# Create and configure the label
label = tk.Label(root, text="Background Color:", bg='white', fg='black')
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Start the main loop
root.mainloop()
