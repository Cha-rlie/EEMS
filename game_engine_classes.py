# Simple Rednering PyGame Functions

# Import necessary classes
import pygame as py

def draw_text(frame, text, size, x, y, colour="#EE6C4D", font="Assets/Font/aesymatt.ttf"):
    font_obj = py.font.Font(font, size)

    text_surface = font_obj.render(text, False, colour)

    text_rect = text_surface.get_rect()

    text_rect.center = (x, y)

    frame.blit(text_surface, text_rect)


class text_button:
    def __init__(
        self,
        frame,
        text,
        size,
        x,
        y,
        on_click="Button Clicked!",
        primary_colour="#EE6C4D",
        secondary_colour="#3D5A80",
        font="Assets/Font/aesymatt.ttf"
    ):
        self.x, self.y = (x, y)
        self.text_colour = primary_colour
        self.background_colour = secondary_colour
        self.font_obj = py.font.Font(font, size)
        self.on_click = on_click
        self.alter_button(frame, text)

    def alter_button(self, frame, text):

        # Make a text surface with the button's text
        text_obj = self.font_obj.render(text, False, self.text_colour)
        
        # Make a surface that will have the button's background colour
        self.button_surface = py.Surface(text_obj.get_size())
        self.button_surface.fill(self.background_colour)

        # Make an invisible rectangle that will check for clicks in its area 
        self.button_click_rect = self.button_surface.get_rect()
        self.button_click_rect.center = (self.x, self.y)

        # Make a rounded rectangle that will act as the button's border
        py.draw.rect(frame, self.text_colour, self.button_click_rect.inflate(12,12), 3, border_radius=10)
        #py.draw.rect(surface=frame, color=self.text_colour, rect=self.button_click_rect, width=1)

        # Attach the text to the button's surface and then to the frame
        self.button_surface.blit(text_obj, (0,0))
        frame.blit(self.button_surface, self.button_click_rect)

    def click_button(self, event):
        mouse_x, mouse_y = py.mouse.get_pos()
        if event.type == py.MOUSEBUTTONDOWN:
            if py.mouse.get_pressed()[0]:
                if self.button_click_rect.collidepoint(mouse_x, mouse_y):
                    return self.on_click
        return None
    
class draw_background_image():
    def __init__(self, frame, image_path):
        
        # Load the image in
        image = py.image.load(image_path)

        # Resize the image
        resized_image = py.transform.scale(image, (750,750))

        # Put this onto the frame
        frame.blit(resized_image, (0,0))

class image_button():
    def __init__(
        self,
        frame,
        image_path,
        size,
        x,
        y,
        on_click="Button Clicked!",
    ):
        self.x, self.y = (x, y)
        self.on_click = on_click
        self.size = size
        self.alter_button(frame, image_path)
    
    def alter_button(self, frame, image_path):
        # Load the image in
        image = py.image.load(image_path)#.convert_alpha()

        # Remove the background of the image
        # image.set_colorkey((0,0,0))

        # Resize the image
        resized_image = py.transform.scale(image, self.size)

        # Put the image onto a surface
        # self.button_surface = py.Surface(resized_image.get_size())

        # Attach the image onto the button surface
        #frame.blit(resized_image, (0,0))

        # Create an invisible rectangle where clicks will be measured
        self.button_click_rect = py.Surface(resized_image.get_size()).get_rect()
        self.button_click_rect.center = (self.x, self.y)

        # Put this all onto the frame for the user to interact with
        frame.blit(resized_image, self.button_click_rect)

    def click_button(self, event):
        mouse_x, mouse_y = py.mouse.get_pos()
        if event.type == py.MOUSEBUTTONDOWN:
            if py.mouse.get_pressed()[0]:
                if self.button_click_rect.collidepoint(mouse_x, mouse_y):
                    print("button clicked")
                    return self.on_click
        return None


