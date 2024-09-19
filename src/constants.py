"""
CS1 24fa - Assignment 4
Constants required for a Newton's cradle simulation.
"""
from vpython import *

GRAV = 9.81 # gravitational acceleration in m/s^2
R = 0.2 # cord length in meters, functions as size parameter for whole system
THETA_INIT = -30 * pi / 180 # initial angle of 1st pendulum in radians

DT = 0.005 # timestep (between 0.000005 [slo-mo] and 0.01 [normal])

# TODO 0.1: Choose the relevant range of cells in the spreadsheet
RANGE = ""
# TODO 0.2: Enter the relevant spreadsheet ID 
SPREADSHEET_ID = ""

# Define color and texture dictionaries that map strings -> VPython attributes
COLOR_MAP = {
    "red": color.red,
    "green": color.green,
    "blue": color.blue,
    "yellow": color.yellow,
    "orange": color.orange,
    "cyan": color.cyan,
    "magenta": color.magenta,
    "white": color.white,
    "black": color.black,
    "gray": color.gray(0.5) 
}

TEXTURE_MAP = {
    "earth": textures.earth,
    "flower": textures.flower,
    "granite": textures.granite,
    "gravel": textures.gravel,
    "metal": textures.metal,
    "rock": textures.rock,
    "rough": textures.rough,
    "rug": textures.rug,
    "stones": textures.stones,
    "stucco": textures.stucco,
    "wood": textures.wood,
    "wood_old": textures.wood_old
}
