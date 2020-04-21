

class GameStats:

    def __init__(self, si_game):
        """Contols game statistics"""
        self.settings = si_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Create statistics that will be tracked throughout the game"""
        self.ships_left = self.settings.ship_limit
