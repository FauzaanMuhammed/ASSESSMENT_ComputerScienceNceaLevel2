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
file_length=len(saved_list) # Gets file length, so we know how many times we need to loop through it, as well where the extra line is located.
save_file.close() # Closes the save_file

new_saved_list=[] # A new list to contain the new information after changes have been made to the old one.
for i in saved_list:
    new_saved_list.append(i[0:-1]) #This the start to 2nd to last item of the list, and put it onto a new list. This is done, as the normal list includes '\n'(line breaks) at the end, which we don't want

client_list=[]
try: # Attempts load the save file onto the treeview with no errors. 
    for i in range(0,file_length,5): # This function puts 5 of every item into a list, which is put onto a bigger list. The reason multidimensional lists are used are because they allow information to be place in columns and rows better. Each list is a row, and the individul client information ie. Customer Name, are columns. 
        client_list.append([new_saved_list[i],new_saved_list[i+1],new_saved_list[i+2],new_saved_list[i+3],new_saved_list[i+4]])
except: # If the save file cannot be loaded onto the treeview without any errors, clear the list to remove errors.
    save_file = open("save_data_party_hire.txt","w")
    save_file.write("") # Clear save file, otherwise it cannot be opened.
    save_file.close()
    messagebox.showwarning("Data Modified or Corrupted","You save data has been modified/corrupted, and data couldn't be added to the treeview. We've had to clear your data.\n\n Sorry for the inconvinience!")

deletion_instruction_title=Label(root,text="Press the 'Enter' key to delete rows you have clicked. Data is automatically saved",font=(("arial bold"),10))
deletion_instruction_title.place(x=330,y=355) # This tells user instructions on how to the enter key to delete rows
column_list=("row_number","customer_name","receipt_number","item_hired","number_hired") 
treeview = ttk.Treeview(root,columns=column_list,height=11)
treeview.column("#0", width=0) # Hides the unused row
treeview.heading("row_number",text="Row");treeview.column("#1", width=45)
treeview.heading("customer_name",text="Customer Name")# The heading for the treeview.
treeview.heading("receipt_number",text="Receipt Number")
treeview.heading("item_hired",text="Item Hired")
treeview.heading("number_hired",text="Number Hired");treeview.column("#5", width=150) # Fixed widths stop other elements from pushing columns
treeview.place(x=200,y=380)

for i in client_list: # This for loop will insert the client information on each row there is on the list.
    treeview.insert("",tk.END,values=i)
    
treeview_scrollbar = ttk.Scrollbar(root, orient="vertical", command=treeview.yview) # the command will scroll the scrollbar on the treeview in the y axis.
treeview_scrollbar.place(x=979, y=420, height=180)
treeview.configure(yscrollcommand=treeview_scrollbar.set)


def random_receipt_checkbox_action():

    if random_receipt_checked.get()==1: # If checkbox is on
        receipt_number_entry["state"]=DISABLED # if checkbox is on, disabled the receipt_number entry

        random_num_digit_entry.place(x=570,y=282)
        random_receipt_checkbox["text"]="random value(digits)"# Tells users that the entry placed is for the digits

        if receipt_number_entry.get()=="": # If the receipt_number entry is empty
            receipt_number_title["fg"]="black" # -> Display the receipt number title as black, to prevent confusion. 
    else:
        receipt_number_entry["state"]=NORMAL   # otherwise, it is enabled
        random_num_digit_entry.place_forget() # Removes  random_num_digit_entry from view.
        random_receipt_checkbox["text"]="random value" # Puts text back to default.

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
def quit():  # The function for quitting. Works by destroying the tkinter GUI
    root.destroy()

# Help Button
help_button = Button(root,text="❓Help",bg="#3498DB")
help_button.place(x=1145,y=30)
def help_popup():
    messagebox.showinfo("Help","If you enter data and an error shows up, follow the instructions and then enter you data. The color of the text will change from red to black if it is valid.\n\nPress enter to delete rows when you have clicked them. A clicked row will be blue. Once the row is blue then pressing enter will delete that row.\n\nIf you would like to generate a random receipt number, tick the 'random receipt' tickbox and input a number of digits, between 1 and 15.\n\nThe table also has a scrollbar to navigate through the table.\n\nData is automatically saved.")
help_button.configure(command=help_popup) # Makes the help_button put the messagebox out when clicked.
#Customer name title and entry
customer_name_title = Label(root,text="Customer Name",font=(("Arial"),14),width="31") # width=31 Seperates the entries
customer_name_title.grid(column=1,row=1,)                                   # -> So they don't look messy

customer_name_entry = Entry(root,width="25") 
customer_name_entry.grid(column=1,row=2)

#receipt Number title and entry
receipt_number_title = Label(root,text="Receipt Number",font=(("Arial"),14)) # Width=31 is not used, as width covers both
receipt_number_title.grid(column=2,row=1)   
                                                            # To the right and left of the element        
receipt_number_entry = Entry(root,width="25")                # Therefore, it only needs to be used for every odd element
receipt_number_entry.grid(column=2,row=2)

#Random receipt Number Checkbox
random_receipt_checked  = tk.IntVar() # This variable will be 1 when the checkbox is ticked, and 0 when it is off.
random_receipt_checkbox = Checkbutton(root,text="random value",variable=random_receipt_checked,command=random_receipt_checkbox_action,font=(("Arial bold"),12)) # changes the font from default settings to make the text easier to see.
random_receipt_checkbox.grid(column=2,row=3)

# Random receipt number digit entry
random_num_digit_entry = Entry(root,width="3")
random_num_digit_entry.place(x=570,y=282)
random_num_digit_entry.place_forget() # By default, this is disabled, as manual entry is turned on by default.

