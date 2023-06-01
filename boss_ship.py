import pygame
from pygame.sprite import Sprite

class Boss_Ship(Sprite):
    """A Class to manage the boss ship."""

    def __init__(self, sis_game):
        """Initialize the boss ship and it's starting postition."""
        super().__init__()
        self.movement = False
        self.screen = sis_game.screen
        self.settings = sis_game.settings
        self.screen_rect = sis_game.screen.get_rect()

        # Load the boss ship's image and get it's rect
        self.image = pygame.image.load('images/boss_ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the left outside of the screen.
        self.rect.midleft = self.screen_rect.midright
        # Store a float for the ship's exact vertical position.
        self.x = float(self.rect.x)
   
    
    def update(self):
        """Update the boss ship's position based on the movement flag."""
        # Update the ship's 
        if self.movement:
            self.x -= 1

        self.rect.x = self.x

        if self.rect.left == self.settings.screen_width / 2:
            self.movement = False
            
    def _enter_screen(self):
        """Move the boss ship from outside the screen to right center of the screen
        """
        self.movement = True

        
        
           
        
    def blitme(self):
        """Draw the boss ship at its current location."""
        self.screen.blit(self.image, self.rect)