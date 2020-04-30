class GameStats:
    """Keeps track of statistics and scoring for gameplay"""

    def __init__(self, si_game):
        """Contols game statistics"""
        self.settings = si_game.settings
        self.reset_stats()

        # Create flag for gameplay to end
        self.game_active = False

    def reset_stats(self):
        """Create statistics that will be tracked throughout the game"""
        self.ships_left = self.settings.ship_limit
