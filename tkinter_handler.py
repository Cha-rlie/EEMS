# tkinter_handler

# Import the necessary libraries
import tkinter as tk
import tkinter.messagebox as tk_m


class tk_handler:
    def __init__(self):
        pass

    def check_closing(self):

        main = tk.Tk()
        main.destroy()

        return tk_m.askokcancel(
            title="Quit",
            message="Are you sure that you would like to close this application?",
            icon=tk_m.WARNING,
        )
