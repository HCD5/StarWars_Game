import sys
import pygame

from settings import Settings

class StarwarsInvaders:
    """Main class to manage gamplay"""

    def __init__(self):
        """Start up game and creat gamplay features"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_w,self.settings.screen_h))
        pygame.display.set_caption("StarWars Invaders")


    def run_game(self):
        """Starts the main loop for gamplay"""
        while True:
            # Watch for input from the user
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Update backround
            self.screen.fill(self.settings.bg_color)

            # Update screen
            pygame.display.flip()

if __name__ == '__main__':
    # Rum game
    si = StarwarsInvaders()
    si.run_game()

    
