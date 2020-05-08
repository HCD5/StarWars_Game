import pygame

class Settings:
    """Class to store all of the settings for the game"""

    def __init__(self):
        """Initilize all of the games settings"""
        # Screen settings
        self.screen_w = 1200
        self.screen_h = 800
        self.background = pygame.image.load('pictures/back.png')
        self.background = pygame.transform.smoothscale(self.background, (1200, 800))
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_limit = 3

        # Laser settings
        self.laser_width = 3
        self.laser_height = 20
        self.laser_color = (255, 31, 31)
        self.laser_amount = 4

        # Tie fighter settings
        self.fleet_drop_speed = 10
        # 1 = right, -1 = left
        self.fleet_direction = 1

        # Game speed up and score scale
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initilize_dynamic_settings()

    def initilize_dynamic_settings(self):
        """Initilize settings that are subject to change throughout gameplay"""
        self.ship_speed = 8
        self.laser_speed = 10
        self.tie_speed = 4

        # 1 = right, -1 = left
        self.fleet_direction = 1

        # Scoreing
        self.tie_points = 25

    
    def increase_speed(self):
        """Increase speed of game elements and points value for hitting ties"""
        self.ship_speed *= self.speedup_scale
        self.laser_speed *= self.speedup_scale
        self.tie_speed *= self.speedup_scale

        self.tie_points = int(self.tie_points * self.score_scale)