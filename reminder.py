from tkinter import *
import time

root = Tk()
root.title('Reminder Raccoon')
root.geometry("400x100")


def close_popup():
    time.sleep(3)  # waits 3 seconds, irl should b 15 minutes
    root.deiconify()
    run_app()


class OpenMessage:
    def __init__(self, master):
        self.master = master
        self.mainFrame = Frame(self.master)
        self.leaveFrame = Frame(self.master)
        self.mainFrame.pack()
        self.distracted = Label(self.mainFrame, text="Distracted?")  # see if you can label without name
        self.stay_here = Label(self.mainFrame,
                               text="Do you want to stay on this webpage?")  # see if you can label without name
        self.button1 = Button(self.mainFrame, text="Yes", fg="red", command=self.stay)
        self.button2 = Button(self.mainFrame, text="No", fg="blue", command=self.leave)
        self.distracted.grid(row=0, columnspan=2)
        self.stay_here.grid(row=1, columnspan=2)
        self.button1.grid(row=2)
        self.button2.grid(row=2, column=1)

    def leave(self):
        self.hide_main_frame()
        self.leaveFrame = Frame(self.master)
        self.leaveFrame.pack()
        Label(self.leaveFrame, text="Close this page and get to work!!").pack()
        self.goodbye()

    def stay(self):
        self.hide_main_frame()
        self.leaveFrame.pack()
        Label(self.leaveFrame, text="Great, keep it up!").pack()
        self.goodbye()

    def goodbye(self):
        self.leaveFrame.after(1500, lambda: self.master.withdraw())
        self.leaveFrame.after(1500, lambda: self.leaveFrame.pack_forget())
        self.leaveFrame.after(1500, lambda: close_popup())

    def hide_main_frame(self):
        self.mainFrame.pack_forget()


def run_app():
    OpenMessage(root)
    root.mainloop()


run_app()
