# los notes: first, once all the shenanigans (character that can move) are done, make all the room and the links between the rooms

# EEMS (Educational Economic Market - Simulated)

# Import necessary libraries
import pygame as py
import tkinter as tk
import tkinter_handler
import scene_controller

# Start a PyGame instance
py.init()

# Start a scene_controller instance
scene_controller = scene_controller.scene_controller()

while scene_controller.game_running:

    scene_controller.main_menu_scene()

# End the program
py.quit()
