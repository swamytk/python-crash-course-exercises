import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    ''' A class to manage the ship '''

    def __init__(self, ai_game):
        ''' Initialize starting position '''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load image and get its location 
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start the new ship at middle bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal location
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        ''' Draw ship at current location '''
        self.screen.blit(self.image, self.rect)

    def update(self):
        ''' Update ship position based on movement flags '''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        self.rect.x = self.x

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
