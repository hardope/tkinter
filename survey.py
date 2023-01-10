# import kinter module
from tkinter import *
import sys

def isint(a):
     try:
          int(a)
          return True
     except:
          return False

def admin(heading, element, element2, element1, window):
     element.place_forget()
     element1.place_forget()
     element2.place_forget()
     heading.place_forget()

     adminhead = Label(window, text="Admin Page", font=(25))
     adminhead.place(x=495, y=15)
     
     with open("raw_data.txt", 'r') as file:
          data = file.read()
     data = data.split("\n")
     data.pop(0)
     data.pop()
     head = "NAME    AGE   SEX     ETHNICITY    Q1    Q2    Q3"
     thead = Label(window, text=head, font=(20))
     thead.place(x=200, y=80)
     new_data = []
     y = 120
     for i in data:
          val = Label(window, text=i.replace(" : ", "    "), font=5)
          val.place(x=200, y=y)
          y+=40
          new_data.append(i.replace(" : ", "    "))
     print(new_data)

def questions(heading, element, element2, element1, window):
     # Remove contents of current page
     heading.place_forget()
     element.place_forget()
     element1.place_forget()
     element2.place_forget()

     def fetch():
          # Authenticate Input
          if name_field.get() is not None and isint(age.get()):
               with open("raw_data.txt", 'a') as file:
                    file.write(f"{name_field.get()} : {age.get()} : {sex.get()} : {ethnicity.get()} : {question1.get()} : {question2.get()} : {question3.get()}\n")
                    sys.exit()
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
     age = Entry(window, width=20, bd=3, font=(12))
     age.place(x=440, y=150)

     # Initialize Variable to stroe the users sex
     sex = StringVar()
     sex.set("male")
     
     # Label for sex option
     sex_label = Label(window, text="Sex", font=(20))
     sex_label.place(x=50, y=190)

     # Radio Button to choose Sex
     male = Radiobutton(window, text="Male", variable=sex, value="male")
     female = Radiobutton(window, text="Female", variable=sex, value="female")

     # Place Radio Buttons In view
     male.place(x=50, y=220)
     female.place(x=50, y=240)

     # Label For ethnicity Option
     ethnicity_label = Label(window, text="Ethnicity", font=(20))
     ethnicity_label.place(x=50, y=270)

     # Variable for ethnicity options
     ethnicity = StringVar()
     ethnicity.set("black")

     # Radio buttons To choose ethnicity
     black = Radiobutton(window, text="Black", variable=ethnicity, value="black")
     white = Radiobutton(window, text="White", variable=ethnicity, value="white")
     asian = Radiobutton(window, text="Asian", variable=ethnicity, value="asian")
     other = Radiobutton(window, text="Other", variable=ethnicity, value="other")

     # Place ethnicity radio buttons in View
     black.place(x=50, y=300)
     white.place(x=50, y=320)
     asian.place(x=50, y=340)
     other.place(x=50, y=360)

     # Question1: Did You Enjoy The sculpture
     question1_label = Label(window, text="Did You Enjoy The sculpture", font=(20))
     question1_label.place(x=50, y=390)

     # Variable for question 1 options
     question1 = StringVar()
     question1.set("agree")

     # Radio buttons To choose answer for question 1
     q1_sa = Radiobutton(window, text="Strongly Agree", variable=question1, value="strongly agree")
     q1_a = Radiobutton(window, text="Agree", variable=question1, value="agree")
     q1_nad = Radiobutton(window, text="Neither Agree Nor Disagree", variable=question1, value="neutral")
     q1_d = Radiobutton(window, text="Disagree", variable=question1, value="disagree")
     q1_sd = Radiobutton(window, text="Strongly Disagree", variable=question1, value="strongly disagree")

     # Place Question 1 radio buttons in View
     q1_sa.place(x=50, y=420)
     q1_a.place(x=50, y=440)
     q1_nad.place(x=50, y=460)
     q1_d.place(x=50, y=480)
     q1_sd.place(x=50, y=500)

     
     # Question2: Are you curious About How The sculpture Works
     question2_label = Label(window, text="Are you curious About How The sculpture Works", font=(20))
     question2_label.place(x=550, y=190)

     # Variable for question 2 options
     question2 = StringVar()
     question2.set("agree")

     # Radio buttons To choose answer for question 2
     q2_sa = Radiobutton(window, text="Strongly Agree", variable=question2, value="strongly agree")
     q2_a = Radiobutton(window, text="Agree", variable=question2, value="agree")
     q2_nad = Radiobutton(window, text="Neither Agree Nor Disagree", variable=question2, value="neutral")
     q2_d = Radiobutton(window, text="Disagree", variable=question2, value="disagree")
     q2_sd = Radiobutton(window, text="Strongly Disagree", variable=question2, value="strongly disagree")

     # Place Question 2 radio buttons in View
     q2_sa.place(x=550, y=220)
     q2_a.place(x=550, y=240)
     q2_nad.place(x=550, y=260)
     q2_d.place(x=550, y=280)
     q2_sd.place(x=550, y=300)


     # Question2: Are More Interested Science As A result Of This Sculpture
     question3_label = Label(window, text="Are More Interested Science As A result Of This Sculpture", font=(20))
     question3_label.place(x=550, y=340)

     # Variable for question 3 options
     question3 = StringVar()
     question3.set("agree")

     # Radio buttons To choose answer for question 1
     q3_sa = Radiobutton(window, text="Strongly Agree", variable=question3, value="strongly agree")
     q3_a = Radiobutton(window, text="Agree", variable=question3, value="agree")
     q3_nad = Radiobutton(window, text="Neither Agree Nor Disagree", variable=question3, value="neutral")
     q3_d = Radiobutton(window, text="Disagree", variable=question3, value="disagree")
     q3_sd = Radiobutton(window, text="Strongly Disagree", variable=question3, value="strongly disagree")

     # Place Question 1 radio buttons in View
     q3_sa.place(x=550, y=370)
     q3_a.place(x=550, y=390)
     q3_nad.place(x=550, y=410)
     q3_d.place(x=550, y=430)
     q3_sd.place(x=550, y=450)


     # submit Button
     submit = Button(window, text="Submit", fg="Black", bg="lightblue", command=fetch)
     submit.place(x=500, y=550)

