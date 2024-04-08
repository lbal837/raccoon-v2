import tkinter as tk


class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Raccoon")

        self.feelings_window = FeelingsWindow()
        self.distracted_window = DistractedWindow()

    def show_feelings_window(self):
        if self.distracted_window:
            self.distracted_window.destroy()
        self.distracted_window = FeelingsWindow(self, self.s)

    def show_distracted_window(self):

class DistractedWindow:
    pass


class FeelingsWindow:
    pass
