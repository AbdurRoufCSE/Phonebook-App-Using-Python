from tkinter import *
import  datetime
from mypeople import  MyPeople
from addpepole import AddPeople
from aboutus import About
date = datetime.datetime.now().date()
date = str(date)
class Application(object):
    def __init__(self,master):
        self.master = master

        #frames

        self.top = Frame(master, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(master, height=500,bg='#19C1E6')
        self.bottom.pack(fill=X)
        #top frame design
        self.top_image = PhotoImage(file='icons/book.png')
        self.top_image_label = Label(self.top,image=self.top_image)
        self.top_image_label.place(x=130,y=25)

        self.heading = Label(self.top, text='My Phonebook App',
                             font='arial 15 bold', bg='white',fg='#EFCE14')
        self.heading.place(x=240,y=50)

        self.date_lbl = Label(self.top, text="Today's date: "+date, font='arial 12 bold',
                              fg='#EFCE14',bg='white')
        self.date_lbl.place(x=440, y=110)

        #button1 . view people
        self.viewButton = Button(self.bottom, text= "  My People  ",fg='#19C1E6',bg='white', font='arial 12 bold',command=self.my_people)
        self.viewButton.place(x=240,y=70)
        #button 2 - add people
        self.addButton = Button(self.bottom, text=" Add People ",fg='#19C1E6',bg='white', font='arial 12 bold', command=self.addpepolefunction)
        self.addButton.place(x=240, y=130)
        # button 3 - about us
        self.aboutButton = Button(self.bottom, text="   About Us   ", fg='#19C1E6',bg='white',font='arial 12 bold',command = self.about_us)
        self.aboutButton.place(x=240, y=190)

    def my_people(self):
        people=MyPeople()
    def about_us(self):
        aboutpage = About()
    def addpepolefunction(self):
        addpepolewindow = AddPeople()



def main():
    root=Tk()
    app = Application(root)
    root.title("Phonebook App")
    root.geometry("650x550+350+200")
    root.resizable(False, False)
    root.mainloop()

if __name__ == '__main__':
        main()
