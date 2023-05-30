import pygame

class Settings:
    """A class to store all settings for Sloth In Space."""

    def __init__(self):
        """initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
       
        # Ship settings
        self.ship_speed = 7.0
        self.ship_limit = 3
        # Bullet settings
        self.bullet_speed = 10.0
        self.bullet_width = 10
        self.bullet_height = 4
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3

        # Asteroid settings
        self.asteroid_speed = 3
        self.number_of_asteroids = 20