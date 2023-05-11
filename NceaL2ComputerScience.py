import tkinter as tk
from tkinter import *
import time 
from PIL import Image,ImageTk

root = tk.Tk()

#Image
placeholder = Label(root,text="",height="15",width=5)
placeholder.grid(column=0,row=0)

img = ImageTk.PhotoImage(Image.open('computer_science_image.jpg')) # Opens computer_science_image.jpg, another file associated with the repo.
img_panel = Label(root, image = img)
img_panel.place(x=500,y=30)

#Title
title_label = Label(root,text="Julie’s Party Hire",font=(("Elephant"),20)) # The elephant font stands out compared to the rest of the text
title_label.place(x=475,y=0)

#Exit Button
exit_button=Button(root,text="QUIT",bg="#B50404",fg="white",command=quit) 
exit_button.place(x=1160,y=0)
def quit():  # The function for quitting
    root.destroy()

#Customer name title and entry
customer_name_title = Label(root,text="Customer Name",font=(("Arial"),14),width="33") # width=33 Seperates the entries
customer_name_title.grid(column=1,row=1,)                                   # -> So they don't look messy

customer_name_entry = Entry(root,width="25") 
customer_name_entry.grid(column=1,row=2)

#Recipt Number title and entry
recipt_number_title = Label(root,text="Recipt Number",font=(("Arial"),14)) # Width=33 is not used, as width covers both
recipt_number_title.grid(column=2,row=1)   
                                                            # To the right and left of the element        
recipt_number_entry = Entry(root,width="25")                # Therefore, it only needs to be used for every odd element
recipt_number_entry.grid(column=2,row=2)

#Item hired title and entry
item_hired_title = Label(root,text="Item Hired",font=(("Arial"),14),width="33") 
item_hired_title.grid(column=3,row=1)           
                                            
item_hired_entry = Entry(root,width="25")
item_hired_entry.grid(column=3,row=2)

#Number hired
num_item_hired_title = Label(root,text="Number Hired",font=(("Arial"),14))
num_item_hired_title.grid(column=4,row=1)

num_item_hired_entry = Entry(root,width="25")
num_item_hired_entry.grid(column=4,row=2)


# Main function for enter data button
def main_function():
    customer_name = customer_name_entry.get()
    recipt_number = recipt_number_entry.get()
    item_hired = item_hired_entry.get()
    num_item_hired = num_item_hired_entry.get()
    try:
        if 0<int(num_item_hired)<501:
            error_text["text"]=""
        else:
            error_text["text"]="Error! Number must be 1-500!"
    except:
        error_text["text"]="Error! Please put a number between 1-500 no letters"


#Enter Data Button
enter_data_button=Button(root,width="14",text="enter data",font=(("Arial"),14),command=main_function)
enter_data_button.place(x=500,y=290)

#Error Text
error_text=Label(root,font=(("Arial"),14))
error_text.place(x=500,y=330)


root.geometry("1200x800-40+0")
root.mainloop()