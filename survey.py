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
                    file.write(f"Ethnicity: {ethnicity.get()}\n")
                    file.write(f"01: {question1.get()}\n")
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

     # Label For ethnicity Option
     ethnicity_label = Label(window, text="Ethnicity", font=(20))
     ethnicity_label.place(x=495, y=240)

     # Variable for ethnicity options
     ethnicity = StringVar()
     ethnicity.set("black")

     # Radio buttons To choose ethnicity
     black = Radiobutton(window, text="Black", variable=ethnicity, value="black")
     white = Radiobutton(window, text="White", variable=ethnicity, value="white")
     asian = Radiobutton(window, text="Asian", variable=ethnicity, value="asian")
     other = Radiobutton(window, text="Other", variable=ethnicity, value="other")

     # Place ethnicity radio buttons in View
     black.place(x=400, y=260)
     white.place(x=400, y=280)
     asian.place(x=400, y=300)
     other.place(x=400, y=320)

     # Question1: Did You Enjoy The sculpture
     question1_label = Label(window, text="Did You Enjoy The sculpture", font=(20))
     question1_label.place(x=430, y=340)

     # Variable for ethnicity options
     question1 = StringVar()
     question1.set("agree")

     # Radio buttons To choose ethnicity
     q1_sa = Radiobutton(window, text="Strongly Agree", variable=question1, value="strongly agree")
     q1_a = Radiobutton(window, text="Agree", variable=question1, value="agree")
     q1_nad = Radiobutton(window, text="Neither Agree Nor Disagree", variable=question1, value="neutral")
     q1_d = Radiobutton(window, text="Disagree", variable=question1, value="disagree")
     q1_sd = Radiobutton(window, text="Strongly Disagree", variable=question1, value="strongly disagree")

     # Place ethnicity radio buttons in View
     q1_sa.place(x=400, y=370)
     q1_a.place(x=400, y=390)
     q1_nad.place(x=400, y=410)
     q1_d.place(x=400, y=430)
     q1_sd.place(x=400, y=450)



     # submit Button
     submit = Button(window, text="Submit", fg="Black", bg="lightblue", command=fetch)
     submit.place(x=500, y=600)

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