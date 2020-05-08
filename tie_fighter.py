import pygame
from pygame.sprite import Sprite


class TieFighter(Sprite):
    """Class to represent a single tie fighter in the fleet"""

    def __init__(self, si_game):
        """Create tie fighter and its starting position"""
        super().__init__()
        self.screen = si_game.screen
        self.settings = si_game.settings

        # Load image of tie and get rect of it
        self.image = pygame.image.load('pictures/tie.png')
        self.image = pygame.transform.rotozoom(self.image, 0, 0.11)
        self.rect = self.image.get_rect()

        # Place new tie figher at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the tie fighers horizontal position
        self.x = float(self.rect.x)


    def update(self):
        """Scroll tie fighter to the right"""
        self.x += (self.settings.tie_speed * self.settings.fleet_direction)
        self.rect.x = self.x


    def check_edges(self):
        """Checks to see if a tie has reached the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True