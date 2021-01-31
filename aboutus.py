from tkinter import  *

class About(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("550x550+500+100")
        self.title("About Us")
        self.resizable(False, False)

        self.top = Frame(self, height=550,width=550, bg='#ffa500')
        self.top.pack(fill=BOTH)

        self.text = Label(self.top, text='This is about us page'
                          '\n this application is made for education purpose'
                          '\n you can contact us on'
                          '\n Email: abdurrouf.cse.cu@gmail.com'
                          '\n Phone: +8801757011158',
                          font = 'aril 14 bold', bg="#ffa500", fg="white")
        self.text.place(x=50, y=50)
