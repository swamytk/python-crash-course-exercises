class Settings:
    ''' Settings class to store and retieve all configuration for Alien Invasion '''
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3 # number of bullets on screen at a time

        # Alien settings
        self.fleet_drop_speed = 10

        # Game speed level up
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5 
        self.bullet_speed = 2.5
        self.alien_speed = 1.0        
        self.fleet_direction = 1    # 1 - right, -1, left
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale 

        self.alien_points = int(self.alien_points * self.score_scale)       
        