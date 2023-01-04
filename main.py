# import kinter module
from tkinter import *

def save():
	
	...

# Function to set focus (cursor)
def focus1(event):
	# set focus on the course_field box
	course_field.focus_set()

# Function for clearing the
# contents of text entry boxes
def clear():
	
	# clear the content of text entry box
	name_field.delete(0, END)
	course_field.delete(0, END)


# Function to take data from GUI
# window and write to an excel file
def insert():
	
	# if user not fill any entry
	# then print "empty input"
	if (name_field.get() == "" and course_field.get() == ""):
		print("empty input")

	else:
          print(f"Name: {name_field.get()}")
          print(f"Age: {course_field.get()}")

          # set focus on the name_field box
          name_field.focus_set()

          # call the clear() function
          clear()

# Driver code
if __name__ == "__main__":
	
     # create a GUI window
     root = Tk()

     # set the background colour of GUI window
     root.configure(background='white')

     # set the title of GUI window
     root.title("SculpturSurvey")

     # set min-size
     root.minsize(width=400, height=200)

     # set the configuration of GUI window
     root.geometry("1200x600")

     # create a Form label
     heading = Label(root, text="Form", bg="white", font=("calibri", 25))

     # create a Name label
     name = Label(root, text="Name", bg="white", font=("calibri", 15))

     # create a Course label
     course = Label(root, text="Age", bg="white", font=("calibri", 15))

     # grid method is used for placing
     # the widgets at respective positions
     # in table like structure .
     heading.place(x=495, y=15)
     name.place(x=500, y=70)
     course.place(x=505, y=170)

     # create a text entry box
     # for typing the information
     name_field = Entry(root, width=35, bd=3, font=("calibri", 12))
     course_field = Entry(root, width=35, bd=3, font=("calibri", 12))
     submit = Button(root, text="Submit", fg="Black", bg="lightblue", command=insert)

     # bind method of widget is used for
     # the binding the function with the events

     # whenever the enter key is pressed
     # then call the focus1 function
     name_field.bind("<Return>", focus1)

     # Place Elements
     name_field.place(x=400, y=110)
     course_field.place(x=400, y=200)
     submit.place(x=530, y=280)

     # start the GUI
     root.mainloop()
