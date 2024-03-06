from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Reminder Raccoon')
minutes_working = 0
bad_emotions = ["bad", "grr", "anxious", "sad", "angry"]


def close_popup(mins):
    # print("I am waiting " + str(wait) + " minutes while you " + str(activity))
    # waits "wait" minutes
    global minutes_working
    if mins == 0:
        minutes_working = 0
    else:
        minutes_working += mins
    root.deiconify()
    run_app()


def stay_on_top():
    root.wm_attributes("-topmost", 1)  # app will stay on top of other windows


class OpenMessage:
    def __init__(self, master):
        self.continue_working_button = None
        self.something_else_button = None
        self.something_else_label = None
        self.break_reason_label = None
        self.breathe_button = None
        self.tea_button = None
        self.water_button = None
        self.outside_button = None
        self.walk_button = None
        self.break_label = None
        self.feel_error = None
        self.activity_for_timer = None
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
        self.break_true = False
        self.master = master
        self.minutes_working = minutes_working
        self.main_frame = Frame(self.master)
        self.leave_frame = Frame(self.master)
        self.distracted_frame = Frame(self.master)
        self.timer_frame = Frame(self.master)
        self.break_frame = Frame(self.master)
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
                                  command=lambda: self.feels_checker())
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

    def take_a_break(self, break_text):
        self.break_frame.pack()
        root.geometry("400x200")
        self.break_reason_label = Label(self.break_frame, text=break_text)
        self.break_label = Label(self.break_frame, text="I suggest a 5 minute break, here are some ideas!")
        self.walk_button = Button(self.break_frame, text="Taking a walk", fg="green", command=lambda: self.hide_break_frame())
        self.outside_button = Button(self.break_frame, text="Going outside", fg="pink", command=lambda: self.hide_break_frame())
        self.water_button = Button(self.break_frame, text="Drinking some water", fg="blue", command=lambda: self.hide_break_frame())
        self.tea_button = Button(self.break_frame, text="Making tea", fg="brown", command=lambda: self.hide_break_frame())
        self.breathe_button = Button(self.break_frame, text="Breathing", fg="purple", command=lambda: self.hide_break_frame())
        self.something_else_label = Label(self.break_frame, text="I want to do my own thing -->", padx=0)
        self.something_else_button = Button(self.break_frame, text="just  break", command=lambda: self.hide_break_frame(), padx=0)
        self.continue_working_button = Button(self.break_frame, text="keep working", command= lambda: self.hide_break_but_continue())
        self.break_reason_label.grid(row=1, columnspan=3)
        self.break_label.grid(row=2, columnspan=3)
        self.walk_button.grid(row=3, column=1)
        self.outside_button.grid(row=3, column=3)
        self.water_button.grid(row=4, column=2)
        self.tea_button.grid(row=5, column=1)
        self.breathe_button.grid(row=5, column=3)
        #self.something_else_label.grid(row=6, column=2)
        self.something_else_button.grid(row=6, column=2)
        self.continue_working_button.grid(row=7, column=3)




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

    def feels_checker(self):
        if self.feel_entry.get() == '' and self.feel_error is None:
            self.feel_error = Label(self.main_frame, text="No feeling entered! try again")
            self.feel_error.grid(row=3)
        elif self.feel_entry.get() != '':
            self.hide_main_frame()

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

        # self.master.geometry("+600+250")
        root.geometry("50x50")

        self.timer_frame.pack()
        if self.activity_entry is None:
            self.activity_for_timer = "stay on this webpage"
        else:
            self.activity_for_timer = self.activity_entry.get()
        self.timer_label = Label(self.timer_frame, text=f"{self.minutes}m: {self.secs}s")
        self.timer_label.pack()
        self.countdown()

    def countdown(self):
        count = self.minutes * 60
        count_init = self.minutes * 60
        while count > 0:
            self.minutes, self.secs = divmod(count, 60)
            self.timer_label.config(text=f"{self.minutes}m: {self.secs}s")
            self.timer_label.after(1000, self.timer_label.update())
            # time.sleep(1)
            count -= 1
            if count == count_init - 2:
                root.iconify()
        self.timer_frame.after(950, lambda: self.master.withdraw())
        self.timer_frame.after(950, lambda: self.timer_frame.pack_forget())
        if self.break_true:
            self.timer_frame.after(1000, lambda: close_popup(0))
        else:
            self.timer_frame.after(1000, lambda: close_popup(count_init / 60))

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
        if self.minutes_working >= 180:
            return self.take_a_break("You have been on your computer for 3 hours or more!")
        else:
            self.distracted_frame.pack()
            return self.distracted()

    def hide_break_frame(self):
        self.break_frame.pack_forget()
        self.minutes = 5
        self.break_true = True
        return self.timer_display()

    def hide_break_but_continue(self):
        self.break_frame.pack_forget()
        self.distracted_frame.pack()
        root.geometry("400x100")
        return self.distracted()



def run_app():
    root.geometry("400x100")
    root.geometry("+450+250")
    OpenMessage(root)
    stay_on_top()
    root.mainloop()


run_app()
