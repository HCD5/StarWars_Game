import pygame
from pygame.sprite import Sprite 

class TieFighter(Sprite):
    """Class to represent a single tie fighter in the fleet"""

    def __init__(self, si_game):
        """Create tie fighter and its starting position"""
        super().__init__()
        self.screen = si_game.screen

        # Load image of tie and get rect of it
        self.image = pygame.image.load('pictures/tie.png')
        self.image = pygame.transform.rotozoom(self.image, 0, 0.13)
        self.rect = self.image.get_rect()

        # Place new tie figher at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the tie fighers horizontal position
        self.x = float(self.rect.x)
