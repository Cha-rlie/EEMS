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
            elif self.current_scene == "Settings":
                self.settings()
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
        # Fill the window with colour and content
        self.frame.fill("#3D5A80")

        self.current_scene_running = True

        game_engine_classes.draw_text(frame=self.frame, text="E•E•M•S", size=60, x=250, y=50)
        game_engine_classes.draw_text(frame=self.frame, text="Educational Economic Market - Simulated", size=25, x=250, y=100,)

        play_game_button = game_engine_classes.text_button(frame=self.frame, text="Play Game", size=28, x=250, y=180, on_click="Play_Game")
        how_it_works_button = game_engine_classes.text_button(frame=self.frame, text="About Us", size=28, x=250, y=260, on_click="About_Us")
        about_us_button = game_engine_classes.text_button(frame=self.frame, text="Settings", size=28, x=250, y=340, on_click="Settings")
        credits_button = game_engine_classes.text_button(frame=self.frame, text="Credits", size=28, x=250, y=420, on_click="Credits")

        # settings_button = game_engine_classes.image_button(frame=self.frame, image_path="Assets/Icons/Pixel_Settings_Button.png", size=(50,50), x=460, y=40, on_click="Settings")

        while self.current_scene_running:
             # Check for inputs from the player
            for event in py.event.get():
                if event.type == py.QUIT:
                    if tk_handler.check_closing():
                        self.current_scene_running = False
                        self.game_running = False
                else:
                    if play_game_button.click_button(event) != None:
                        self.current_scene = play_game_button.click_button(event)
                    elif how_it_works_button.click_button(event) != None:
                        self.current_scene = how_it_works_button.click_button(event)
                    elif about_us_button.click_button(event) != None:
                        self.current_scene = about_us_button.click_button(event)
                    else:
                        self.current_scene = credits_button.click_button(event)
                    
                    if self.current_scene == None:
                        self.current_scene = "Main_Menu"
                    else:
                        self.current_scene_running = False
                        self.change_scene(scene_called_from="Main_Menu")
                    print(f"Before change {self.current_scene}")

                # Ensures that all devices can run the program at a basic speed of 60fps
                clock.tick(60)

                # Update the window
                py.display.flip()
        
            # Change the scene if necessary
            #self.current_scene_running = self.change_scene(scene_called_from="Main Menu")
    
    def play_game_scene(self):
        self.current_scene_running = True
        self.frame.fill("#3D5A80")

        while self.current_scene_running:
            # Check for imputs from the player
            for event in py.event.get():
                if event.type == py.QUIT:
                    if tk_handler.check_closing():
                        self.current_scene_running = False
                        self.game_running = False

            # Ensures that all devices can run the program at a basic speed of 60fps
            clock.tick(60)

            # Update the window
            py.display.flip()
    
    def about_us_scene(self):
        self.current_scene_running = True
        self.frame.fill("#3D5A80")

        game_engine_classes.draw_text(frame=self.frame, text="About Us", size=60, x=250, y=50)
        game_engine_classes.draw_text(frame=self.frame, text="The Creators: Carlos and Charlie Tarre-Sancier", size=20, x=250, y=110)
        game_engine_classes.draw_text(frame=self.frame, text="Hello reader, we hope this little simulation is enjoyable.", size=17, x=250, y=170)
        game_engine_classes.draw_text(frame=self.frame, text="A lot of hard work, elbow grease (in Photoshop),", size=17, x=250, y=190)
        game_engine_classes.draw_text(frame=self.frame, text="lost sleep (Charlie, sleep more!), skills, and dedication", size=17, x=250, y=210) 
        game_engine_classes.draw_text(frame=self.frame, text="merged together to create this fantastic simulation!,", size=17, x=250, y=230)
        game_engine_classes.draw_text(frame=self.frame, text="Please, nos amis, have fun!", size=17, x=250, y=250)

        back_button = game_engine_classes.image_button(frame=self.frame, image_path="Assets/Icons/Pixel_Back_Button.png", size=(50, 50), x = 50, y=50, on_click="Main_Menu")

        while self.current_scene_running:
             # Check for inputs from the player
            for event in py.event.get():
                if event.type == py.QUIT:
                    if tk_handler.check_closing():
                        self.current_scene_running = False
                        self.game_running = False
                else:
                    if back_button.click_button(event) != None:
                        self.current_scene = back_button.click_button(event)                  
                    if self.current_scene == None:
                        self.current_scene = "About_Us"
                    else:
                        self.current_scene_running = False
                        self.change_scene(scene_called_from="About_Us")
                    print(f"Before change {self.current_scene}")

                # Ensures that all devices can run the program at a basic speed of 60fps
                clock.tick(60)

                # Update the window
                py.display.flip()
            py.display.flip()

    def settings(self):
        self.current_scene_running = True
        self.frame.fill("#3D5A80")

        game_engine_classes.draw_text(frame=self.frame, text="Settings", size=60, x=250, y=50)
        game_engine_classes.draw_text(frame=self.frame, text="Character Colour", size=30, x=250, y=100)
        game_engine_classes.text_button(frame=self.frame, text="Orange", size=28, x=166, y=140)
        game_engine_classes.text_button(frame=self.frame, text="Yellow", size=28, x=333, y=140)
        game_engine_classes.text_button(frame=self.frame, text="Green", size=28, x=166, y=210)
        game_engine_classes.text_button(frame=self.frame, text="Blue", size=28, x=333, y=210)

        back_button = game_engine_classes.image_button(frame=self.frame, image_path="Assets/Icons/Pixel_Back_Button.png", size=(50, 50), x = 50, y=50, on_click="Main_Menu")

        while self.current_scene_running:
             # Check for inputs from the player
            for event in py.event.get():
                if event.type == py.QUIT:
                    if tk_handler.check_closing():
                        self.current_scene_running = False
                        self.game_running = False
                else:
                    if back_button.click_button(event) != None:
                        self.current_scene = back_button.click_button(event)                  
                    if self.current_scene == None:
                        self.current_scene = "Settings"
                    else:
                        self.current_scene_running = False
                        self.change_scene(scene_called_from="Settings")
                    print(f"Before change {self.current_scene}")

                # Ensures that all devices can run the program at a basic speed of 60fps
                clock.tick(60)

                # Update the window
                py.display.flip()
    
    def credits_scene(self):
        # Fill the window with colour and content
        self.current_scene_running = True
        self.frame.fill("#3D5A80")

        game_engine_classes.draw_text(frame=self.frame, text="Credits", size=60, x=250, y=50)
        game_engine_classes.draw_text(frame=self.frame, text="Educational Economic Market - Simulated", size=18, x=250, y=90)
        game_engine_classes.draw_text(frame=self.frame, text="Our School - QASMT", size=22, x=250, y=145)
        game_engine_classes.draw_text(frame=self.frame, text="Our Supervising Mentors - Mr Isaac", size=22, x=250, y=195)
        game_engine_classes.draw_text(frame=self.frame, text="Research Interview -  Mr Altoft", size=22, x=250, y=245)
        game_engine_classes.draw_text(frame=self.frame, text="Feedback Interview - Mr Fredericksen", size=22, x=250, y=295)
        game_engine_classes.draw_text(frame=self.frame, text="Image to Pixel Art - Pixelied.com", size=22, x=250, y=345)
        game_engine_classes.draw_text(frame=self.frame, text="Pixel Art Font - AE Systematic TT (BRK)", size=22, x=250, y=395)
        game_engine_classes.draw_text(frame=self.frame, text="Icons - Icons8.com", size=22, x=250, y=445)

        #game_engine_classes.text_button(frame=self.frame, text="<", size=40, x=20, y=20, on_click="Back")

        back_button = game_engine_classes.image_button(frame=self.frame, image_path="Assets/Icons/Pixel_Back_Button.png", size=(50, 50), x = 50, y=50, on_click="Main_Menu")

        while self.current_scene_running:
             # Check for inputs from the player
            for event in py.event.get():
                if event.type == py.QUIT:
                    if tk_handler.check_closing():
                        self.current_scene_running = False
                        self.game_running = False
                else:
                    if back_button.click_button(event) != None:
                        self.current_scene = back_button.click_button(event)                  
                    if self.current_scene == None:
                        self.current_scene = "Credits"
                    else:
                        self.current_scene_running = False
                        self.change_scene(scene_called_from="Credits")
                    print(f"Before change {self.current_scene}")

                # Ensures that all devices can run the program at a basic speed of 60fps
                clock.tick(60)

                # Update the window
                py.display.flip()