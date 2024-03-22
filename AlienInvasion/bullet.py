import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    ''' A Class to manage bullet fired '''

    def __init__(self, ai_game):
        super().__init__()  # Parent class constructor is called
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create and position bullet on top of ship
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Bullet's vertical position
        self.y = float(self.rect.y)

    def update(self):
        ''' Move bullet up on the screen '''
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        ''' Draw the bullet on screen '''
        pygame.draw.rect(self.screen, self.color, self.rect)
