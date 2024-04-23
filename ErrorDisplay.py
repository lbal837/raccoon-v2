class ErrorDisplay:
    def __init__(self, frame):
        self.frame_display = frame
        self.error_message = None

    def word_checker(self, message, row, entry):
        if entry == '' and self.error_message is None:
            self.error_message = self.frame_display.create_label(message)
            self.error_message.grid(row=row)
        elif entry != '':
            print("here!")

    def num_checker(self):
        pass