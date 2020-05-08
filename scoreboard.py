import pygame.font 
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    """A class to display the players score"""

    def __init__(self, si_game):
        """Initilize scoreboard properties"""
        self.si_game = si_game
        self.screen = si_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = si_game.settings
        self.stats = si_game.stats

        # Set scorboard font and color
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare first score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn players score into image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display score at the top right of the sceren
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """"Turn players highscore into an image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Place high score at the top center of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def prep_level(self):
        """Turn level number intop and image"""
        level_string = str(self.stats.level)
        self.level_image = self.font.render(level_string, True, self.text_color, self.settings.bg_color)

        # Place level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10


    def prep_ships(self):
        """Displays images of ships left"""
        self.ships = Group()
        for num_ships in range(self.stats.ships_left):
            ship = Ship(self.si_game)
            ship.rect.x = 10 + num_ships * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)


    def check_high_score(self):
        """Check for a high score and updates high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()


    def display_score(self):
        """Display scoreboard to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
