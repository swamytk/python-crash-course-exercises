import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    ''' A class for a Alien '''

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load image and get size
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Initialize near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        ''' Move alien to the right '''
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        ''' return true if on edge '''
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
