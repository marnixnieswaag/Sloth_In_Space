import pygame
from pygame.sprite import Sprite
from random import randint
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from asteroid import Asteroid

class Boss_Ship(Sprite):
    """A Class to manage the boss ship."""

    def __init__(self, sis_game):
        """Initialize the boss ship and it's starting postition."""
        self.sis_game = sis_game
        self.settings = sis_game.settings
        self.stats = GameStats(self)
        self.sb = Scoreboard
        self.movement = False
        self.bullets = sis_game.bullets
        self.screen = sis_game.screen
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
        
        self.x_speed = 3
        self.y_speed = 3

        self.enter_screen = False
        self.move_random = False

        self.health = self.settings.boss_ship_health

    def update(self):
        """Update the boss ship's position based on the movement flag."""
        if self.enter_screen:
            self.x -= 2
        
        if self.rect.right == (self.screen_rect.right - 100) :
            self.enter_screen = False
            self._move_random()
        
        if self.move_random:

            self.draw_hp_bar = True

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

    def _respawn(self):
        """Resets the ship's location, hp and removes hp bar"""
        self.health = 500
        self.draw_hp_bar = False
        self.move_random = False
        self.rect.midleft = self.screen_rect.midright
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def _move_random(self):
       
        """Moves the boss ship in a random pattern."""
        self.move_random = True

    def _draw_hp_bar(self):
        """Draws a hp bar"""
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        pygame.draw.rect(self.screen,RED,(525,70,500,10))
        pygame.draw.rect(self.screen,GREEN,(525,70,self.health,10))


    def blitme(self):
        """Draw the boss ship at its current location."""
        self.screen.blit(self.image, self.rect)