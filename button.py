import pygame.font

class Button:

    def __init__(self, si_game, msg):
        """Initilize buttons attributes"""
        self.screen = si_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set buttons properties
        self.width, self.height = 200, 50
        self.button_color = (255,255,0)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        # Create buttons rect
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Message
        self.prep_message(msg)

    
    def prep_message(self, msg):
        """Create image of button and place msg on it"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    
    def draw_button(self):
        """Draw button"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)