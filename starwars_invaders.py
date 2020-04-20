import sys
import pygame

from settings import Settings
from ship import Ship
from laser import Laser
from tie_fighter import TieFighter

class StarwarsInvaders:
    """Main class to manage gamplay"""

    def __init__(self):
        """Start up game and create gamplay features"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption("StarWars Invaders")

        self.ship = Ship(self)
        self.lasers = pygame.sprite.Group()
        self.tie_fighters = pygame.sprite.Group()

        self.create_fleet()


    def run_game(self):
        """Starts the main loop for gamplay"""
        while True:
            self.check_events()
            self.ship.update()
            self.update_laser()
            self.update_screen()


    def check_events(self):
        """Checks for user input"""
        for event in pygame.event.get():
            # Check if user wants to exit
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
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self.fire_laser()


    def check_keyup(self, event):
        """Checks for keyup events"""
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        if event.key == pygame.K_LEFT:
            self.ship.move_left = False


    def fire_laser(self):
        """Creates new laser and adds it to the lasers group"""
        if len(self.lasers) < self.settings.laser_amount:
            new_laser = Laser(self)
            self.lasers.add(new_laser)


    def update_laser(self):
        """Updates laser position and removes lasers that reach the edge of the screen"""
        # Update lasers positions
        self.lasers.update()

        # Get rid of lasers that reach the edge of the screen
        for laser in self.lasers.copy():
            if laser.rect.bottom <= 0:
                self.lasers.remove(laser)


    def create_fleet(self):
        """Creates tie fighters and adds them to group """
          # Check to see how may tie fighters can fit in a row
        tie = TieFighter(self)
        tie_width = tie.rect.width
        available_space_x = self.settings.screen_w - (2 * tie_width)
        number_of_ties_x = available_space_x // (2 * tie_width)

        # Create the first row of tie fighters
        for num_ties in range(number_of_ties_x):
            self.create_tie(num_ties)


    def create_tie(self, num_ties):
        #Create tie and place in the row
        tie = TieFighter(self)
        tie_width = tie.rect.width
        tie.x = tie_width + (2 * tie_width) * num_ties
        tie.rect.x = tie.x
        self.tie_fighters.add(tie)


    def update_screen(self):
        """Updates image position on screen, and flip screen"""
        self.screen.blit(self.settings.background, (0, 0))
        self.ship.place_ship()
        for laser in self.lasers.sprites():
            laser.place_laser()
        self.tie_fighters.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Run game
    si = StarwarsInvaders()
    si.run_game()