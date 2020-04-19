class Settings:
    """Class to store all of the settings for the game"""

    def __init__(self):
        "Initilize all of the games settings"
        # Screen settings
        self.screen_w = 1200
        self.screen_h = 800
        self.bg_color = (109, 29, 140)

        # Ship settings
        self.ship_speed = .5

        # Laser settings
        self.laser_speed = 1.0
        self.laser_width = 3.0
        self.laser_height = 30.0
        self.laser_color = (255, 31, 31)
        
