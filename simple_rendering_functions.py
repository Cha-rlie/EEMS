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

        text_rect.center = (x,y)

        frame.blit(text_surface,text_rect)

class button:
    def __init__(self, frame, text, size, x, y, primary_colour="#3D5A80", secondary_colour="#EE6C4D", font="Assets/Font/aesymatt.ttf"):
        self.text_colour = primary_colour
        self.background_colour = secondary_colour
        font_obj = py.font.Font(font, size)
        text_obj = font_obj.render(text, False, self.text_colour)
        self.text_size = text_obj.get_size()
        self.button_surface = py.Surface(self.text_size)
        self.button_surface.fill(self.background_colour)
        frame.blit(text_obj,(0,0))
        self.button_click_rect = py.Rect(x, y, self.text_size[0], self.text_size[1])
        frame.blit(self.button_surface, (x,y))

    def react_to_click(self):
        self.button_surface.fill(py.Color("white"))

    def click_button(self, event):
        mouse_x, mouse_y = py.get_pos()
        if event.type == py.MOUSEBUTTONDOWN:
            if py.mouse.get_pressed()[0]:
                if self.button_click_rect.collidepoint(mouse_x, mouse_y):
                    self.react_to_click()