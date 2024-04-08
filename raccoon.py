import tkinter as tk
import tkinter as ttk


class FrameController(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # create a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        dependencies = Dependencies()
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # initialise frames into empty array
        self.frames = {}
        for F in (Feelings, Distracted):
            frame = F(container, self, dependencies)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Feelings)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Dependencies:
    def __init__(self):
        self.feelings = ""

    def set_feeling(self, feeling):
        self.feelings = feeling

    def get_feeling(self):
        return self.feelings


class Distracted(tk.Frame):
    def __init__(self, parent, controller, d):
        tk.Frame.__init__(self, parent)
        if d.get_feeling():
            feel_text = "you feel " + d.get_feeling()
        else:
            feel_text = "error"
        self.distracted_label = ttk.Label(self, text=feel_text)  # see if you can label without name
        self.stay_here = ttk.Label(self,
                                   text="Do you want to stay on this webpage?")  # see if you can label without name
        self.button1 = ttk.Button(self, text="Yes", fg="red", command="")
        self.button2 = ttk.Button(self, text="No", fg="blue", command="")
        self.distracted_label.grid(row=0, columnspan=2)
        self.stay_here.grid(row=1, columnspan=2)
        self.button1.grid(row=2)
        self.button2.grid(row=2, column=1)


class Feelings(tk.Frame):
    def __init__(self, parent, controller, d):
        tk.Frame.__init__(self, parent)
        self.feel_error = None
        self.controller = controller
        self.d = d
        self.feel_label = ttk.Label(self, text="How do you feel right now?")
        self.feel_entry = ttk.Entry(self)
        self.feel_label.grid(row=1, column=0)
        self.feel_entry.grid(row=1, column=1)
        self.feel_button = ttk.Button(self, text="Enter", fg="red", command=lambda: self.feels_checker())
        self.feel_button.grid(row=2, columnspan=2)

    def feels_checker(self):
        if self.feel_entry.get() == '' and self.feel_error is None:
            self.feel_error = ttk.Label(self, text="No feeling entered! try again")
            self.feel_error.grid(row=3)

        elif self.feel_entry.get() != '':
            self.d.set_feeling(self.feel_entry.get())
            self.controller.show_frame(Distracted)


# Driver Code
app = FrameController()
app.mainloop()
