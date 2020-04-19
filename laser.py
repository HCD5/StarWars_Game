import pygame
from pygame.sprite import Sprite

class Laser(Sprite):
    """A class to manage the lasers the players ship shoots"""

    def __init__(self, si_game):
        """Create a laser from the ships current position"""
        super().__init__()
        self.screen = si_game.screen
        self.settings = si_game.settings
        self.color = si_game.settings.laser_color

        # Create laser and then set correct position
        self.rect = pygame.Rect(0,0, self.settings.laser_width, self.settings.laser_width)
        self.rect.midtop = si_game.ship.rect.midtop

        # Store lasers position
        self.y = float(self.rect.y)


    def update(self):
        """Move the laser up the screen"""
        # Update position of the laser
        self.y -= self.settings.laser_speed
        self.rect.y = self.y


    def place_laser(self):
        """Draw laser on the screen"""
        pygame.draw.rect(self.screen,self.color, self.rect)
    


