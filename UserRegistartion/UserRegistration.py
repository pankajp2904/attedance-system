# import openpyxl and tkinter modules
import database_proc as db_proc
from tkinter import *
from tkinter import messagebox
def clear():
	# clear the content of text entry box
	name_field.delete(0, END)
	dept_field.delete(0, END)
	Emp_field.delete(0, END)
	contact_no_field.delete(0, END)
	email_id_field.delete(0, END)
	address_field.delete(0, END)


# Function to take data from GUI
# window and write to an excel file
def insert():
	str =Emp_field.get()+"|"+ name_field.get() +"|"+ dept_field.get()+"|" + address_field.get() + "|" + email_id_field.get() + "|" + contact_no_field.get()
	username=db_proc.insert_UserInfo(str)
	messagebox.showinfo("Registartion Success", "Your User Name "+username)
	clear()


# Driver code
if __name__ == "__main__":
	# create a GUI window
	root = Tk()

	# set the background colour of GUI window
	root.configure(background='light green')

	# set the title of GUI window
	root.title("registration form")

	# set the configuration of GUI window
	root.geometry("500x300")

	# create a Form label
	heading = Label(root, text="User Registration", bg="light green")

	# create a Name label
	name = Label(root, text="Name :-", bg="light green")

	# create a Course label
	Dept = Label(root, text="Department :-", bg="light green")

	# create a Semester label
	Emp_ID = Label(root, text="Employee ID      :-", bg="light green")

	# create a Contact No. label
	contact_no = Label(root, text="Contact No.  :-", bg="light green")

	# create a Email id label
	email_id = Label(root, text="Email id :-", bg="light green")

	# create a address label
	address = Label(root, text="Address :-", bg="light green")

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	heading.grid(row=0, column=1)
	name.grid(row=1, column=0)
	Dept.grid(row=2, column=0)
	Emp_ID.grid(row=3, column=0)
	contact_no.grid(row=5, column=0)
	email_id.grid(row=6, column=0)
	address.grid(row=7, column=0)

	# create a text entry box
	# for typing the information
	name_field = Entry(root)
	dept_field = Entry(root)
	Emp_field = Entry(root)
	contact_no_field = Entry(root)
	email_id_field = Entry(root)
	address_field = Entry(root)

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	name_field.grid(row=1, column=1, ipadx="100")
	dept_field.grid(row=2, column=1, ipadx="100")
	Emp_field.grid(row=3, column=1, ipadx="100")
	contact_no_field.grid(row=5, column=1, ipadx="100")
	email_id_field.grid(row=6, column=1, ipadx="100")
	address_field.grid(row=7, column=1, ipadx="100")

	# create a Submit Button and place into the root window
	submit = Button(root, text="Submit", fg="Black",
					bg="Red", command=insert)
	submit.grid(row=8, column=1)

	# start the GUI
	root.mainloop()

