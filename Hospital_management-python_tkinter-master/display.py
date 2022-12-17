#armaan 2110994755
from tkinter import * #importing librariries for using sql and images 
import sqlite3
import pyttsx3
from PIL import ImageTk,Image
conn = sqlite3.connect('database1.db') #establishing connection with the data base using .connect method
c = conn.cursor()

number = []
patients = []

sql = "SELECT * FROM appointment" #running the sql query with command select
res = c.execute(sql) #using execute method to execute the sql query
for r in res:
    ids = r[0]
    name = r[1]
    number.append(ids)
    patients.append(name)

class Application: #application class created
    def __init__(self, master): #"__init__" is a reseved method in python classes.
        #It is known as a constructor in object oriented concepts. 
        #This method called when an object is created from the class and it allow the class to initialize the attributes of a class.
        self.master = master
        self.image=ImageTk.PhotoImage(Image.open("hospital6.jpg")) #using the image for display
        self.panel=Label(master,image=self.image)
        self.panel.pack()
        self.x = 0
#using the widgtes such as label and button to create the display
        self.heading = Label(master, text="Appointments", font=('arial 60 bold'), fg='green')
        self.heading.place(x=150, y=0)

        self.change = Button(master, text="Next Patient", width=25, height=2, bg='steelblue', command=self.func)
        self.change.place(x=350, y=450)

        self.n = Label(master, text="", font=('arial 80 bold'))
        self.n.place(x=200, y=200)

        self.pname = Label(master, text="", font=('arial 80 bold'))
        self.pname.place(x=300, y=200)
    
    def func(self):
        self.n.config(text=str(number[self.x]))
        self.pname.config(text=str(patients[self.x]))
        self.x += 1
root = Tk()
b = Application(root)
root.geometry("800x520+0+0")
root.resizable(False, False)
root.mainloop()
