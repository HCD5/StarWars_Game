import sys

import pygame

class StarwarsInvaders:
    """Main class to manage gamplay"""

    def __init__(self):
        """Start up game and creat gamplay features"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("StarWars Invaders")

    def run_game(self):
        """Starts the main loop for gamplay"""
        while True:
            # Watch for input from the user
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Update screen
            pygame.display.flip()

if __name__ == '__main__':
    # Rum game
    si = StarwarsInvaders()
    si.run_game()

    
