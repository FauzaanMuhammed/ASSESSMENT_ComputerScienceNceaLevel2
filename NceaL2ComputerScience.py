import tkinter as tk
from tkinter import *
import time
root = tk.Tk()
image_placeholder = Label(root,text="Image")
image_placeholder.grid(column=0,row=0)

title_label = Label(root,text="Julie’s Party Hire",font=(("Arial"),20))
title_label.place(x=475,y=0)

root.geometry("1200x800-40+0")
root.mainloop()