#Item hired title and entry
item_hired_title = Label(root,text="Item Hired",font=(("Arial"),14),width="33") # 2 more width fills up more area to balance out the entry and make the entries all symmetrical
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
    error_message="" # Sets error message as empty
    customer_name = customer_name_entry.get()
    if random_receipt_checked.get()==1:  # checks if random_receipt check list has been ticked. if so, generate a random number from 100,000 to 999,999 for it. 
        try:
            if int(random_num_digit_entry.get())>15:
                error_message+="Random receipt Digit: Too many digits. Please make this number is in the range of 1-15\n\n"     
            else:
                receipt_number=randint(0.1*10**int(random_num_digit_entry.get()),0.9*10**int(random_num_digit_entry.get()))
        except:
            error_message+="Random receipt Digit: Please put a number from 1-15, and make sure to remove any letters\n\n"
    else:
        receipt_number = receipt_number_entry.get().strip("`~-/ .")   # Otherwise, get the manual entry .strip removes any `,~,/,whitespace and . characters present, which the user may have mistakingly put in

    item_hired = item_hired_entry.get()
    num_item_hired = num_item_hired_entry.get().strip("`~-/ .") 
    try: # The reason try is used instead of type() is because all entry.get values are strings. Because of this, I used try to figure out if they can be converted into a float/int with/without errors depending on the scenario.
        test = float(customer_name)+1 
        customer_name_title["fg"]="red"#-> Since the entry can be converted without any error message, this means customer_name must be a number/float, therefore an error has to be thrownout
        error_message+="Customer name: Please put no numbers\n\n" # Adds a new errors message, and a double line break for neatness

    except:
        if customer_name=="": # customer name cannot be empty, however. So an error must be thrown out.
            customer_name_title["fg"]="red"
            error_message+="Customer Name: Please don't leave empty, you can put anything but numbers\n\n"
        else:
            customer_name_title["fg"]="black" # Sets the text color back to black if no error.
        

    try:
        test=int(receipt_number)+1 #Try adding 1 to the receipt number.
        receipt_number_title["fg"]="black"
        
    except:           
        receipt_number_title["fg"]="red"
        if not random_receipt_checked.get()==1: # If the receipt checkbox is not chcked, and the checbox is empty, give the user an error, as a value must be given for manual receipt
            error_message+="receipt number: Please put any number. Make sure to remove any letters, or tick the tickbox for generating a random receipt.\n\n"

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

        client_list.append([len(client_list)+1,customer_name,receipt_number,item_hired,num_item_hired]) #All information from the entries is appended onto the end of global list
        for i in client_list:
            treeview.insert("",tk.END,values=i) # Adds back client_list onto treeview after it has been reassigned

        # Opening File, clearing it and adding back the treeview contents onto it for saving.
        file = open("save_data_party_hire.txt","w") # Open file in w mode to overwrite text in the txt file,
        file.write("") # Clears save_data_party_hire
        file.close()

        file=open("save_data_party_hire.txt","a") # Opens file again in a mode to append information
        for i in client_list:
            for x in range(5): # Uses a nested for loop through the 2 dimensional list to get each values of the list's list 5 items.
                file.write(f"{i[x]}\n") # write the information with in new line, so each information has it's own line, able to be accessed by .readline() when data is being loaded
        file.close()

    else:
        messagebox.showerror("Error!",error_message) # If errors are present, show the error in a seperate window
  
def delete_row(event): # The Event parameter allows a keyboard press to be binded.

    try: # Prevents errors that would happens if enter is pressed with no treeview
        root.forget(treeview)
        # Getting the information about the selected row, so that row can be deleted when enter is pressed 
        full_selected_list = treeview.item(treeview.focus())
        
        # Deletion of the selected row. 
        row_deleted = full_selected_list["values"][0]
        client_list.pop(row_deleted-1) # Since the row value is 1 greater than it normaly is, we must -1 to normalize the pop function and delete the correct row
        
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

        # Opening File, clearing it and adding back the treeview contents onto it for saving.
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



def text_color_update(event): # This function updates the entry titles from red to black IF they're valid. This will help users to figure if when they've got a correct input

    # Random receipt digit number. checking if the random recipt checbox is on. if so, check if num of digits is 1-15. If so, make text black as it is now valid.
    if random_receipt_checked.get()==1:
        try:
            if 0<int(random_num_digit_entry.get())<16: 
                receipt_number_title["fg"]="black"
        except:
            pass # Prevents errors from being thrown
    # Random receipt -  no checkbox. Just checks if recipt number entry can be converted without errors
    else:
        try:
            int(receipt_number_entry.get())
            receipt_number_title["fg"]="black"
        except:
            pass

    # Customer name -  Checking if it not empty, then if it isn't a integer. If so, make the text valid
    if not customer_name_entry.get()=="":
        try:
            test = int(customer_name_entry.get())
        except:
            customer_name_title["fg"]="black"
    # Item_hired
    if not item_hired_entry.get()=="": # If item_hired_entry.get() is not empty, make it valid.
        item_hired_title["fg"]="black"
    # Num_item_hired
    try:
        test = int(num_item_hired_entry.get())
        if 0<test<501:
            num_item_hired_title["fg"]="black"
    except:
        pass
   
root.bind("<Return>",delete_row) #The delete row function fires when enter(Return) is pressed
root.bind("<Motion>",text_color_update) # text_color_update runs whenever there is motion detected in the mouse
#Enter Data Button
enter_data_button=Button(root,width="14",text="enter data",font=(("Arial"),14),command=main_function)
enter_data_button.place(x=500,y=310)

root.title("Julie's Party Hire")
root.geometry("1200x800-40+0") # 1200X800 window shifted 40X to the left so the window is in the middle of the screen
root.mainloop() # Loops the tkinter so it is always running