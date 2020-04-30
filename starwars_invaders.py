import sys
import pygame
from time import sleep

from settings import Settings
from ship import Ship
from laser import Laser
from tie_fighter import TieFighter
from game_stats import GameStats
from button import Button


class StarwarsInvaders:
    """Main class to manage gamplay"""

    def __init__(self):
        """Start up game and create gamplay features"""
        pygame.init()
        self.settings = Settings()

        # Initialize screen settings
        self.screen = pygame.display.set_mode((self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption("StarWars Invaders")

        # Initialize game statistics
        self.stats = GameStats(self)

        # Initialize gameplay elements
        self.ship = Ship(self)
        self.lasers = pygame.sprite.Group()
        self.tie_fighters = pygame.sprite.Group()
        self.create_fleet()

        # Create play button
        self.play_button = Button(self, "Play")


    def run_game(self):
        """Starts the main loop for gamplay"""
        while True:
            self.check_events()

            if self.stats.game_active:
                self.ship.update()
                self.update_laser()
                self.update_ties()

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

            # Check for mouse click
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)


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


    def check_play_button(self, mouse_pos):
        """Start the game when the play button is pressed"""
        if self.play_button.rect.collidepoint(mouse_pos):
            # Reset statistics
            self.stats.reset_stats()
            self.stats.game_active = True

            # Delete remaining tie fighters and lasers
            self.tie_fighters.empty()
            self.lasers.empty()

            # Create new fleet and center ship
            self.create_fleet()
            self.ship.center_ship()


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

        # Check for laser hitting ship
        self.check_laser_tie_collision()


    def check_laser_tie_collision(self):
        """Check if laser has hit a tie fighter and creates new fleet if all ties are destroyed"""
        collisions = pygame.sprite.groupcollide(self.lasers, self.tie_fighters, True, True)

        #Create another fleet if all tie fighters are destroyed
        if not self.tie_fighters:
            self.lasers.empty()
            self.create_fleet()


    def create_fleet(self):
        """Creates tie fighters and adds them to group """
          # Check to see how may tie fighters can fit in a row
        tie = TieFighter(self)
        tie_width, tie_height = tie.rect.size
        available_space_x = self.settings.screen_w - (3 * tie_width)
        number_of_ties_x = available_space_x // (2 * tie_width)

        # Find out how many rows fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_h - (3 * tie_height) - ship_height)
        number_of_rows = available_space_y // (3 * tie_height)

        # Create the first row of tie fighters
        for row_number in range(number_of_rows):
            for num_ties in range(number_of_ties_x):
                self.create_tie(num_ties, row_number)


    def create_tie(self, num_ties, number_of_rows):
        """Creates tie fighter and adds it to group"""
        #Create tie and place in the row
        tie = TieFighter(self)
        tie_width, tie_height = tie.rect.size
        tie.x = tie_width + (2 * tie_width) * num_ties
        tie.rect.x = tie.x
        tie.rect.y = tie_height + 2.5 * tie_height * number_of_rows
        self.tie_fighters.add(tie)


    def check_fleet_edges(self):
        """Checks to see if the row has reached the end of the screen"""
        for tie in self.tie_fighters.sprites():
            if tie.check_edges():
                self.change_fleet_direction()
                break


    def change_fleet_direction(self):
        """Changes the fleet direction and drops down tie fighters"""
        self.settings.fleet_direction *= -1
        for tie in self.tie_fighters.sprites():
            tie.rect.y += self.settings.fleet_drop_speed


    def update_ties(self):
        """Updates the position of the tie fighters"""
        self.check_fleet_edges()
        self.tie_fighters.update()

        # Check if tie fighter collided with ship
        if pygame.sprite.spritecollideany(self.ship, self.tie_fighters):
            self.ship_hit()

        # Check if tie fighter reached the bottom of the screen
        self.check_tie_bottom()


    def ship_hit(self):
        """Respond to the event of ship being hit"""
        if self.stats.ships_left > 0:
            # Remove a ship from statistics
            self.stats.ships_left -= 1

            # Remove remaining tie fighters and lasers
            self.tie_fighters.empty()
            self.lasers.empty()

            # Create new fleet and center ship
            self.create_fleet()
            self.ship.center_ship()

            # Pause game
            sleep(1)
        else:
            self.stats.game_active = False


    def check_tie_bottom(self):
        """Check of the tie fighters have reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for tie in self.tie_fighters.sprites():
            if tie.rect.bottom >= screen_rect.bottom:
                self.ship_hit()
                break


    def update_screen(self):
        """Updates image position on screen, and flip screen"""
        self.screen.blit(self.settings.background, (0, 0))
        self.ship.place_ship()
        for laser in self.lasers.sprites():
            laser.place_laser()
        self.tie_fighters.draw(self.screen)

        # Draw play button if game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # Run game
    si = StarwarsInvaders()
    si.run_game()