def main():
     # create a GUI window
     window = Tk()

     # set Window Title
     window.title("SculpturSurvey")

     # set the configuration of GUI window
     window.geometry("1000x600")

     class ScrollableFrame:
          """A scrollable tkinter frame that will fill the whole window"""

          def __init__ (self, master, width, height, mousescroll=0):
               self.mousescroll = mousescroll
               self.master = master
               self.height = height
               self.width = width
               self.main_frame = Frame(self.master)
               self.main_frame.pack(fill=BOTH, expand=1)

               self.scrollbar = Scrollbar(self.main_frame, orient=VERTICAL)
               self.scrollbar.pack(side=RIGHT, fill=Y)

               self.canvas = Canvas(self.main_frame, yscrollcommand=self.scrollbar.set)
               self.canvas.pack(expand=True, fill=BOTH)

               self.scrollbar.config(command=self.canvas.yview)

               self.canvas.bind(
                    '<Configure>',
                    lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
               )

               self.frame = Frame(self.canvas, width=self.width, height=self.height)
               self.frame.pack(expand=True, fill=BOTH)
               self.canvas.create_window((0,0), window=self.frame, anchor="nw")

               self.frame.bind("<Enter>", self.entered)
               self.frame.bind("<Leave>", self.left)

          def _on_mouse_wheel(self,event):
               self.canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

          def entered(self,event):
               if self.mousescroll:
                    self.canvas.bind_all("<MouseWheel>", self._on_mouse_wheel)
               
          def left(self,event):
               if self.mousescroll:
                    self.canvas.unbind_all("<MouseWheel>")

     # Example usage

     obj = ScrollableFrame(
          window,
          height=10000, # Total required height of canvas
          width=1500 # Total width of master
     )

     objframe = obj.frame
     bgimg= tk.PhotoImage(file = "Tulips.ppm")
     
     limg= Label(objframe, i=bgimg)
     limg.pack()
          
     def auth():
          # Authenticate Input
          if host.get() is not None and host.get() == "adminpassword":
               admin(heading, host, survey, submit, objframe)
          else:
               pass

     heading = Label(window, text="Log In To Admin Page", font=(25))
     heading.place(x=410, y=90)

     host = Entry(window, width=35, bd=3)
     host.place(x=410, y=150)

     survey = Button(window, text="Take Survey", width=30, fg="Black", bg="lightblue", command=lambda: questions(heading, host, survey, submit, objframe))
     survey.place(x=400, y=50)

     submit = Button(window, text="Submit", fg="Black", bg="lightblue", command=auth)
     submit.place(x=500, y=200)

     window.mainloop()


# Driver code
if __name__ == "__main__":
     main()
