import pygame

class Settings:
    """Class to store all of the settings for the game"""

    def __init__(self):
        "Initilize all of the games settings"
        # Screen settings
        self.screen_w = 1200
        self.screen_h = 800
        self.bg_color = (211,211,211)
        self.background = pygame.image.load('pictures/back.png')
        self.background = pygame.transform.smoothscale(self.background, (1200, 800))

        # Ship settings
        self.ship_speed = 7

        # Laser settings
        self.laser_speed = 6
        self.laser_width = 3
        self.laser_height = 20
        self.laser_color = (255, 31, 31)
        self.laser_amount = 4

        
