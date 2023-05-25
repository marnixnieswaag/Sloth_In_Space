import sys
import math
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class Sloth_In_Space:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode ((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Sloth In Space")
        self.bg_width = self.settings.bg.get_width()
        self.bg_rect = self.settings.bg.get_rect()

        #define game variables 
        self.scroll = 0
        self.tiles = math.ceil(self.settings.screen_width / self.bg_width) + 1
 
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()

            # Get rid of bullets that have disappeared.
            for bullet in self.bullets.copy():
                if bullet.rect.left >=1200:
                    self.bullets.remove(bullet)
            self._update_screen()
          
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullet group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to the screen."""
        self.screen.fill(self.settings.bg_color)
        self._scroll_background()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        pygame.display.flip()


    def _scroll_background(self):
        """Makes the background scroll infinitely"""

        # Draw scrolling background
        for i in range(0, self.tiles):
            self.screen.blit(self.settings.bg, (i * self.bg_width + self.scroll, 0))
            self.bg_rect.x = i * self.bg_width + self.scroll
            pygame.draw.rect(self.screen, (0, 0, 0), self.bg_rect, 1)

        #scroll background
        self.scroll -= 5

        #reset scroll
        if abs(self.scroll) > self.bg_width:
            self.scroll = 0

if __name__ == '__main__':
    # Make a game instance, and run the game.
    sis = Sloth_In_Space()
    sis.run_game()

