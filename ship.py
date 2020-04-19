import pygame

class Ship:
    """A Class to display and contol the user ship"""

    def __init__(self, si_game):
        """Create the ship and set its starting position"""
        self.screen = si_game.screen
        self.screen_rect = si_game.screen.get_rect()

        # Load the ships image and and get its position
        self.image = pygame.image.load('pictures/ship.png')
        self.image = pygame.transform.rotozoom(self.image, 0, 0.3)
        self.rect = self.image.get_rect()

        # Place the ships starting position at the bottom middle of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flags
        self.move_right = False
        self.move_left = False

    def update(self):
        """Update the ships position based on the current movement flag"""
        if self.move_right == True:
            self.rect.x += 1
        if self.move_left == True:
            self.rect.x -= 1

    def placeShip(self):
        self.screen.blit(self.image, self.rect)
