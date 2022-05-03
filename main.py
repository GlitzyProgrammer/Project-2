from Scheduler import *

def main():
    window = Tk()
    window.geometry("300x300")
    window.resizable(False, False)
    window.title("Scheduler")
    remote_widget = schedule_widget(window)
    window.mainloop()





if __name__ == '__main__':
    main()