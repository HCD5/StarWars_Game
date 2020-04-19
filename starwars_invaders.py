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
            self.check_events()
            self.update_screen()


    def check_events(self):
        """Checks for user input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # Check for key down input
            elif event.type == pygame.KEYDOWN:
                self.check_keydown(event)
            # Check for key up input 
            elif event.type == pygame.KEYUP:
                self.check_keyup(event)
           

    def check_keydown(self, event):
        """Checks for keydown events"""
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        if event.key == pygame.K_LEFT:
            self.ship.move_left = True


    def check_keyup(self, event):
        """Checks for keyup events"""
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        if event.key == pygame.K_LEFT:
            self.ship.move_left = False



    def update_screen(self):
        """Updates image position on screen, and flip screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.placeShip()
        self.ship.update()

        pygame.display.flip()


if __name__ == '__main__':
    # Run game
    si = StarwarsInvaders()
    si.run_game()

    
