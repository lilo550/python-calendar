from tkinter import*
from calendar import*

class Calender:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('250x240')
        self.window.title("Calender")

        # Component initialization
        self.frame =  Frame(self.window)

        # Creation of components
        self.labels()
        self.frame.pack(pady=20)
        self.entry()
        self.buttons()

    def labels(self):
        label_title = Label(self.window, text="Calendar", font=('Courrier', 26))
        label_title.pack()
        label_entry_title = Label(self.frame, text="Enter year", font=('Courrier', 16))
        label_entry_title.pack()

    def entry(self):
        self.year = IntVar()
        year_entry = Entry(self.frame, text=self.year, font=('Courrier', 14), width=13)
        year_entry.pack()

    def buttons(self):
        show_calender_button = Button(self.frame, text="Show calender", width=13, font=('Courrier', 14), command=self.show_calender)
        show_calender_button.pack(pady=5)
        exit_button = Button(self.frame, text="Exit", font=('Courrier', 14), width=13, command=self.window.quit)
        exit_button.pack(pady=5)

    def show_calender(self):
        calender = calendar(self.year.get())
        calender_window = Tk()
        calender_window.title("Calender for the year " + str(self.year.get())
        calender_label = Label(calender_window, text=calender, font=('Courrier', 16), relief='solid')
        calender_label.pack()

# Display
c = Calender()
c.window.mainloop()
