
import pygame

from pygame.sprite import Sprite

class Boss_Bullet(Sprite):
    """A class to manage bullets fired from the boss ship."""

    def __init__(self, sis_game):
        super().__init__()
        self.screen = sis_game.screen
        self.settings = sis_game.settings
        self.boss_ship = sis_game.boss_ship
        self.color = self.settings.boss_bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.boss_bullet_width,
            self.settings.boss_bullet_height)
        self.rect.midright = sis_game.boss_ship.rect.midleft
        self.rect.y += 5

        self.x = float(self.rect.x)

    def update(self):
        "Move the missile across the screen."
        self.x -= self.settings.boss_bullet_speed

        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the boss ship at its current location."""
        pygame.draw.rect(self.screen, self.color, self.rect)