class character():
    def __init__(self, frame, character_folder_path, start_x, start_y):

        self.drive_animation_tracker = 1
        
        self.character_folder_path = character_folder_path
        self.x, self.y = start_x, start_y

        # Load the character image in
        character_image_path = self.character_folder_path + "/robot_jump.png" 
        image = py.image.load(character_image_path)

        # Resize the character image
        resized_image = py.transform.scale(image, (image.get_width()*0.8,image.get_height()*0.8))

        self.character_area_rect = py.Surface(resized_image.get_size()).get_rect()
        self.character_area_rect.center = (self.x, self.y)

        # Put this onto the frame
        frame.blit(resized_image, (self.x, self.y))

        # Save the created image as the last image
        self.image_to_render = image

    def draw_character(self, frame):

        # Set the scale that the image will be multiplied by
        self.scale = 0.8

        # Resize the character image
        resized_image_to_render = py.transform.scale(self.image_to_render, (self.image_to_render.get_width()*self.scale,self.image_to_render.get_height()*self.scale))

        self.character_area_rect = py.Surface(resized_image_to_render.get_size()).get_rect()
        self.character_area_rect.center = (self.x, self.y)

        # Put this onto the frame
        frame.blit(resized_image_to_render, (self.x, self.y))

        # Save the last image if it is different
        if self.image_to_render != self.image_to_render:
            self.image_to_render = self.image_to_render
    
    def move_character(self, frame, key_state_list):
        if key_state_list[py.K_s] or key_state_list[py.K_DOWN]:
            # Load the character image in
            character_image_path = self.character_folder_path + "/robot_down.png" 
            image = py.image.load(character_image_path)

            # Change its coordinates
            self.y += 5

            # Set the chosen image as the image to be displayed
            self.image_to_render = image
        
        elif key_state_list[py.K_w] or key_state_list[py.K_UP]:
            # Load the character image in
            character_image_path = self.character_folder_path + "/robot_down.png" 
            image = py.image.load(character_image_path)
            
            # Flip the image so the robot faces upwards
            image = py.transform.flip(image, False, True)

            # Change its coordinates
            self.y -= 5

            # Set the chosen image as the image to be displayed
            self.image_to_render = image

        elif key_state_list[py.K_d] or key_state_list[py.K_RIGHT]:
            # Load the character image in
            character_image_path = self.character_folder_path + "/robot_drive" + str(self.drive_animation_tracker + 1) + ".png" 
            image = py.image.load(character_image_path)

            # Change its coordinates
            self.x += 5

            # Set the chosen image as the image to be displayed
            self.image_to_render = image

            # loop the animation number for driving
            self.drive_animation_tracker = (self.drive_animation_tracker + 1) % 2

        elif key_state_list[py.K_a] or key_state_list[py.K_LEFT]:
            # Load the character image in
            character_image_path = self.character_folder_path + "/robot_drive" + str(self.drive_animation_tracker + 1) + ".png" 
            image = py.image.load(character_image_path)

            # Flip the image so the robot faces to the left
            image = py.transform.flip(image, True, False)

            # Change its coordinates
            self.x -= 5

            # Set the chosen image as the image to be displayed
            self.image_to_render = image

            # loop the animation number for driving
            self.drive_animation_tracker = (self.drive_animation_tracker + 1) % 2
    
    def select_item(self, frame, item, key_event):
        if key_event.type == py.KEYDOWN:
            if key_event.key == py.K_SPACE:
                # Load the character image in
                character_image_path = self.character_folder_path + "/robot_jump.png" 
                image = py.image.load(character_image_path)

                # Set the chosen image as the image to be displayed
                self.image_to_render = image

        elif key_event.type == py.KEYUP:
            if key_event.key == py.K_SPACE:
                # Load the character image in
                character_image_path = self.character_folder_path + "/robot_drive1.png" 
                image = py.image.load(character_image_path)

                # Set the chosen image as the image to be displayed
                self.image_to_render = image
