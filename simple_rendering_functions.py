# Simple Rednering PyGame Functions

# Import necessary classes
import pygame as py


class simple_functions:
    def __init__(self):
        pass

    def draw_text(self, frame, text, size, x, y, colour="#EE6C4D", font="Assets/Font/aesymatt.ttf"):
        font_obj = py.font.Font(font, size)

        text_surface = font_obj.render(text, False, colour)

        text_rect = text_surface.get_rect()

        text_rect.center = (x, y)

        frame.blit(text_surface, text_rect)


class button:
    """def __init__(self):
        pass"""

    def __init__(
        self,
        frame,
        text,
        size,
        x,
        y,
        primary_colour="#EE6C4D",
        secondary_colour="#3D5A80",
        font="Assets/Font/aesymatt.ttf",
    ):
        self.x, self.y = (x, y)
        self.text_colour = primary_colour
        self.background_colour = secondary_colour
        self.font_obj = py.font.Font(font, size)
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
                    print("Button clicked!")
