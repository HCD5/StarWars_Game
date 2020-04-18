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
        while true:
            