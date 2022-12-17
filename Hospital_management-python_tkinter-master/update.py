#armaan 2110994755
from tkinter import *
import tkinter.messagebox   #importing librariries such as messagebox used for displaying messages
import sqlite3
from PIL import ImageTk,Image #ImageTk module contains support to create and modify Tkinter BitmapImage and PhotoImage objects from
#PIL images used everywhere Tkinter expects an image object
conn = sqlite3.connect('database1.db')
c = conn.cursor()
#this file is created so that the user can update the data in accordance to their need if they feel it needs to be edited
class Application:
    def __init__(self, master):
        self.master = master
        self.image=ImageTk.PhotoImage(Image.open("hospital5.jpg"))
        self.panel=Label(master,image=self.image)
        self.panel.pack()
        self.heading = Label(master, text="Update Appointments",  fg='steelblue', font=('arial 40 bold'))
        self.heading.place(x=150, y=0)

        self.name = Label(master, text="Enter Patient's Name", font=('arial 18 bold'))
        self.name.place(x=0, y=80)

        self.namenet = Entry(master, width=30,bd=3) #user inputs the name to search for the data base
        self.namenet.place(x=280, y=80)
#search button enables the searching of the data base in accordance to the name 
        self.search = Button(master, text="Search", width=12, height=1, bg='steelblue',bd=3,command=self.search_db)
        self.search.place(x=330, y=120)


    def search_db(self):
        self.input = self.namenet.get()  #taking the user input for the name by the patient

        sql = "SELECT * FROM appointment WHERE name LIKE ?" #select sql query used and stored in the sql variable
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.name1 = self.row[1]
            self.age = self.row[2]
            self.gender = self.row[3]
            self.address = self.row[4]
            self.phone = self.row[5]
            self.time = self.row[6]
#label used for displaying the name, age gender etc when the patient searches 
        self.uname = Label(self.master, text="Patient's Name", font=('arial 18 bold'))
        self.uname.place(x=0, y=150)

        self.uage = Label(self.master, text="Age", font=('arial 18 bold'))
        self.uage.place(x=0, y=190)

        self.ugender = Label(self.master, text="Gender", font=('arial 18 bold'))
        self.ugender.place(x=0, y=230)

        self.uaddress = Label(self.master, text="Address", font=('arial 18 bold'))
        self.uaddress.place(x=0, y=270)

        self.uphone = Label(self.master, text="Phone Number", font=('arial 18 bold'))
        self.uphone.place(x=0, y=310)

        self.utime = Label(self.master, text="Appointment time", font=('arial 18 bold'))
        self.utime.place(x=0, y=350)

   
        self.ent1 = Entry(self.master, width=30,bd=3)
        self.ent1.place(x=300, y=150)
        self.ent1.insert(END, str(self.name1))

        self.ent2 = Entry(self.master, width=30,bd=3)
        self.ent2.place(x=300, y=190)
        self.ent2.insert(END, str(self.age))

        self.ent3 = Entry(self.master, width=30,bd=3)
        self.ent3.place(x=300, y=230)
        self.ent3.insert(END, str(self.gender))

        self.ent4 = Entry(self.master, width=30,bd=3)
        self.ent4.place(x=300, y=270)
        self.ent4.insert(END, str(self.address))

        self.ent5 = Entry(self.master, width=30,bd=3)
        self.ent5.place(x=300, y=310)
        self.ent5.insert(END, str(self.phone))

        self.ent6 = Entry(self.master, width=30,bd=3)
        self.ent6.place(x=300, y=350)
        self.ent6.insert(END, str(self.time))

        self.update = Button(self.master, text="Update", width=20, height=2, bg='lightblue',bd=3, command=self.update_db)
        self.update.place(x=400, y=390)

        self.delete = Button(self.master, text="Delete", width=20, height=2, bg='red',bd=3, command=self.delete_db)
        self.delete.place(x=150, y=390)
    def update_db(self): #this method takes in the user input and uses the update sql query to update the data by the user

        self.var1 = self.ent1.get()
        self.var2 = self.ent2.get() 
        self.var3 = self.ent3.get() 
        self.var4 = self.ent4.get()  
        self.var5 = self.ent5.get() 
        self.var6 = self.ent6.get() 
#update query used fro name, age , gender etc
        query = "UPDATE appointment SET name=?, age=?, gender=?, address=?, phone=?, time=? WHERE name LIKE ?"
        c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var5, self.var6, self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Updated", "Successfully Updated.")
    def delete_db(self): #method uses the delete query and executes it 
        sql2 = "DELETE FROM appointment WHERE name LIKE ?"
        c.execute(sql2, (self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Deleted Successfully")
        self.ent1.destroy()
        self.ent2.destroy()
        self.ent3.destroy()
        self.ent4.destroy()
        self.ent5.destroy()
        self.ent6.destroy()

root = Tk()
b = Application(root)
root.geometry("800x500+0+0")
root.resizable(False, False)
root.mainloop()
