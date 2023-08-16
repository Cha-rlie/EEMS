# tkinter_handler

# Import the necessary libraries
import tkinter as tk
import tkinter.messagebox as tk_m
from tkinter import ttk
from PIL import Image, ImageTk


class tk_handler:
    def __init__(self):
        self.main_running = False

    def check_closing(self):

        main = tk.Tk()
        main.destroy()

        return tk_m.askokcancel(
            title="Deactivate EEMS",
            message="Are you sure that you would like to deactive the EEMS and all its protocols? This is an irrevocable process.",
            icon=tk_m.WARNING,
        )

    def teleportation_destination_selection(self):
        
        self.main_running = True

        main = tk.Tk()

        main.geometry("320x80")

        main.title("Teleporter Control Panel")

        ttk.Label(main, text="Please choose the destination to set the teleporter to:")

        main.possible_destinations = ["Control Room", "Corporation Room", "Government Room", "Household Room"]
        main.destination = tk.StringVar(main)
        #destination.set("Choose a Destination")

        dropdown = ttk.OptionMenu(main, main.destination, "Choose a Destination", *main.possible_destinations)
        dropdown.pack()

        ttk.Button(main, text="Set Destination", command=lambda: self.end(main)).pack()

        while self.main_running:
            main.mainloop()
        
        return main.destination.get()
    
    def teleportation_destination_selection_failed(self):
        main = tk.Tk()
        main.destroy()

        return tk_m.showerror("Teleportation Error","You did not select a destination, so it was defaulted to the Control Room.")

    def end(self, main):
        main.destroy()
        self.main_running = False