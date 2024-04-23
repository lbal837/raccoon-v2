from tkinter import *


class FrameDisplayer:
    def __init__(self, master):
        self.frame = Frame(master)

    def create_label(self, text=""):
        return Label(self.frame, text=text)

    def create_entry_box(self):
        return Entry(self.frame)

    def create_button(self, text="", command=""):
        return Button(self.frame, text=text, command= command)

    def pack(self):
        self.frame.pack()

    def get_frame(self):
        return self.frame

