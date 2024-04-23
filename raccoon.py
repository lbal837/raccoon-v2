from tkinter import *
from FrameDisplayer import FrameDisplayer
from ErrorDisplay import ErrorDisplay

root = Tk()
root.title('Reminder Raccoon')
minutes_working = 0


def stay_on_top():
    root.wm_attributes("-topmost", 1)  # app will stay on top of other windows


class FrameDestroyer:
    def __init__(self, old_frame):
        self.old_frame = old_frame

    def destroy(self):
        self.old_frame.pack_forget()

class DeciderFrame:
    def __init__(self):
        pass


class FeelingsFrame:
    def __init__(self, master):
        self.feelings_display = FrameDisplayer(master)
        self.feelings_destroy = FrameDestroyer(self.feelings_display.get_frame())
        self.feelings_display.pack()
        self.feel_label = self.feelings_display.create_label("How do you feel right now?")
        self.feel_entry = self.feelings_display.create_entry_box()
        self.error_display = ErrorDisplay(self.feelings_display)
        self.feel_button = self.feelings_display.create_button("Enter", self.error)
        self.feelings()

    def feelings(self):
        self.feel_label.grid(row=1, column=0)
        self.feel_entry.grid(row=1, column=1)
        self.feel_button.grid(row=2, columnspan=2)

    def error(self):
        self.error_display.word_checker("No feeling entered!", 3, self.feel_entry.get())

    def kill(self, new_frame):
        self.feelings_destroy.destroy()



def run_app():
    root.geometry("400x100")
    root.geometry("+450+250")
    FeelingsFrame(root)
    stay_on_top()
    root.mainloop()


run_app()
