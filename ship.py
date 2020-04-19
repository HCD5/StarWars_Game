import pygame

class Ship:
    """A Class to display and contol the user ship"""

    def __init__(self, si_game):
        """Create the ship and set its starting position"""
        self.screen = si_game.screen
        self.settings = si_game.settings
        self.screen_rect = si_game.screen.get_rect()

        # Load the ships image and and get its position
        self.image = pygame.image.load('pictures/ship.png')
        self.image = pygame.transform.rotozoom(self.image, 0, 0.3)
        self.rect = self.image.get_rect()

        # Place the ships starting position at the bottom middle of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Create float variable for ships x position 
        self.x = float(self.rect.x)

        # Movement flags
        self.move_right = False
        self.move_left = False

    def update(self):
        """Update the ships position based on the current movement flag"""
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.move_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update ships position
        self.rect.x = self.x

    def place_ship(self):
        self.screen.blit(self.image, self.rect)
