import pygame

class Settings:
    """A class to store all settings for Sloth In Space."""

    def __init__(self):
        """initialize the game's settings."""

        # Screen settings
        self.bg_color = (0, 0, 0)
        # Ship settings
        self.ship_speed = 3.0
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 10
        self.bullet_height = 4
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3
        
        # Asteroid settings
        self.asteroid_speed = 2.0
        self.number_of_asteroids = 5
       
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        #how quickly the number of asteroids increase
        self.number_up_scale = 1

        #Boss ship health
        self.boss_ship_health = 500

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 3.0
        self.bullet_speed = 5.0
        self.asteroid_speed = 2.0
        self.number_of_asteroids = 5

        # Scoring settings
        self.asteroid_points = 50

    
    def increase_speed(self):
        """Increase speed settings and asteroid point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.asteroid_speed *= self.speedup_scale

        self.asteroid_points = int(self.asteroid_points * self.score_scale)

    def increase_asteroids(self):
        """Increase amount of asteroids."""
        self.number_of_asteroids += self.number_up_scale
        
