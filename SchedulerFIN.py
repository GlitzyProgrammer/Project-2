#Orginal Idea was from a phone app I have that keeps track of stuff I do: Googe Calendar
#I have added an interactive gui, a delete functoin in the application,
# Project link https://github.com/GlitzyProgrammer/Project-2

from tkinter import *
import Calendar_Data as Calendar

class schedule_widget:
    """
    This class is used to create the object scheduluar
    """

    def __init__(self,window):
        """
        this intializes all the widgets that the class calls upon for it's functionality
        :param window:
        """
        month = ""
        year = ""
        day = ""
        event = ""
        self.window = window
        self.Hello = Label(window,text='Welcome to the schedule program!\nDo you want to modify a schedule?',font=('Times New Roman',14))
        self.ExampleText = Label(window,text='Example of what to input in the text boxes.\nMay\n31\n2023\nEating with Sally')
        self.Entry = Entry(window)
        self.FoundLabel = Label(window,text=f'We found the date Month:{month}\nDay:{day}\nYear:{year}\nEvent:{event}')
        self.YesButton = Button(window,text='YES',command=self.yesoption, font=('Times New Roman',14))
        self.NoButton = Button(window, text='NO',command=self.no_option, font=('Times New Roman',14))
        self.SearchInstruction = Label(window, text='To find or delete your event just\nenter Month,Day,Year',font=('Times New Roman',10))
        self.DeleteButton = Button(window, text='DELETE',command=self.delete_command, font=('Times New Roman',14))
        self.SearchSubmit = Button(window,command=self.data_search, text= 'Submit')
        self.QuitButton = Button(window,text= 'Quit',command=window.destroy, font=('Times New Roman',14))
        self.Instruction = Label(window, text='Enter a Month, Day, Year, Event', font=('Times New Roman',12))
        self.MonthLabel = Label(window,text='Month',font=('Times New Roman', 12))
        self.MonthEntry = Entry(window,font=('Times New Roman',12))
        self.DayLabel = Label(window, text='Day',font=('Times New Roman',12))
        self.DayEntry = Entry(window, font=('Times New Roman', 12))
        self.YearLabel = Label(window, text='Year', font=('Times New Roman', 12))
        self.YearEntry = Entry(window, font=('Times New Roman', 12))
        self.EventLabel = Label(window, text='Event',font=('Times New Roman',12))
        self.EventEntry = Entry(window, font=('Times New Roman', 12))
        self.SubmitButton = Button(window, text='Sumbit',command=self.dataRetrival, font=('Times New Roman',12) )
        self.ErrorMessage = Label(window, text='The data you submitted was invalid\nclick the back button to view the instructions')
        self.BackButton = Button(window,command=self.backwards, text='BACK',font=('Times New Roman',12))
        self.SearchButton = Button(window, text='SEARCH',font=('Times New Roman',12))
        self.YesButton.grid(row=1,column=0)
        self.NoButton.grid(row=2,column=0)
        self.Hello.grid(row=0,column=0)
        self.ExampleText.grid(row=3,column=0)
        self.QuitButton.grid(row=4,column=0)


    def yesoption(self):
        """
        Method used to move the user to the page that does the scheduling
        :return:
        """
        self.NoButton.grid_remove()
        self.YesButton.grid_remove()
        self.Hello.grid_remove()
        self.ExampleText.grid_remove()
        self.QuitButton.grid_remove()
        self.Instruction.grid(row=0,column=0)
        self.MonthLabel.grid(row=1,column=0)
        self.MonthEntry.grid(row=1,column=1)
        self.DayLabel.grid(row=2,column=0)
        self.DayEntry.grid(row=2,column=1)
        self.YearLabel.grid(row=3,column=0)
        self.YearEntry.grid(row=3,column=1)
        self.EventLabel.grid(row=4,column=0)
        self.EventEntry.grid(row=4,column=1)
        self.SubmitButton.grid(row=5,column=0)
        self.QuitButton.grid(row=6,column=0)
        self.BackButton.grid(row=7, column=0)

    def dataRetrival(self):
        """
        This method retreives the data from the entry widgets and checks if the data is valid
        then adds it to the file 'Schedule_Book.txt' only if it passes the tests
        :return:
        """
        month = self.MonthEntry.get().lower().strip()
        day = self.DayEntry.get().strip()
        year= self.YearEntry.get().strip()
        event = self.EventEntry.get()
        try:
            if year.isdigit():
                year = int(year)
                if year <= 9999:
                    year = str(year)
                else:
                    raise ValueError
            else:
                raise ValueError

            if not (month.isdigit()):
                if month in Calendar.month:
                    month = month
                else:
                    raise ValueError
            else:
                raise ValueError
            if day.isdigit():
                day = int(day)
                if day <= 31 and day > 0:
                    day = str(day)
                else:
                    raise ValueError
            else:
                raise ValueError
            if not (event.isdigit()):
                event = event
            else:
                raise ValueError
        except ValueError:
            self.ErrorMessage.grid(row=6,column=0)
            self.BackButton.grid(row=7,column=0)
        with open("Schedule_Book.txt", 'a', newline='') as file:
            file.writelines([month,day,year,event,'\n'])
            self.EventEntry.delete(0, END)
            self.MonthEntry.delete(0, END)
            self.DayEntry.delete(0, END)
            self.YearEntry.delete(0, END)

    def backwards(self):
        """
        This method activates when the back button is clicked and takes the user back to the main screen
        :return:
        """
        self.DayEntry.delete(0,END)
        self.YearEntry.delete(0,END)
        self.EventEntry.delete(0,END)
        self.MonthEntry.delete(0,END)
        self.DayLabel.grid_remove()
        self.DayEntry.grid_remove()
        self.YearEntry.grid_remove()
        self.YearLabel.grid_remove()
        self.MonthEntry.grid_remove()
        self.MonthLabel.grid_remove()
        self.Instruction.grid_remove()
        self.EventEntry.grid_remove()
        self.EventLabel.grid_remove()
        self.BackButton.grid_remove()
        self.ErrorMessage.grid_remove()
        self.SearchSubmit.grid_remove()
        self.QuitButton.grid_remove()
        self.DeleteButton.grid_remove()
        self.SearchInstruction.grid_remove()
        self.SearchButton.grid_remove()
        self.SubmitButton.grid_remove()
        self.NoButton.grid()
        self.YesButton.grid()
        self.Hello.grid()
        self.ExampleText.grid()
        self.QuitButton.grid()

    def no_option(self):
        """
        This method takes the user dirrectly to the search page
        :return:
        """
        self.Instruction.grid_remove()
        self.Hello.grid_remove()
        self.ExampleText.grid_remove()
        self.NoButton.grid_remove()
        self.YesButton.grid_remove()
        self.SearchInstruction.grid(row=1,column=0)
        self.MonthLabel.grid(row=2, column=0)
        self.MonthEntry.grid(row=2, column=1)
        self.DayLabel.grid(row=3, column=0)
        self.DayEntry.grid(row=3, column=1)
        self.YearLabel.grid(row=4, column=0)
        self.YearEntry.grid(row=4, column=1)
        self.SearchSubmit.grid(row=5,column=0)
        self.QuitButton.grid(row=6,column=0)
        self.BackButton.grid(row=7, column=0)
        self.FoundLabel.grid(row=7, column=1)
        self.DeleteButton.grid(row=8, column=0)
        self.SearchButton.grid(row=9, column= 0)
        self.FoundLabel.grid_remove()

    def data_search(self):
        month = self.MonthEntry.get().lower().strip()
        day = self.DayEntry.get().strip()
        year = self.YearEntry.get().strip()
        try:
            if year.isdigit():
                year = int(year)
                if year <= 9999:
                    year = str(year)

                else:
                    raise ValueError
            else:
                raise ValueError

            if not (month.isdigit()):
                if month in Calendar.month:
                    month = month
                else:
                    raise ValueError
            else:
                raise ValueError
            if day.isdigit():
                day = int(day)
                if day <= 31 and day > 0:
                    day = str(day)
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            self.ErrorMessage.grid(row=6,column=0)
            self.BackButton.grid(row=7,column=0)
        with open("Schedule_Book.txt", 'r', newline='') as file:
            reference = month+day+year
            self.MonthEntry.delete(0, END)
            self.DayEntry.delete(0, END)
            self.YearEntry.delete(0, END)
            occurance = 0
            for line in file:
                if  reference in line.strip('\n'):
                    self.FoundLabel.grid()
                    break
                # TODO: Make a label that does display the month,day,event,year variables





    def delete_command(self):
        """
        This is like the data_search method but this time it removes the item when contitionds are fufilled.
        :return:
        """
        month = self.MonthEntry.get().lower().strip()
        day = self.DayEntry.get().strip()
        year = self.YearEntry.get().strip()
        try:
            if year.isdigit():
                year = int(year)
                if year <= 9999:
                    year = str(year)

                else:
                    raise ValueError
            else:
                raise ValueError

            if not (month.isdigit()):
                if month in Calendar.month:
                    month = month
                else:
                    raise ValueError
            else:
                raise ValueError
            if day.isdigit():
                day = int(day)
                if day <= 31 and day > 0:
                    day = str(day)
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            self.ErrorMessage.grid(row=6, column=0)
            self.BackButton.grid(row=7, column=0)
        with open("Schedule_Book.txt", 'r', newline='') as file:
            lines = file.readlines()
            reference = month + day + year
            self.MonthEntry.delete(0, END)
            self.DayEntry.delete(0, END)
            self.YearEntry.delete(0, END)
        with open("Schedule_Book.txt", 'w', newline='') as file:
            for line in lines:
                if not (reference in line.strip('\n')):
                  file.write(line)


                    #for line in file:
                # TODO: Eventaully reduce time compelxedity cause it's currently O(n) (fine but better exsit)
               #  TODO: Figure out how to detete the item and doesn't leave a blank line
             #   if line.strip("\n") != reference:
              #       file.write("")
                # TODO: Make a label that does display the month,day,event,year variables
