import tkinter as tk
from tkinter import *
from tkinter import ttk
import time 
from PIL import Image,ImageTk

global client_list;client_list=[]
global customer_name 
global recipt_number
global item_hired
global num_item_hired



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
        test = float(customer_name)+1 # checks if customer_name can be converted to float with no errors.
        customer_name_title["fg"]="red"#-> If so, this means customer_name must be a number/float, therefore an error has to be thrownout
        customer_memo="Error! Please put no numbers on 'customer name'" #-> As they aren't allowed on customer names
        error_text["text"]=customer_memo
    except:
        customer_name_title["fg"]="black"
        customer_memo=""

    try:
        test=int(recipt_number)+1 #Try adding 1 to the recipt number.
        recipt_number_title["fg"]="black"
        recipt_memo="" # Recipt memo variable allows us to add messages to the end of error messages without creating a new function
    except:            # If 1 can't be added to recipt number i.e it's a string, throw an error
        recipt_number_title["fg"]="red" 
        recipt_memo="'Error! Please put any number for 'recipt number'"
        error_text["text"]=recipt_memo 
    try:        # Checking if num_item_checked is between 1-500 AND is not a string, no errors come as a result
        if 0<int(num_item_hired)<501:
            error_text["text"]=""+recipt_memo+customer_memo
            num_item_hired_title["fg"]="black"
        else:
            error_text["text"]=f"Error! Number must be 1-500!\n{recipt_memo}{customer_memo}"
            num_item_hired_title["fg"]="red"
    except:
        error_text["text"]=f"Error! Please put a number between 1-500 no letters for 'number hired'\n {recipt_memo}\n{customer_memo}"
        num_item_hired_title["fg"]="red"

    if error_text["text"]=="":
        deletion_instruction_title=Label(root,text="Press 'Enter' to delete rows you have clicked.")
        deletion_instruction_title.place(x=450,y=355)


        column_list=("row_number","customer_name","recipt_number","item_hired","number_hired") 
        global treeview
        treeview = ttk.Treeview(root,columns=column_list,height=11)
        treeview.column("#0", width=0)
        treeview.heading("row_number",text="Row");treeview.column("#1", width=45)
        treeview.heading("customer_name",text="Customer Name")
        treeview.heading("recipt_number",text="Recipt Number")
        treeview.heading("item_hired",text="Item Hired")
        treeview.heading("number_hired",text="Number Hired")
        treeview.place(x=150,y=380)
        client_list.append([len(client_list)+1,customer_name,recipt_number,item_hired,num_item_hired])
        for i in client_list:
            treeview.insert("",tk.END,values=i)
  

def delete_row(event):

    if client_list: # Only runs function if client_list isn't empty, to prevent errors.

        # Getting the information about the selected row, so that row can be deleted when enter is pressed 
        full_selected_list = treeview.item(treeview.focus())
            
        # Deletion of the selected row. 
        row_deleted = full_selected_list["values"][0]
        client_list.pop(row_deleted-1) # Since the row value is 1 greater than it normaly is, we must -1 to normalize the pop function
        
        # Deletion of selected rows
        item_selected = treeview.selection()[0] # Treeview returns the tuple of selected items.[0] makes sure others aren't deleted on accident.
        treeview.delete(item_selected)
        # Changing the rows numbers to be updated after all changes are made to the treeview
        for i in range(len(client_list)):
            client_list[i][0]=i+1 # i starts at 0 and goes up by 1, this allows to correct row numbers that have been altered by deleting rows
                                # 1 has been added, so the row actually starts at 1 instead of 0 

        # Global variable treeview cannot be reassigned, so we must delete all the items in it, and add client_list onto it again
        # This will allow us to update the list after rows have been deleted
        for i in treeview.get_children():
            treeview.delete(i)
        treeview.column("#0", width=0)
        treeview.heading("row_number",text="Row");treeview.column("#1", width=45)
        treeview.heading("customer_name",text="Customer Name")
        treeview.heading("recipt_number",text="Recipt Number")
        treeview.heading("item_hired",text="Item Hired")
        treeview.heading("number_hired",text="Number Hired")
        treeview.place(x=150,y=380)
        for i in client_list:
            treeview.insert("",tk.END,values=i)

    
root.bind("<Return>",delete_row)

#Enter Data Button
enter_data_button=Button(root,width="14",text="enter data",font=(("Arial"),14),command=main_function)
enter_data_button.place(x=500,y=290)


#Error Text
error_text=Label(root,font=(("Arial"),14))
error_text.place(x=300,y=330)


root.geometry("1200x800-40+0")
root.mainloop()