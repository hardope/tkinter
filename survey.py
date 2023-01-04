# import kinter module
from tkinter import *

def isint(a):
     try:
          int(a)
          return True
     except:
          return False

def admin(element, element1, window):
     element.place_forget()
     element1.place_forget()

     heading = Label(window, text="Admin Page", font=(25))
     heading.place(x=495, y=15)

def questions(element, element1, window):
     # Remove contents of current page
     element.place_forget()
     element1.place_forget()

     def fetch():
          # Authenticate Input
          if name_field.get() is not None and isint(age.get()):
               with open("raw_data.txt", 'a') as file:
                    file.write(f"Name: {name_field.get()}\n")
                    file.write(f"Age: {age.get()}\n")
                    file.write(f"Sex: {sex.get()}\n")
                    file.write(f"Race: {race.get()}\n")
               a = True
          else:
               pass

     # Label For Name Entry
     heading = Label(window, text="Your Name", font=(20))
     heading.place(x=495, y=15)

     # Name Entry
     name_field = Entry(window, width=35, bd=3, font=(12))
     name_field.place(x=350, y=50)

     # Age Label
     age_label = Label(window, text="Your Age", font=(20))
     age_label.place(x=495, y=100)

     # Age Entry
     age = Entry(window, width=35, bd=3, font=(12))
     age.place(x=350, y=135)

     # Initialize Variable to stroe the users sex
     sex = StringVar()
     sex.set("male")
     
     # Label for sex option
     sex_label = Label(window, text="Sex", font=(20))
     sex_label.place(x=495, y=170)

     # Radio Button to choose Sex
     male = Radiobutton(window, text="Male", variable=sex, value="male")
     female = Radiobutton(window, text="Female", variable=sex, value="female")

     # Place Radio Buttons In view
     male.place(x=400, y=190)
     female.place(x=400, y=210)

     # Label For Race Option
     race_label = Label(window, text="Race", font=(20))
     race_label.place(x=495, y=240)

     # Variable for race options
     race = StringVar()
     race.set("black")

     # Radio buttons To choose race
     black = Radiobutton(window, text="Black", variable=race, value="black")
     white = Radiobutton(window, text="White", variable=race, value="white")
     asian = Radiobutton(window, text="Asian", variable=race, value="asian")
     other = Radiobutton(window, text="Other", variable=race, value="other")

     # Place Race radio buttons in View
     black.place(x=400, y=260)
     white.place(x=400, y=280)
     asian.place(x=400, y=300)
     other.place(x=400, y=320)



     # submit Button
     submit = Button(window, text="Submit", fg="Black", bg="lightblue", command=fetch)
     submit.place(x=500, y=500)

def main():
     # create a GUI window
     window = Tk()

     # set Window Title
     window.title("SculpturSurvey")

     # set the configuration of GUI window
     window.geometry("1000x600")

     host = Button(window, text="Host", width=30, fg="Black", bg="lightblue", command=lambda: admin(host, survey, window))
     survey = Button(window, text="Survey", width=30, fg="Black", bg="lightblue", command=lambda: questions(host, survey, window))

     host.place(x=300, y=50)
     survey.place(x=600, y=50)

     window.mainloop()


# Driver code
if __name__ == "__main__":
     main()