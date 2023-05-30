# Scene Controller

# Import necessary libraries
import pygame as py
import tkinter_handler
import game_engine_classes

# Start a tkinter_handler instance
tk_handler = tkinter_handler.tk_handler()

# Initialise a Clock instance to keep track of time
clock = py.time.Clock()


class scene_controller:
    def __init__(self):

        # Variable that main.py referneces to know when to stop the game
        self.game_running = True

        # Variable to keep track of the current scene that is being displayed
        self.current_scene = "Main_Menu"

        # Flexible variable that each scene can use to keep running until the scene is over as represented by the variable
        self.current_scene_running = True

        # Initialise the dimensions of the game window (pixels)
        (x, y) = (500, 500)

        # Create a PyGame window
        self.frame = py.display.set_mode([x, y])

        # Change the title of the PyGame window
        py.display.set_caption("EEMS")

        # Load in the EEMS logo and display it as the window icon
        eems_logo_icon = py.image.load("Assets/Original_Art/EEMS-Logo-Small.png")
        py.display.set_icon(eems_logo_icon)

        # Start the first scene
        self.change_scene(just_update=True)
    
    def change_scene(self, scene_called_from="", just_update=False):
        print("change_scene ran")
        print(f"current scene at time of change: {self.current_scene}")
        if self.current_scene != scene_called_from:
            if self.current_scene == "Main_Menu":
                self.main_menu_scene()
            elif self.current_scene == "Play_Game":
                self.play_game_scene()
            elif self.current_scene == "How_It_Works":
                self.how_it_works_scene()
            elif self.current_scene == "About_Us":
                self.about_us_scene()
            elif self.current_scene == "Credits":
                self.credits_scene()
                return None
            #self.current_scene_running = False
        """if just_update == False:
            if self.current_scene != scene_called_from:
                self.current_scene_running = False
            else:
                self.current_scene_running = True"""

    def main_menu_scene(self):
        self.frame.fill("#3D5A80")

        self.current_scene_running = True

        game_engine_classes.draw_text(frame=self.frame, text="E•E•M•S", size=60, x=250, y=50)
        game_engine_classes.draw_text(frame=self.frame, text="Educational Economic Market - Simulated", size=25, x=250, y=100,)

        play_game_button = game_engine_classes.button(frame=self.frame, text="Play Game", size=28, x=250, y=180, on_click="Play_Game")
        how_it_works_button = game_engine_classes.button(frame=self.frame, text="How It Works", size=28, x=250, y=260, on_click="How_It_Works")
        about_us_button = game_engine_classes.button(frame=self.frame, text="About Us", size=28, x=250, y=340, on_click="About_Us")
        credits_button = game_engine_classes.button(frame=self.frame, text="Credits", size=28, x=250, y=420, on_click="Credits")

        while self.current_scene_running:
             # Check for inputs from the player
            for event in py.event.get():
                if event.type == py.QUIT:
                    if tk_handler.check_closing():
                        self.current_scene_running = False
                        self.game_running = False
                else:
                    self.current_scene = play_game_button.click_button(event)
                    self.current_scene = how_it_works_button.click_button(event)
                    self.current_scene = about_us_button.click_button(event)
                    self.current_scene = credits_button.click_button(event)
                    print(f"Before change {self.current_scene}")
                    if self.current_scene == None:
                        self.current_scene = "Main_Menu"
                    else:
                        self.current_scene_running = False
                        self.change_scene(scene_called_from="Main_Menu")

                # Ensures that all devices can run the program at a basic speed of 60fps
                clock.tick(60)

                # Update the window
                py.display.flip()
        
            # Change the scene if necessary
            #self.current_scene_running = self.change_scene(scene_called_from="Main Menu")
    
    def play_scene(self):
        self.frame.fill("#3D5A80")
        print("play_game_scene")

    def how_it_works_scene(self):
        self.frame.fill("#3D5A80")
        print("how_it_works_scene")
    
    def about_us_scene(self):
        self.frame.fill("#3D5A80")
        print("about_us_scene")
    
    def credits_scene(self):
        self.current_scene_running = True
        self.frame.fill("#3D5A80")
        while self.current_scene_running:
            pass
        print("credits_scene")