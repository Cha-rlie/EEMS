# Simple Rednering PyGame Functions

# Import necessary classes
import pygame as py

class simple_functions:
    def __init__(self):
        pass

    def draw_text(self, frame, text, colour, size, font, x, y):
        font_obj = py.font.Font(font, size)

        text_surface = font_obj.render(text, False, colour)

        text_rect = text_surface.get_rect()

        text_rect.center = (x,y)

        frame.blit(text_surface,text_rect)