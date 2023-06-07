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

        # Start each new ship at the left outside of the screen.
        self.rect.midleft = self.screen_rect.midright
        # Store a float for the ship's exact vertical position.
        self.x = float(self.rect.left)
        self.y = float(self.rect.top)

        # Starting speed
        self.speed_x = 5
        self.speed_y = 4

        # Creating a variable for direction
        self.direction = 1

        self.enter_screen = False
        self.move_random = False

    def update(self):
        """Update the boss ship's position based on the movement flag."""
        if self.enter_screen:
            self.x -= 2
        
        if self.rect.left == (self.screen_rect.centerx + 20) :
            self.enter_screen = False
            self._move_random()
        
        if self.move_random:

            # Changing the direction and x,y coordinate
            if self.rect.left <= self.screen_rect.centerx or \
                self.rect.right >= self.screen_rect.right :
                    self.direction *= -1
                    self.speed_x = randint(0, 8) * self.direction
                    self.speed_y = randint(0, 8) * self.direction

                # Changing the value if speed_x
                # and speed_y both are zero
                    if self.speed_x == 0 and self.speed_y == 0:
                        self.speed_x = randint(2, 8) * self.direction
                        self.speed_y = randint(2, 8) * self.direction

            # Changing the direction and x,y coordinate
            # of the object if the coordinate of top
            # side is less than equal to 20 or bottom side coordinate
            # is greater than equal to 700
            if self.rect.top <= self.screen_rect.top or self.rect.bottom  \
                >= self.screen_rect.bottom:
                self.direction *= -1
                speed_x = randint(0, 8) * self.direction
                speed_y = randint(0, 8) * self.direction
    
                # Changing the value if speed_x
                # and speed_y both are zero
                if speed_x == 0 and speed_y == 0:
                    speed_x = randint(2, 8) * self.direction
                    speed_y = randint(2, 8) * self.direction
    

            # Adding speed_x and speed_y
            # in left and top coordinates of object
            self.x += self.speed_x
            self.y += self.speed_y


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