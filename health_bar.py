import pygame

from pygame.sprite import _Group, Sprite
from settings import Settings

class Healthbar(Sprite):
    """A class to manage the boss ship's healthbar"""

    def __init__(self, sis_game, settings : Settings):
        self.screen = sis_game.screen
        self.settings = settings