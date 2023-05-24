import tkinter as tk
from tkinter import *
from tkinter import ttk
from random import randint
from PIL import Image,ImageTk
from tkinter import messagebox

root = tk.Tk() #Creates an instance of tkinter

global client_list # Global variables are able to be used outside of the function it was assigned, which is very useful

save_file = open("save_data_party_hire.txt","r")# Open save file for reading.
saved_list = save_file.readlines()  # Read all the lines of the save_data_party_hire.txt file, and put it into a list
file_length=len(saved_list)
save_file.close()

new_saved_list=[] # Contains info about the new improved list.
for i in saved_list:
    new_saved_list.append(i[0:-1]) #This the start to 2nd to last item of the list, and put it onto a new list. This is done, as the normal list includes line breaks, which we don't want

client_list=[]
for i in range(0,file_length,5): # This function puts 5 of every item into a list, which is put onto a list. The reason multidimensional lists are used are because they add an extra layer of convienence.
    client_list.append([new_saved_list[i],new_saved_list[i+1],new_saved_list[i+2],new_saved_list[i+3],new_saved_list[i+4]])

deletion_instruction_title=Label(root,text="Press the 'Enter' key to delete rows you have clicked.")
deletion_instruction_title.place(x=440,y=355) # This tells user instructions on how to the enter key to delete rows
column_list=("row_number","customer_name","recipt_number","item_hired","number_hired") 
treeview = ttk.Treeview(root,columns=column_list,height=11)
treeview.column("#0", width=0) # Hides the unused row
treeview.heading("row_number",text="Row");treeview.column("#1", width=45)
treeview.heading("customer_name",text="Customer Name")# The heading for the treeview.
treeview.heading("recipt_number",text="Recipt Number")
treeview.heading("item_hired",text="Item Hired")
treeview.heading("number_hired",text="Number Hired");treeview.column("#5", width=150) # Fixed widths stop other elements from pushing columns
treeview.place(x=200,y=380)

for i in client_list:
    treeview.insert("",tk.END,values=i)
treeview_scrollbar = ttk.Scrollbar(root, orient="vertical", command=treeview.yview)
treeview_scrollbar.place(x=979, y=420, height=180)
treeview.configure(yscrollcommand=treeview_scrollbar.set)


def disable_recipt_entry():
    if random_recipt_checked.get()==1: 
        recipt_number_entry["state"]=DISABLED # if checkbox is on, disabled the recipt_number entry
        if recipt_number_entry.get()=="": # If the recipt_number entry is empty
            recipt_number_title["fg"]="black" # -> Display the recipt number title as black, to prevent confusion. 
    else:
        recipt_number_entry["state"]=NORMAL   # otherwise, it is enabled

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
exit_button = Button(root,text="QUIT",bg="#B50404",fg="white",command=quit) 
exit_button.place(x=1160,y=0)
def quit():  # The function for quitting
    root.destroy()

# Help Button
help_button = Button(root,text="❓Help",bg="#3498DB")
help_button.place(x=1145,y=30)
def help_popup():
    messagebox.showinfo("Help","If you enter data and an error shows up, follow the instructions and then enter you data. The color of the text will change from red to black if it is valid.\nPress enter to delete rows when you have clicked them.\nThe table also has a scrollbar.\nData is automatically saved.")
help_button.configure(command=help_popup)
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

