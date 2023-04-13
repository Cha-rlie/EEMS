#los notes: first, once all the shenanigans (character that can move) are done, make all the room and the links between the rooms

# EEMS (Educational Economic Market - Simulated)

# Import necessary libraries
import pygame as py
import tkinter as tk
import tkinter_handler

# Start a PyGame instance
py.init()

# Start a tkinter_handler instance
tk_handler = tkinter_handler.tk_handler()

# Initialise the dimensions of the game window (pixels)
(x, y) = (500, 500)

# Create a PyGame window
frame = py.display.set_mode([x,y])

# Change the title of the PyGame window
py.display.set_caption("EEMS")

# Initialise a Clock instance to keep track of time
clock = py.time.Clock()

# Loop the game to play infinitely until the user clicks on the cross
run_game = True

while run_game:

    # Check for inputs from the player
    for event in py.event.get():
        if event.type == py.QUIT:
            if tk_handler.check_closing():
                run_game = False

    # Update the window
    py.display.flip()

    # Ensures that all devices can run the program at a basic speed of 60 fps
    clock.tick(60)

# End the program
py.quit()