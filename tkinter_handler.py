# tkinter_handler

# Import the necessary libraries
import tkinter as tk
import tkinter.messagebox as tk_m
from tkinter import ttk
from PIL import Image, ImageTk
import math


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

        main.possible_destinations = [
            "Control Room",
            "Corporation Room",
            "Government Room",
            "Household Room",
        ]
        main.destination = tk.StringVar(main)
        # destination.set("Choose a Destination")

        dropdown = ttk.OptionMenu(
            main, main.destination, "Choose a Destination", *main.possible_destinations
        )
        dropdown.pack()

        ttk.Button(main, text="Set Destination", command=lambda: self.end(main)).pack()

        while self.main_running:
            main.mainloop()

        return main.destination.get()

    def teleportation_destination_selection_failed(self):
        main = tk.Tk()
        main.destroy()

        return tk_m.showerror(
            "Teleportation Error",
            "You did not select a destination, so it was defaulted to the Control Room.",
        )

    def corporations_command_centre(
        self, original_values, current_money, total_positive_circulating_money
    ):
        self.main_running = True

        main = tk.Tk()
        main.geometry("400x260")
        main.title("Corporation Sector Command Centre")

        ttk.Label(
            main, text=f"Corporation Sector's Current Money: ${current_money}"
        ).pack()
        ttk.Label(
            main,
            text=f"Corporation Sector's Economy Ownership Percentage: {math.ceil(current_money/total_positive_circulating_money)*100}%",
        ).pack()

        main.hiring_value = tk.DoubleVar()
        hiring_label = ttk.Label(main, text=f"Hiring Attitude: {main.hiring_value.get()}")
        hiring_label.pack()
        def update_hiring_label(something):
            hiring_label.config(text=f"Hiring Attitude: {round(main.hiring_value.get(), 2)}")
        hiring_slider = ttk.Scale(
            main, from_=0, to=1, orient=tk.HORIZONTAL, variable=main.hiring_value, command=update_hiring_label
        )
        hiring_slider.set(original_values[0])
        hiring_slider.pack()

        main.salary_value = tk.DoubleVar()
        salary_label = ttk.Label(main, text=f"Salary: ${main.salary_value.get()}")
        salary_label.pack()
        def update_salary_label(something):
            salary_label.config(text=f"Salary: ${round(main.salary_value.get(), 2)}")
        salary_slider = ttk.Scale(
            main, from_=0, to=1000, orient=tk.HORIZONTAL, variable=main.salary_value, command=update_salary_label
        )
        salary_slider.set(original_values[1])
        salary_slider.pack()

        main.trading_value = tk.DoubleVar()
        trading_label = ttk.Label(main, text=f"Trading Attitude: {main.trading_value.get()}")
        trading_label.pack()
        def update_trading_label(something):
            trading_label.config(text=f"Trading Attitude: {round(main.trading_value.get(), 2)}")
        trading_slider = ttk.Scale(
            main, from_=0, to=1, orient="horizontal", variable=main.trading_value, command=update_trading_label
        )
        trading_slider.set(original_values[2])
        trading_slider.pack()

        ttk.Button(main, text="Apply", command=lambda: self.end(main)).pack()

        while self.main_running:
            main.mainloop()

        return [main.hiring_value.get(), main.salary_value.get(), main.trading_value.get()]

    def government_control_centre(self, original_values, current_money, total_positive_circulating_money):
        self.main_running = True

        main = tk.Tk()
        main.geometry("400x260")
        main.title("Government Sector Command Centre")

        ttk.Label(
            main, text=f"Government Sector's Current Money: ${current_money}"
        ).pack()
        ttk.Label(
            main,
            text=f"Government Sector's Economy Ownership Percentage: {math.ceil(current_money/total_positive_circulating_money)*100}%",
        ).pack()

        main.printing_rate_value = tk.DoubleVar()
        printing_rate_label = ttk.Label(main, text=f"Printing Rate: {main.printing_rate_value.get()}")
        printing_rate_label.pack()
        def update_printing_rate_label(something):
            printing_rate_label.config(text=f"Printing Rate: {round(main.printing_rate_value.get(), 2)}")
        printing_rate_slider = ttk.Scale(
            main, from_=0, to=1, orient=tk.HORIZONTAL, variable=main.printing_rate_value, command=update_printing_rate_label
        )
        printing_rate_slider.set(original_values[0])
        printing_rate_slider.pack()

        main.gov_spending_value = tk.DoubleVar()
        gov_spending_label = ttk.Label(main, text=f"Government Spending Rate: {main.gov_spending_value.get()}")
        gov_spending_label.pack()
        def update_gov_spending_label(something):
            gov_spending_label.config(text=f"Government Spending Rate: {round(main.gov_spending_value.get(), 2)}")
        gov_spending_slider = ttk.Scale(
            main, from_=0, to=1, orient=tk.HORIZONTAL, variable=main.gov_spending_value, command=update_gov_spending_label
        )
        gov_spending_slider.set(original_values[1])
        gov_spending_slider.pack()

        main.tax_rate_value = tk.DoubleVar()
        tax_rate_label = ttk.Label(main, text=f"Tax Rate: {main.tax_rate_value.get()}")
        tax_rate_label.pack()
        def update_tax_rate_label(something):
            tax_rate_label.config(text=f"Tax Rate: {round(main.tax_rate_value.get(), 2)}")
        tax_rate_slider = ttk.Scale(
            main, from_=0, to=1, orient="horizontal", variable=main.tax_rate_value, command=update_tax_rate_label
        )
        tax_rate_slider.set(original_values[2])
        tax_rate_slider.pack()

        ttk.Button(main, text="Apply", command=lambda: self.end(main)).pack()

        while self.main_running:
            main.mainloop()

        return [main.printing_rate_value.get(), main.gov_spending_value.get(), main.tax_rate_value.get()]

    def household_control_centre(self, original_values, current_money, total_positive_circulating_money):
        self.main_running = True

        main = tk.Tk()
        main.geometry("400x300")
        main.title("Households' Sector Command Centre")

        ttk.Label(
            main, text=f"Households' Sector's Current Money: ${current_money}"
        ).pack()
        ttk.Label(
            main,
            text=f"Households' Sector's Economy Ownership Percentage: {math.ceil(current_money/total_positive_circulating_money)*100}%",
        ).pack()

        main.buying_attitude_value = tk.DoubleVar()
        buying_attitude_label = ttk.Label(main, text=f"Buying Attitude: {main.buying_attitude_value.get()}")
        buying_attitude_label.pack()
        def update_buying_attitude_label(something):
            buying_attitude_label.config(text=f"Buying Attitude: {round(main.buying_attitude_value.get(), 2)}")
        buying_attitude_slider = ttk.Scale(
            main, from_=0, to=1, orient=tk.HORIZONTAL, variable=main.buying_attitude_value, command=update_buying_attitude_label
        )
        buying_attitude_slider.set(original_values[0])
        buying_attitude_slider.pack()

        main.working_attitude_value = tk.DoubleVar()
        working_attitude_label = ttk.Label(main, text=f"Working Attitude: {main.working_attitude_value.get()}")
        working_attitude_label.pack()
        def update_working_attitude_label(something):
            working_attitude_label.config(text=f"Working Attitude: {round(main.working_attitude_value.get(), 2)}")
        working_attitude_slider = ttk.Scale(main, from_=0, to=1, orient=tk.HORIZONTAL, variable=main.working_attitude_value, command=update_working_attitude_label
        )
        working_attitude_slider.set(original_values[1])
        working_attitude_slider.pack()

        main.saving_rate_value = tk.DoubleVar()
        saving_rate_label = ttk.Label(main, text=f"Saving Rate: {main.saving_rate_value.get()}")
        saving_rate_label.pack()
        def update_saving_rate_label(something):
            saving_rate_label.config(text=f"Saving Rate: {round(main.saving_rate_value.get(), 2)}")
        saving_rate_slider = ttk.Scale(
            main, from_=0, to=1, orient="horizontal", variable=main.saving_rate_value, command=update_saving_rate_label
        )
        saving_rate_slider.set(original_values[2])
        saving_rate_slider.pack()

        main.foreign_trading_attitude_value = tk.DoubleVar()
        foreign_trading_attitude_label = ttk.Label(main, text=f"Foreign Trading Rate Attitude: {main.foreign_trading_attitude_value.get()}")
        foreign_trading_attitude_label.pack()
        def update_foreign_trading_attitude_label(something):
            foreign_trading_attitude_label.config(text=f"Foreign Trading Rate Attitude: {round(main.foreign_trading_attitude_value.get(), 2)}")
        foreign_trading_attitude_slider = ttk.Scale(
            main, from_=0, to=1, orient="horizontal", variable=main.foreign_trading_attitude_value, command=update_foreign_trading_attitude_label
        )
        foreign_trading_attitude_slider.set(original_values[3])
        foreign_trading_attitude_slider.pack()

        ttk.Button(main, text="Apply", command=lambda: self.end(main)).pack()

        while self.main_running:
            main.mainloop()

        return [main.buying_attitude_value.get(), main.working_attitude_value.get(), main.saving_rate_value.get(), main.foreign_trading_attitude_value.get()]


    def end(self, main):
        main.destroy()
        self.main_running = False
