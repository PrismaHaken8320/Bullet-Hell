import pygame.image
import time
from pygame.locals import *
from PIL import Image

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

        self.background = pygame.sprite.Sprite()
        self.background.rect = (0, 0, WIDTH, HEIGHT)
        self.background.image = pygame.image.load(
            path_join("assets", "sprites", "backgrounds", "background.png")
        ).convert_alpha()
        self.font = pygame.font.Font(path_join("assets", "fonts", "DFPPOPCorn-W12.ttf"), 45)

        self.matrix = [[["Retry", self.retry_game]], [["Back to Title", self.switch_to_titlescene]]]
        self.ButtonMatrix = SelectButtonMatrix(Vector2(WIDTH/2 - 150, HEIGHT/2 -150), self.matrix, self.font, (100, 100, 100), (255, 50, 40))
    

    def process_input(self, events) -> None:
        self.ButtonMatrix.handle_events(events)

        for evt in events:
            if evt.type == QUIT:
                pygame.quit()

    # update background image
    @render_fps
    def render(self, screen, clock):
        background_group = pygame.sprite.RenderPlain()
        background_group.add(self.background)

        background_group.draw(screen)

        self.ButtonMatrix.draw(screen)
    
    # Switch back to game (not yet possible)
    
    # def switch_to_game(self):
    #     from assets.scripts.scenes.GameScene import GameScene
    #     self.switch_to_scene(GameScene())
    
    
    # retry game
    def retry_game(self):
        from assets.scripts.scenes.GameScene import GameScene
        self.switch_to_scene(GameScene())

    #quit game
    def switch_to_titlescene(self):
        from assets.scripts.scenes.TitleScene import TitleScene
        self.switch_to_scene(TitleScene())