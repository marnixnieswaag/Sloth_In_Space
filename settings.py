import pygame

class Settings:
    """A class to store all settings for Sloth In Space."""

    def __init__(self):
        """initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.background = pygame.image.load("images/space_background.png")

        # Ship settings
        self.ship_speed = 3.0