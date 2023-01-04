# import kinter module
from tkinter import *

def questions(element, element1, window):
     element.place_forget()
     element1.place_forget()
     
     # Get Name
     heading = Label(window, text="Your Name", font=(25))
     heading.place(x=495, y=15)

def admin(element, element1, window):
     element.place_forget()
     element1.place_forget()

     heading = Label(window, text="Admin Page", font=(25))
     heading.place(x=495, y=15)

def forget(element):
     element.place_forget()

def main():
     # create a GUI window
     window = Tk()

     # set Window Title
     window.title("SculpturSurvey")

     # set the configuration of GUI window
     window.geometry("1200x600")

     host = Button(window, text="Host", width=30, fg="Black", bg="lightblue", command=lambda: admin(host, survey, window))
     survey = Button(window, text="Survey", width=30, fg="Black", bg="lightblue", command=lambda: questions(host, survey, window))

     host.place(x=300, y=50)
     survey.place(x=600, y=50)

     window.mainloop()


# Driver code
if __name__ == "__main__":
     main()