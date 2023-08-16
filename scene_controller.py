# Scene Controller

# Import necessary libraries
import pygame as py
import tkinter_handler

# Import necessary custom libraries
import game_engine_classes
import simulation_handler

# Start the simulation
simulation_handler = simulation_handler.simulation_handler()

# Start a tkinter_handler instance
tk_handler = tkinter_handler.tk_handler()

# Initialise a Clock instance to keep track of time
clock = py.time.Clock()


class scene_controller:
    def __init__(self):

        # Settings Variables
        self.character_colour = "Orange_Pixelated"

        # Variable that main.py referneces to know when to stop the game
        self.pygame_running = True

        self.game_started = False

        # Variable to keep track of the current scene that is being displayed
        self.current_scene = "Main_Menu"

        # Flexible variable that each scene can use to keep running until the scene is over as represented by the variable
        self.current_scene_running = True

        # Initialise the dimensions of the game window (pixels)
        (x, y) = (750, 750)

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
        """print("change_scene ran")
        print(f"current scene at time of change: {self.current_scene}")"""
        if self.current_scene != scene_called_from:
            if self.current_scene == "Main_Menu":
                self.main_menu_scene()
            elif self.current_scene == "Control_Room":
                self.control_room()
            elif self.current_scene == "Teleportation_Room":
                self.teleportation_room()
            elif self.current_scene == "Corporation_Room":
                self.corporation_room()
            elif self.current_scene == "Government_Room":
                self.government_room()
            elif self.current_scene == "Household_Room":
                self.household_room()
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

        game_engine_classes.draw_text(frame=self.frame, text="E•E•M•S", size=90, x=375, y=75)
        game_engine_classes.draw_text(frame=self.frame, text="Educational Economic Market - Simulated", size=38, x=375, y=150)

        play_game_button = game_engine_classes.text_button(frame=self.frame, text="Play Game", size=42, x=375, y=270, on_click="Control_Room")
        how_it_works_button = game_engine_classes.text_button(frame=self.frame, text="About Us", size=42, x=375, y=390, on_click="About_Us")
        about_us_button = game_engine_classes.text_button(frame=self.frame, text="Settings", size=42, x=375, y=510, on_click="Settings")
        credits_button = game_engine_classes.text_button(frame=self.frame, text="Credits", size=42, x=375, y=630, on_click="Credits")

        # settings_button = game_engine_classes.image_button(frame=self.frame, image_path="Assets/Icons/Pixel_Settings_Button.png", size=(50,50), x=460, y=40, on_click="Settings")

        while self.current_scene_running:
             # Check for inputs from the player
            for event in py.event.get():
                if event.type == py.QUIT:
                    if tk_handler.check_closing():
                        self.current_scene_running = False
                        self.pygame_running = False
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

                # Ensures that all devices can run the program at a basic speed of 60fps
                clock.tick(60)

                # Update the window
                py.display.flip()
        
            # Change the scene if necessary
            #self.current_scene_running = self.change_scene(scene_called_from="Main Menu")

    def control_room(self):
        self.current_scene_running = True

        if not self.game_started:

            # CHARACTER OBJECT
            character_path = "Assets/Character/kenney_robot-pack/PNG/" + self.character_colour
            self.character = game_engine_classes.character(frame=self.frame, character_folder_path=character_path, start_x=375, start_y=525)

            # IMPORTANT VARIABLES
            self.teleportation_destination = "Control_Room"

            # RECTS FOR SELECTION BY PLAYER
            # For all the rooms
            self.teleportation_section = py.Rect(20, 580, 713, 100)
            
            # For the Control Room
            self.lineplot_section = py.Rect(132, 102, 122, 118)
            self.piechart_section = py.Rect(336, 80, 204, 116)

            # For the Teleportation Room
            self.teleportation_command_computer_left = py.Rect(45, 328, 230, 168)
            self.teleportation_command_computer_right = py.Rect(472, 330, 230, 168)
            self.teleportation_exit = py.Rect(150, 92, 450, 104)

            self.game_started = True

        while self.current_scene_running:

            self.frame.fill("#3D5A80")

            game_engine_classes.draw_background_image(frame=self.frame, image_path="Assets/Game_Rooms/Control_Room.png")

            main_menu_button = game_engine_classes.image_button(frame=self.frame, image_path="Assets/Icons/Pixel_Home_Button.png", size=(55, 55), x = 37, y=37, on_click="Main_Menu")

             # Check for inputs from the player
            for event in py.event.get():
                if event.type == py.QUIT:
                    if tk_handler.check_closing():
                        self.current_scene_running = False
                        self.game_started = False
                        self.pygame_running = False
                elif event.type == py.MOUSEBUTTONDOWN:
                    print(py.mouse.get_pos())
                elif (event.type == py.KEYDOWN and event.key == py.K_SPACE) or (event.type == py.KEYUP and event.key == py.K_SPACE):
                    if self.character.select_item(self.teleportation_section, event):
                        self.current_scene = "Teleportation_Room"
                        self.change_scene(scene_called_from="Control_Room")
                    elif self.character.select_item(self.lineplot_section, event):
                        simulation_handler.history_of_each_sectors_money_lineplot()
                    elif self.character.select_item(self.piechart_section, event):
                        simulation_handler.percentage_ownership_of_circulating_money_piechart()
                else:
                    if main_menu_button.click_button(event) != None:
                        self.game_started = False
                        self.current_scene = main_menu_button.click_button(event)                  
                    if self.current_scene == None:
                        self.current_scene = "Control_Room"
                    else:
                        self.current_scene_running = False
                        self.change_scene(scene_called_from="Control_Room")

                # Use keystroke information to change the character's new image and position
                self.character.move_character(frame=self.frame, key_state_list=py.key.get_pressed())

                # Draw the character to the screen
                self.character.draw_character(frame=self.frame)

                # Ensures that all devices can run the program at a basic speed of 60fps
                clock.tick(40)

                # Update the window
                py.display.flip()
    
    def teleportation_room(self):
        self.current_scene_running = True

        while self.current_scene_running:

            self.frame.fill("#3D5A80")

            game_engine_classes.draw_background_image(frame=self.frame, image_path="Assets/Game_Rooms/Teleportation_Room.png")

            main_menu_button = game_engine_classes.image_button(frame=self.frame, image_path="Assets/Icons/Pixel_Home_Button.png", size=(55, 55), x = 37, y=37, on_click="Main_Menu")

             # Check for inputs from the player
            for event in py.event.get():
                if event.type == py.QUIT:
                    if tk_handler.check_closing():
                        self.current_scene_running = False
                        self.game_started = False
                        self.pygame_running = False
                elif (event.type == py.KEYDOWN and event.key == py.K_SPACE) or (event.type == py.KEYUP and event.key == py.K_SPACE):
                    if self.character.select_item(self.teleportation_command_computer_left, event) or self.character.select_item(self.teleportation_command_computer_right, event):
                        print("It collided with the robot")
                        self.teleportation_destination = tk_handler.teleportation_destination_selection()
                        if self.teleportation_destination not in ["Control Room", "Corporation Room", "Government Room", "Household Room"]:
                            tk_handler.teleportation_destination_selection_failed()
                            self.teleportation_destination = "Control Room"
                        self.teleportation_destination = self.teleportation_destination.split()[0] + "_" + self.teleportation_destination.split()[1]
                        print(self.teleportation_destination)
                    elif self.character.select_item(self.teleportation_exit, event):
                        print("collided with exit" + self.teleportation_destination)
                        self.current_scene = self.teleportation_destination
                        self.change_scene(scene_called_from="Teleportation_Room")
                else:
                    if main_menu_button.click_button(event) != None:
                        self.game_started = False
                        self.current_scene = main_menu_button.click_button(event)                  
                    if self.current_scene == None:
                        self.current_scene = "Teleportation_Room"
                    else:
                        self.current_scene_running = False
                        self.change_scene(scene_called_from="Teleportation_Room")

                # Use keystroke information to change the character's new image and position
                self.character.move_character(frame=self.frame, key_state_list=py.key.get_pressed())

                # Draw the character to the screen
                self.character.draw_character(frame=self.frame)

                # Ensures that all devices can run the program at a basic speed of 60fps
                clock.tick(40)

                # Update the window
                py.display.flip()

    def corporation_room(self):
        self.current_scene_running = True

        while self.current_scene_running:

            self.frame.fill("#3D5A80")

            game_engine_classes.draw_background_image(frame=self.frame, image_path="Assets/Game_Rooms/Corporation_Room.png")

            main_menu_button = game_engine_classes.image_button(frame=self.frame, image_path="Assets/Icons/Pixel_Home_Button.png", size=(55, 55), x = 37, y=37, on_click="Main_Menu")

             # Check for inputs from the player
            for event in py.event.get():
                if event.type == py.QUIT:
                    if tk_handler.check_closing():
                        self.current_scene_running = False
                        self.game_started = False
                        self.pygame_running = False
                elif (event.type == py.KEYDOWN and event.key == py.K_SPACE) or (event.type == py.KEYUP and event.key == py.K_SPACE):
                    if self.character.select_item(self.teleportation_section, event):
                        self.current_scene = "Teleportation_Room"
                        self.change_scene(scene_called_from="Corporation_Room")
                else:
                    if main_menu_button.click_button(event) != None:
                        self.game_started = False
                        self.current_scene = main_menu_button.click_button(event)                  
                    if self.current_scene == None:
                        self.current_scene = "Corporation_Room"
                    else:
                        self.current_scene_running = False
                        self.change_scene(scene_called_from="Corporation_Room")

                # Use keystroke information to change the character's new image and position
                self.character.move_character(frame=self.frame, key_state_list=py.key.get_pressed())

                # Draw the character to the screen
                self.character.draw_character(frame=self.frame)

                # Ensures that all devices can run the program at a basic speed of 60fps
                clock.tick(40)

                # Update the window
                py.display.flip()

    def government_room(self):
        self.current_scene_running = True

        while self.current_scene_running:

            self.frame.fill("#3D5A80")

            game_engine_classes.draw_background_image(frame=self.frame, image_path="Assets/Game_Rooms/Government_Room.png")

            main_menu_button = game_engine_classes.image_button(frame=self.frame, image_path="Assets/Icons/Pixel_Home_Button.png", size=(55, 55), x = 37, y=37, on_click="Main_Menu")

             # Check for inputs from the player
            for event in py.event.get():
                if event.type == py.QUIT:
                    if tk_handler.check_closing():
                        self.current_scene_running = False
                        self.game_started = False
                        self.pygame_running = False
                elif (event.type == py.KEYDOWN and event.key == py.K_SPACE) or (event.type == py.KEYUP and event.key == py.K_SPACE):
                    if self.character.select_item(self.teleportation_section, event):
                        self.current_scene = "Teleportation_Room"
                        self.change_scene(scene_called_from="Government_Room")
                else:
                    if main_menu_button.click_button(event) != None:
                        self.game_started = False
                        self.current_scene = main_menu_button.click_button(event)                  
                    if self.current_scene == None:
                        self.current_scene = "Government_Room"
                    else:
                        self.current_scene_running = False
                        self.change_scene(scene_called_from="Government_Room")

                # Use keystroke information to change the character's new image and position
                self.character.move_character(frame=self.frame, key_state_list=py.key.get_pressed())

                # Draw the character to the screen
                self.character.draw_character(frame=self.frame)

                # Ensures that all devices can run the program at a basic speed of 60fps
                clock.tick(40)

                # Update the window
                py.display.flip()

    def household_room(self):
        self.current_scene_running

        while self.current_scene_running:

            self.frame.fill("#3D5A80")

            game_engine_classes.draw_background_image(frame=self.frame, image_path="Assets/Game_Rooms/Household_Room.png")

            main_menu_button = game_engine_classes.image_button(frame=self.frame, image_path="Assets/Icons/Pixel_Home_Button.png", size=(55, 55), x = 37, y=37, on_click="Main_Menu")

             # Check for inputs from the player
            for event in py.event.get():
                if event.type == py.QUIT:
                    if tk_handler.check_closing():
                        self.current_scene_running = False
                        self.game_started = False
                        self.pygame_running = False
                elif (event.type == py.KEYDOWN and event.key == py.K_SPACE) or (event.type == py.KEYUP and event.key == py.K_SPACE):
                    if self.character.select_item(self.teleportation_section, event):
                        self.current_scene = "Teleportation_Room"
                        self.change_scene(scene_called_from="Household_Room")
                else:
                    if main_menu_button.click_button(event) != None:
                        self.game_started = False
                        self.current_scene = main_menu_button.click_button(event)                  
                    if self.current_scene == None:
                        self.current_scene = "Household_Room"
                    else:
                        self.current_scene_running = False
                        self.change_scene(scene_called_from="Househole_Room")

                # Use keystroke information to change the character's new image and position
                self.character.move_character(frame=self.frame, key_state_list=py.key.get_pressed())

                # Draw the character to the screen
                self.character.draw_character(frame=self.frame)

                # Ensures that all devices can run the program at a basic speed of 60fps
                clock.tick(40)

                # Update the window
                py.display.flip()

    def about_us_scene(self):
        self.current_scene_running = True
        self.frame.fill("#3D5A80")

        game_engine_classes.draw_text(frame=self.frame, text="About Us", size=90, x=375, y=75)
        game_engine_classes.draw_text(frame=self.frame, text="The Creators: Carlos and Charlie Tarre-Sancier", size=30, x=375, y=165)
        game_engine_classes.draw_text(frame=self.frame, text="Hello reader, we hope this little simulation is enjoyable.", size=26, x=375, y=255)
        game_engine_classes.draw_text(frame=self.frame, text="A lot of hard work, elbow grease (in Photoshop),", size=26, x=375, y=285)
        game_engine_classes.draw_text(frame=self.frame, text="lost sleep (Charlie, sleep more!), skills, and dedication", size=26, x=375, y=315) 
        game_engine_classes.draw_text(frame=self.frame, text="merged together to create this fantastic simulation!,", size=26, x=375, y=345)
        game_engine_classes.draw_text(frame=self.frame, text="Please, nos amis, have fun!", size=26, x=375, y=375)

        back_button = game_engine_classes.image_button(frame=self.frame, image_path="Assets/Icons/Pixel_Back_Button.png", size=(75, 75), x = 75, y=75, on_click="Main_Menu")

        while self.current_scene_running:
             # Check for inputs from the player
            for event in py.event.get():
                if event.type == py.QUIT:
                    if tk_handler.check_closing():
                        self.current_scene_running = False
                        self.pygame_running = False
                else:
                    if back_button.click_button(event) != None:
                        self.current_scene = back_button.click_button(event)                  
                    if self.current_scene == None:
                        self.current_scene = "About_Us"
                    else:
                        self.current_scene_running = False
                        self.change_scene(scene_called_from="About_Us")

                # Ensures that all devices can run the program at a basic speed of 60fps
                clock.tick(60)

                # Update the window
                py.display.flip()

    def settings(self):
        self.current_scene_running = True
        self.frame.fill("#3D5A80")

        game_engine_classes.draw_text(frame=self.frame, text="Settings", size=90, x=375, y=75)
        game_engine_classes.draw_text(frame=self.frame, text="Character Colour", size=45, x=375, y=150)

        orange_colour_settings_button = game_engine_classes.text_button(frame=self.frame, text="Orange", size=42, x=249, y=240, on_click="Character Orange")
        yellow_colour_settings_button = game_engine_classes.text_button(frame=self.frame, text="Yellow", size=42, x=500, y=240, on_click="Character Yellow")
        green_colour_settings_button = game_engine_classes.text_button(frame=self.frame, text="Green", size=42, x=249, y=345, on_click="Character Green")
        blue_colour_settings_button = game_engine_classes.text_button(frame=self.frame, text="Blue", size=42, x=500, y=345, on_click="Character Blue")

        back_button = game_engine_classes.image_button(frame=self.frame, image_path="Assets/Icons/Pixel_Back_Button.png", size=(75, 75), x = 75, y=75, on_click="Main_Menu")

        while self.current_scene_running:
             # Check for inputs from the player
            for event in py.event.get():
                if event.type == py.QUIT:
                    if tk_handler.check_closing():
                        self.current_scene_running = False
                        self.pygame_running = False
                elif str(orange_colour_settings_button.click_button(event)).split(" ")[0] == "Character":
                        self.character_colour = str(orange_colour_settings_button.click_button(event)).split(" ")[1] + "_Pixelated"
                elif str(yellow_colour_settings_button.click_button(event)).split(" ")[0] == "Character":
                        self.character_colour = str(yellow_colour_settings_button.click_button(event)).split(" ")[1] + "_Pixelated"
                elif str(green_colour_settings_button.click_button(event)).split(" ")[0] == "Character":
                        self.character_colour = str(green_colour_settings_button.click_button(event)).split(" ")[1] + "_Pixelated"
                elif str(blue_colour_settings_button.click_button(event)).split(" ")[0] == "Character":
                        self.character_colour = str(blue_colour_settings_button.click_button(event)).split(" ")[1] + "_Pixelated"
                else:
                    if back_button.click_button(event) != None:
                        self.current_scene = back_button.click_button(event)                  
                    if self.current_scene == None:
                        self.current_scene = "Settings"
                    else:
                        self.current_scene_running = False
                        self.change_scene(scene_called_from="Settings")

                # Ensures that all devices can run the program at a basic speed of 60fps
                clock.tick(60)

                # Update the window
                py.display.flip()
    
    def credits_scene(self):
        # Fill the window with colour and content
        self.current_scene_running = True
        self.frame.fill("#3D5A80")

        game_engine_classes.draw_text(frame=self.frame, text="Credits", size=90, x=375, y=75)
        game_engine_classes.draw_text(frame=self.frame, text="Educational Economic Market - Simulated", size=27, x=375, y=135)
        game_engine_classes.draw_text(frame=self.frame, text="Our School - QASMT", size=33, x=375, y=218)
        game_engine_classes.draw_text(frame=self.frame, text="Our Supervising Mentors - Mr Isaac", size=33, x=375, y=293)
        game_engine_classes.draw_text(frame=self.frame, text="Research Interview -  Mr Altoft", size=33, x=375, y=368)
        game_engine_classes.draw_text(frame=self.frame, text="Feedback Interview - Mr Fredericksen", size=33, x=375, y=442)
        game_engine_classes.draw_text(frame=self.frame, text="Image to Pixel Art - Pixelied.com", size=33, x=375, y=518)
        game_engine_classes.draw_text(frame=self.frame, text="Pixel Art Font - AE Systematic TT (BRK)", size=33, x=375, y=593)
        game_engine_classes.draw_text(frame=self.frame, text="Icons - Icons8.com", size=33, x=375, y=668)

        #game_engine_classes.text_button(frame=self.frame, text="<", size=40, x=20, y=20, on_click="Back")

        back_button = game_engine_classes.image_button(frame=self.frame, image_path="Assets/Icons/Pixel_Back_Button.png", size=(75, 75), x = 75, y=75, on_click="Main_Menu")

        while self.current_scene_running:
             # Check for inputs from the player
            for event in py.event.get():
                if event.type == py.QUIT:
                    if tk_handler.check_closing():
                        self.current_scene_running = False
                        self.pygame_running = False
                else:
                    if back_button.click_button(event) != None:
                        self.current_scene = back_button.click_button(event)                  
                    if self.current_scene == None:
                        self.current_scene = "Credits"
                    else:
                        self.current_scene_running = False
                        self.change_scene(scene_called_from="Credits")

                # Ensures that all devices can run the program at a basic speed of 60fps
                clock.tick(60)

                # Update the window
                py.display.flip()