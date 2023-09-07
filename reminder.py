from tkinter import *
import time
from tkinter import ttk

root = Tk()
root.title('Reminder Raccoon')
root.geometry("400x100")


def close_popup(wait):
    print("I am waiting " + str(wait) + " minutes")
    time.sleep(wait)  # waits "wait" minutes
    root.deiconify()
    run_app()


class OpenMessage:
    def __init__(self, master):
        self.activity_error = None
        self.activity_button = None
        self.activity = None
        self.activity_entry = None
        self.webpage = IntVar(value=0)
        self.close_webpage = None
        self.time_entry = None
        self.master = master
        self.main_frame = Frame(self.master)
        self.leave_frame = Frame(self.master)
        self.main_frame.pack()
        self.distracted = Label(self.main_frame, text="Distracted?")  # see if you can label without name
        self.stay_here = Label(self.main_frame,
                               text="Do you want to stay on this webpage?")  # see if you can label without name
        self.button1 = Button(self.main_frame, text="Yes", fg="red", command=lambda: self.hide_main_frame(self.stay()))
        self.button2 = Button(self.main_frame, text="No", fg="blue", command=lambda: self.hide_main_frame(self.leave()))
        self.distracted.grid(row=0, columnspan=2)
        self.stay_here.grid(row=1, columnspan=2)
        self.button1.grid(row=2)
        self.button2.grid(row=2, column=1)

    def leave(self):
        t = "Close the webpage you are on"
        self.close_webpage = Checkbutton(self.leave_frame, variable=self.webpage, text=t, command=lambda: self.close())
        self.close_webpage.grid(row=0, columnspan=2)

    def close(self):
        self.close_webpage.config(state=DISABLED)
        self.activity = Label(self.leave_frame, text="What would you like to do now?")  # make text space bigger
        self.activity_entry = Entry(self.leave_frame)
        self.activity.grid(row=1, column=0)
        self.activity_entry.grid(row=1, column=1)
        self.activity_button = Button(self.leave_frame, text="Enter", fg="red",
                                      command=lambda: self.activity_checker())
        self.activity_button.grid(row=2, columnspan=2)

    def stay(self, t="Great, how much longer would you like to stay on this page?(minutes)"):
        Label(self.leave_frame, text=t).grid(row=0,
                                             columnspan=2)
        self.time_entry = ttk.Combobox(self.leave_frame,
                                       state="readonly",
                                       values=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
                                       )
        task_button = Button(self.leave_frame, text="Enter", fg="red", command=lambda: self.time_checker())
        self.time_entry.grid(row=1, column=0)
        task_button.grid(row=1, column=1)

    def time_checker(self):
        if self.time_entry.get() == '':
            Label(self.leave_frame, text="no time entered! try again").grid(row=2)
        else:
            self.goodbye(1, int(self.time_entry.get()))

    def activity_checker(self):
        if self.activity_entry.get() == '' and self.activity_error is None:
            self.activity_error = Label(self.leave_frame, text="no activity entered! try again")
            self.activity_error.grid(row=3)
        elif self.activity_entry.get() != '':
            t = "how long would you like to " + self.activity_entry.get() + " for?(minutes)"
            self.hide_leave_frame(self.stay(t))

    def goodbye(self, buffer=1500, wait=15):
        self.leave_frame.after(buffer, lambda: self.master.withdraw())
        self.leave_frame.after(buffer, lambda: self.leave_frame.pack_forget())
        self.leave_frame.after(buffer, lambda: close_popup(wait))

    def hide_leave_frame(self, function):
        self.activity.grid_forget()
        self.activity_entry.grid_forget()
        self.activity_button.grid_forget()
        self.close_webpage.grid_forget()
        if self.activity_error is not None:
            self.activity_error.grid_forget()
        return function

    def hide_main_frame(self, function):
        self.main_frame.pack_forget()
        self.leave_frame.pack()
        return function


def run_app():
    OpenMessage(root)
    root.mainloop()


run_app()
