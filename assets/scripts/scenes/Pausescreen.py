import pygame.image
import time
from pygame.locals import *

from os.path import join as path_join

from assets.scripts.classes.hud_and_rendering.SelectButtonMatrix import SelectButtonMatrix
from assets.scripts.math_and_data.Vector2 import Vector2
from assets.scripts.math_and_data.enviroment import *
from assets.scripts.classes.hud_and_rendering.Scene import Scene, render_fps

class PauseScene(Scene):

    #initialize Pausescreen
    def __init__(self):
        super().__init__()
        music_module.play_music("01.-A-Dream-that-is-more-Scarlet-than-Red_1.wav")