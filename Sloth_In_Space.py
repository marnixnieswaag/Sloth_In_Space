import sys
from time import sleep
import math
import pygame
import random

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from asteroid import Asteroid
from boss_ship import Boss_Ship

class Sloth_In_Space:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources"""
        super().__init__()
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode ((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Sloth In Space")

        # Create an instance to store game statisctics.
        #   and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        # Scale background to screensize
        self.bg = pygame.image.load("images/space_background.png").convert()
        self.bg = pygame.transform.smoothscale(self.bg, self.screen.get_size())
        self.bg_width = self.bg.get_width()
        self.bg_rect = self.bg.get_rect()

        #define game variables 
        self.scroll = 0
        self.tiles = math.ceil(self.screen_width / self.bg_width) + 1
 
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.boss_ship = Boss_Ship(self)

        #Start sloth in space in an inactive state.
        self.game_active = False

        # Make the Play button.
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self.clock.tick(60)
            self._check_events()

            if self.game_active:

                self.ship.update()
                self.boss_ship.update()
                self.update_bullets()
                self._update_asteroids()

            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                    
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Reset the game statistics
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active = True

            # Get rid of any remaining bullets and asteroids.
            self.bullets.empty()
            self.asteroids.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()
            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

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
    
    def _check_asteroids_left(self):
        """Check if any asteroids have reached the left of the screen"""
        for asteroid in self.asteroids.sprites():
            if asteroid.rect.left <= 0:
                # Treat this the same as if the ship got hit.
                self._ship_hit(asteroid)
                break
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullet group."""
        # Update bullet positions.
        new_bullet = Bullet(self)
        if len(self.bullets) < self.settings.bullets_allowed: 
            self.bullets.add(new_bullet)

    def update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

         # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left >=1800:
                self.bullets.remove(bullet)

        self._check_bullet_asteroid_collisions()

    def _check_bullet_asteroid_collisions(self):
        """Respond to bullet-asteroid collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.asteroids, True, True) 
        
        if collisions:
            for asteroids in collisions.values():
                self.stats.score += self.settings.asteroid_points \
                      * len(asteroids)
            self.sb.prep_score()
            self.sb.check_high_score()

        # Stops spawning the asteroids and 
        # let the boss ship enter the screen every 10th level
            if not self.asteroids and self.stats.level % 1 == 0:   
                self.boss_ship._enter_screen()
                # Destroy existing bullets and create new fleet.
                self.bullets.empty()
                self.stats.level += 1
                self.sb.prep_level()
                self.settings.increase_speed()

            elif not self.asteroids:
                
                self.bullets.empty()
                self.stats.level += 1
                self.sb.prep_level()
                self.settings.increase_speed()
                self._create_fleet()
               
        
               
    
    def _update_asteroids(self):
        """Update the position of all asteroids in the fleet."""
        self.asteroids.update()

        # Look for asteroid-ship collisions.
        collided_asteroid = pygame.sprite.spritecollideany(self.ship, self.asteroids)
        if collided_asteroid:
            self._ship_hit(collided_asteroid)
        
        # look for asteroids hitting the left of the screen.
        self._check_asteroids_left()
            

    def _update_screen(self):
        """Update images on the screen, and flip to the screen."""
        self.screen.fill(self.settings.bg_color)
        self._scroll_background()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.boss_ship.blitme()
        self.asteroids.draw(self.screen)
        self.boss_ship._draw_hp_bar()
        # Draw the score information.
        self.sb.show_score()

        # Draw the play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def _create_fleet(self):
        """Create the fleet of asteroids."""
        while len(self.asteroids.sprites()) < self.settings.number_of_asteroids: 
            current_x = random.randint(self.screen_width , (self.screen_width * 2) - 120)
            current_y = random.randint(20, self.screen_height - 120)
    
            self._create_asteroid(current_x, current_y)
        
    def _create_asteroid(self, x_position, y_position):
        """Create an asteroid and place it in the fleet."""
        new_asteroid = Asteroid(self)
        new_asteroid.x = x_position
        new_asteroid.rect.x = x_position
        new_asteroid.rect.y = y_position
        self.asteroids.add(new_asteroid)

    def _ship_hit(self, asteroid):
        """Respond to the ship being hit by an asteroid."""
        if self.stats.ships_left > 0:
            # Decrement ships_left and update scoreboard.
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self.asteroids.remove(asteroid)
          
          
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _scroll_background(self):
        """Makes the background scroll infinitely"""

        # Draw scrolling background
        for i in range(0, self.tiles):
            self.screen.blit(self.bg, (i * self.bg_width + self.scroll, 0))
            self.bg_rect.x = i * self.bg_width + self.scroll
            pygame.draw.rect(self.screen, (0, 0, 0), self.bg_rect, 1)

        #scroll background
        self.scroll -= 2

        #reset scroll
        if abs(self.scroll) > self.bg_width:
            self.scroll = 0


if __name__ == '__main__':
    # Make a game instance, and run the game.
    sis = Sloth_In_Space()
    sis.run_game()