#Random Recipt Number Checkbox
random_recipt_checked  = tk.IntVar()
random_recipt_checkbox = Checkbutton(root,text="random value",variable=random_recipt_checked,command=disable_recipt_entry,font=(("Arial bold"),12)) # changes the font from default settings to make the text easier to see.
random_recipt_checkbox.grid(column=2,row=3)

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
    if random_recipt_checked.get()==1: # checks if random_recipt check list has been ticked. if so, generate a random number from 100,000 to 999,999 for it. 
        recipt_number=randint(100000,999999)
    else:
        recipt_number = recipt_number_entry.get() # Otherwise, get the manual entry

    item_hired = item_hired_entry.get()
    num_item_hired = num_item_hired_entry.get()
    error_message="" 
    try: # The reason try is used instead of type() is because all entry.get values are strings. Because of this, I used try to figure out if they can be converted into a float/int with/without errors depending on the scenario.
        test = float(customer_name)+1 
        customer_name_title["fg"]="red"#-> Since the entry can be converted without any error message, this means customer_name must be a number/float, therefore an error has to be thrownout
        error_message="Customer name: Please put no numbers\n\n" # Adds a new errors message, and a double line break for neatness

    except:
        if customer_name=="": # customer name cannot be empty, however. So an error must be thrown out.
            customer_name_title["fg"]="red"
            error_message="Customer Name: Please don't leave empty, you can put anything but numbers\n\n"
        else:
            customer_name_title["fg"]="black" # Sets the text color back to black if no error.
        

    try:
        test=int(recipt_number)+1 #Try adding 1 to the recipt number.
        recipt_number_title["fg"]="black"
        
    except:           
        recipt_number_title["fg"]="red"
        if not random_recipt_checked.get()==1: # If the recipt checkbox is not chcked, and the checbox is empty, give the user an error, as a value must be given for manual recipt
            error_message+="Recipt number: Please put any number. Make sure to remove any letters, or tick the tickbox for generating a random recipt.\n\n"

    if item_hired=="":
        error_message+="item hired: Please put don't leave this empty\n\n"
        item_hired_title["fg"]="red"
    else:
        item_hired_title["fg"]="black"

    try:        # Checking if num_item_checked is between 1-500 AND is not a string, no errors come as a result
        if 0<int(num_item_hired)<501:
            num_item_hired_title["fg"]="black"
        else:
            error_message+="Number hired: Number must be between between 1-500! Make sure to remove any letters" # No \n is used, as it is not needed for the last error message, as no other messages come after it
            num_item_hired_title["fg"]="red"
    except:
        error_message+="Number hired: Please put a number. Make sure to remove letters"
        num_item_hired_title["fg"]="red" # If num_item_hired cannot be turned into a number, it must be a string.

    if error_message=="": # If no errors are present, continue the program.
        for i in treeview.get_children():
            treeview.delete(i)     

        client_list.append([len(client_list)+1,customer_name,recipt_number,item_hired,num_item_hired]) #All information from the entries is appended onto the end of global list
        for i in client_list:
            treeview.insert("",tk.END,values=i) # Adds back client_list onto treeview after it has been reassigned
        file = open("save_data_party_hire.txt","w")
        file.write("") # Clears save_data_party_hire
        file.close()

        file=open("save_data_party_hire.txt","a")
        for i in client_list:
            for x in range(5): # Uses a nested for loop through the 2 dimensional list to get each values of the list's list 5 items.
                file.write(f"{i[x]}\n") 
        file.close()

    else:
        messagebox.showerror("Error!",error_message)
  
def delete_row(event):

    try: # Prevents errors that would happens if enter is pressed with no treeview
        root.forget(treeview)
        # Getting the information about the selected row, so that row can be deleted when enter is pressed 
        full_selected_list = treeview.item(treeview.focus())
        
        # Deletion of the selected row. 
        row_deleted = full_selected_list["values"][0]
        client_list.pop(row_deleted-1) # Since the row value is 1 greater than it normaly is, we must -1 to normalize the pop function
        
        # Deletion of selected rows
        item_selected = treeview.selection()[0] # Treeview returns the tuple of selected items.[0] is the part of the tuple that needs to be deleted
        treeview.delete(item_selected)
        # Changing the rows numbers to be updated after all changes are made to the treeview
        for i in range(len(client_list)):
            client_list[i][0]=i+1 # Corrects row numbers when row is deleted.
                                # 1 has been added, so the row actually starts at 1 instead of 0 

        # This will allow us to update the list after rows have been deleted
        for i in treeview.get_children():
            treeview.delete(i)
        for i in client_list:
            treeview.insert("",tk.END,values=i)

        file = open("save_data_party_hire.txt","w")
        file.write("") # Clears save_data_party_hire
        file.close()

        file=open("save_data_party_hire.txt","a")
        for i in client_list:
            for x in range(5): # Uses a nested for loop through the 2 dimensional list to get each values of the list's list 5 items.
                file.write(f"{i[x]}\n")  
        file.close()

    except: # If errors are present, run this instead
        pass # Cannot be empty, otherwise indenting errors will occur



def text_color_update(event): # This function updates the entry titles from red to black IF they're valid
    # Customer name
    if not customer_name_entry.get()=="":
        try:
            test = int(customer_name_entry.get())
        except:
            customer_name_title["fg"]="black"
    # Item_hired
    if not item_hired_entry.get()=="":
        item_hired_title["fg"]="black"
    # Num_item_hired
    try:
        test = int(num_item_hired_entry.get())
        if 0<test<501:
            num_item_hired_title["fg"]="black"
    except:
        pass
   
root.bind("<Return>",delete_row) #The delete row function fires when enter(Return) is pressed
root.bind("<Motion>",text_color_update) # text_color_update runs whenever there is motion detected is the mouse
#Enter Data Button
enter_data_button=Button(root,width="14",text="enter data",font=(("Arial"),14),command=main_function)
enter_data_button.place(x=500,y=310)

root.title("Julie's Party Hire")
root.geometry("1200x800-40+0")
root.mainloop() # Loops the tkinter so it is always running