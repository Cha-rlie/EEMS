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
            title="Deactivate EEMS",
            message="Are you sure that you would like to deactive the EEMS and all its protocols? This is an irrevocable process.",
            icon=tk_m.WARNING,
        )
