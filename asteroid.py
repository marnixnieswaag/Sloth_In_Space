import pygame
from pygame.sprite import Sprite

class Asteroid(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, sis_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = sis_game.screen

        # Load the asteroid image and set its starting position.
        self.image = pygame.image.load('images/asteroid.bmp')
        self.rect = self.image.get_rect()

        # Start each new asteroid near the top right of the screen.
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
