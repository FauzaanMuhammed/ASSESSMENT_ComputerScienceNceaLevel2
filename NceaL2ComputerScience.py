import tkinter as tk
from tkinter import *
import time
root = tk.Tk()
image_placeholder = Label(root,text="Image",height="5")
image_placeholder.grid(column=0,row=0)

title_label = Label(root,text="Julie’s Party Hire",font=(("Arial"),20))
title_label.place(x=475,y=0)

#Customer name title and entry
customer_name_title = Label(root,text="Customer Name",font=(("Arial"),14))
customer_name_title.grid(column=1,row=1)

customer_name_entry = Entry(root,width="25")
customer_name_entry.grid(column=1,row=2)

#Recipt Number title and entry
recipt_number_title = Label(root,text="Recipt Number",width="35",font=(("Arial"),14)) # width=35 Seperates the entries
recipt_number_title.grid(column=2,row=1)                          # -> So they don't look messy
recipt_number_entry = Entry(root,width="25")
recipt_number_entry.grid(column=2,row=2)

#Item hired title and entry
item_hired_title = Label(root,text="Item Hired",font=(("Arial"),14)) # Width=35 is not used, as width covers both
item_hired_title.grid(column=3,row=1)           # To the right and left of the element
                                            # Therefore, it only needs to be used for every odd element
item_hired_entry = Entry(root,width="25")
item_hired_entry.grid(column=3,row=2)

#Number hired
num_item_hired_title = Label(root,text="Number Hired",width="35",font=(("Arial"),14))
num_item_hired_title.grid(column=4,row=1)

num_item_hired_entry = Entry(root,width="25")
num_item_hired_entry.grid(column=4,row=2)

root.geometry("1200x800-40+0")
root.mainloop()