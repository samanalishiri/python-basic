from tkinter import Tk, Button, LEFT


class FormWithOkButton:
    def __init__(self, frame):
        frame.minsize(100, 100)
        self.frame = frame
        self.buttonOk = Button(frame, text="OK", command=self.button_ok_action, height=1, width=2, compound=LEFT)
        self.buttonOk.place(x=20, y=20)

    def button_ok_action(self):
        print("click!")


frame = Tk()
gui = FormWithOkButton(frame)
frame.mainloop()
