from tkinter import *
import time
from tkinter import ttk

root = Tk()
root.title('Reminder Raccoon')
root.geometry("400x100")


def close_popup():
    # print("I am waiting " + str(wait) + " minutes while you " + str(activity))
    # waits "wait" minutes
    root.deiconify()
    run_app()


class OpenMessage:
    def __init__(self, master):
        self.timer_label = None
        self.button2 = None
        self.button1 = None
        self.stay_here = None
        self.distracted_label = None
        self.feel_button = None
        self.feel_entry = None
        self.feel_label = None
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
        self.distracted_frame = Frame(self.master)
        self.timer_frame = Frame(self.master)
        self.minutes = 00
        self.secs = 00
        self.feelings()

    def feelings(self):
        self.main_frame.pack()
        self.feel_label = Label(self.main_frame, text="How do you feel right now?")
        self.feel_entry = Entry(self.main_frame)
        self.feel_label.grid(row=1, column=0)
        self.feel_entry.grid(row=1, column=1)
        self.feel_button = Button(self.main_frame, text="Enter", fg="red",
                                  command=lambda: self.hide_main_frame())
        self.feel_button.grid(row=2, columnspan=2)

    def distracted(self):
        feel_text = "you feel " + self.feel_entry.get()
        self.distracted_label = Label(self.distracted_frame, text=feel_text)  # see if you can label without name
        self.stay_here = Label(self.distracted_frame,
                               text="Do you want to stay on this webpage?")  # see if you can label without name
        self.button1 = Button(self.distracted_frame, text="Yes", fg="red",
                              command=lambda: self.hide_distracted_frame(self.stay()))
        self.button2 = Button(self.distracted_frame, text="No", fg="blue",
                              command=lambda: self.hide_distracted_frame(self.leave()))
        self.distracted_label.grid(row=0, columnspan=2)
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
                                       values=[1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
                                       )
        task_button = Button(self.leave_frame, text="Enter", fg="red", command=lambda: self.time_checker())
        self.time_entry.grid(row=1, column=0)
        task_button.grid(row=1, column=1)

    def time_checker(self):
        if self.time_entry.get() == '':
            Label(self.leave_frame, text="no time entered! try again").grid(row=2)
        else:
            self.minutes = int(self.time_entry.get())
            self.goodbye(1)

    def activity_checker(self):
        if self.activity_entry.get() == '' and self.activity_error is None:
            self.activity_error = Label(self.leave_frame, text="no activity entered! try again")
            self.activity_error.grid(row=3)
        elif self.activity_entry.get() != '':
            t = "how long would you like to " + self.activity_entry.get() + " for?(minutes)"
            self.hide_leave_frame(self.stay(t))

    def goodbye(self, buffer=1500):
        # self.leave_frame.after(buffer, lambda: self.master.withdraw())
        self.leave_frame.after(buffer, lambda: self.leave_frame.pack_forget())
        # if self.activity_entry is not None:
        # self.leave_frame.after(buffer, lambda: close_popup(wait, self.activity_entry.get()))
        # else:
        # self.leave_frame.after(buffer, lambda: close_popup(wait))
        self.leave_frame.after(buffer, lambda: self.timer_display())

    def timer_display(self):
        self.timer_frame.pack()
        self.timer_label = Label(self.timer_frame, text=f"Time Left: {self.minutes}: {self.secs}")
        self.timer_label.pack()
        self.countdown()

    def countdown(self):
        count = self.minutes * 60
        while count > 0:
            self.minutes, self.secs = divmod(count, 60)
            self.timer_label.config(text=f"Time Left: {self.minutes}: {self.secs}")
            self.timer_label.update()
            time.sleep(1)
            count -= 1
        self.timer_frame.after(1000, lambda: self.master.withdraw())
        self.timer_frame.after(1000, lambda: self.timer_frame.pack_forget())
        self.timer_frame.after(1000, lambda: close_popup())

    def hide_leave_frame(self, function):
        self.activity.grid_forget()
        self.activity_entry.grid_forget()
        self.activity_button.grid_forget()
        self.close_webpage.grid_forget()
        if self.activity_error is not None:
            self.activity_error.grid_forget()
        return function

    def hide_distracted_frame(self, function):
        self.distracted_frame.pack_forget()
        self.leave_frame.pack()
        return function

    def hide_main_frame(self):
        self.main_frame.pack_forget()
        self.distracted_frame.pack()
        return self.distracted()


def run_app():
    OpenMessage(root)
    root.mainloop()


run_app()
