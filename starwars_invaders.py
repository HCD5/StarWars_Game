import sys
import pygame

from settings import Settings
from ship import Ship

class StarwarsInvaders:
    """Main class to manage gamplay"""

    def __init__(self):
        """Start up game and create gamplay features"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_w,self.settings.screen_h))
        pygame.display.set_caption("StarWars Invaders")

        self.ship = Ship(self)


    def run_game(self):
        """Starts the main loop for gamplay"""
        while True:
            # Watch for input from the user
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Update backround and ships positions
            self.screen.fill(self.settings.bg_color)
            self.ship.placeShip()

            # Update screen
            pygame.display.flip()

if __name__ == '__main__':
    # Rum game
    si = StarwarsInvaders()
    si.run_game()

    
