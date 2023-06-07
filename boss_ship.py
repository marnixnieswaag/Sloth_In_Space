import pygame
from pygame.sprite import Sprite
from random import randint
from settings import Settings

class Boss_Ship(Sprite):
    """A Class to manage the boss ship."""

    def __init__(self, sis_game):
        """Initialize the boss ship and it's starting postition."""
        self.sis_game = sis_game
        self.settings = Settings()
        self.movement = False
        self.screen = sis_game.screen
        self.settings = sis_game.settings
        self.screen_rect = sis_game.screen.get_rect()
        self.screen_width = sis_game.screen_width
        self.screen_height = sis_game.screen_height
        # Load the boss ship's image and get it's rect
        self.image = pygame.image.load('images/boss_ship.bmp')
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        # Start each new ship at the left outside of the screen.
        self.rect.midleft = self.screen_rect.midright
        # Store a float for the ship's exact vertical position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.x_speed = 2.5
        self.y_speed = 2.5

        self.enter_screen = False
        self.move_random = False

    def update(self):
        """Update the boss ship's position based on the movement flag."""
        if self.enter_screen:
            self.x -= 2
        
        if self.rect.right == (self.screen_rect.right - 100) :
            self.enter_screen = False
            self._move_random()
        
        if self.move_random:

            if (self.x + self.width >= self.screen_width) or \
                (self.x  <= (self.screen_width/2)):
                self.x_speed = -self.x_speed
            
            if (self.y + self.height >= self.screen_height) or (self.y <= 0):
                self.y_speed =  -self.y_speed
        
            self.x += self.x_speed
            self.y += self.y_speed



        self.rect.x = self.x
        self.rect.y = self.y
            

    def _enter_screen(self):
        """Move the boss ship from outside to center of the screen
        """
        self.enter_screen = True

    def _move_random(self):
       
        """Moves the boss ship in a random pattern."""
        self.move_random = True

    def blitme(self):
        """Draw the boss ship at its current location."""
        self.screen.blit(self.image, self.rect)