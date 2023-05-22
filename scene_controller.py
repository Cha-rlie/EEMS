# Scene Controller

# Import necessary libraries
import pygame as py
import tkinter_handler
import simple_rendering_functions

# Start a tkinter_handler instance
tk_handler = tkinter_handler.tk_handler()

# Start a simple_rendering_functions instance
simple_render_functions = simple_rendering_functions.simple_functions()

# Initialise a Clock instance to keep track of time
clock = py.time.Clock()


class scene_controller:
    def __init__(self):
        self.current_scene = "Main_Menu"

        # Variable to loop the game to play infinitely until the user clicks on the cross
        self.game_running = True

        # Initialise the dimensions of the game window (pixels)
        (x, y) = (500, 500)

        # Create a PyGame window
        self.frame = py.display.set_mode([x, y])

        # Change the title of the PyGame window
        py.display.set_caption("EEMS")

    def basic_necessities_for_scenes(self):
        # Check for inputs from the player
        for event in py.event.get():
            if event.type == py.QUIT:
                if tk_handler.check_closing():
                    self.game_running = False
        # Update the window
        py.display.flip()

        # Ensures that all devices can run the program at a basic speed of 60 fps
        clock.tick(60)

    def main_menu_scene(self):
        self.basic_necessities_for_scenes()
        self.frame.fill("#3D5A80")

        simple_render_functions.draw_text(
            frame=self.frame, text="E•E•M•S", size=60, x=250, y=50
        )
        simple_render_functions.draw_text(
            frame=self.frame,
            text="Educational Economic Market - Simulated",
            size=25,
            x=250,
            y=100,
        )

        about_us_button = simple_rendering_functions.button(
            frame=self.frame, text="About us", size=25, x=250, y=175
        )
