import sys
from time import sleep
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button

class AlienInvasion:
    ''' Overall class to manage game assets and behavior'''

    def __init__(self):
        ''' Initialize the game'''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        ### For Window Mode
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        ### For FullScreen Mode
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height

        self.bg_color = self.settings.bg_color
        pygame.display.set_caption("Alien Invasion")

        # Create other game objects
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # Load all media files
        self.shoot_sound = pygame.mixer.Sound('audio/bullet_shoot.wav')
        self.alien_hit = pygame.mixer.Sound('audio/alien_hit.wav')
        self.ship_hit = pygame.mixer.Sound('audio/ship_hit.wav')

        # Put in game in active state
        self.game_active = False

        # Create Play button
        self.play_button = Button(self, "Play")


    def _create_fleet(self):
        ''' create group of aliens '''
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):

            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # For next row
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        ''' Create a Alien '''
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_events(self):
        # Process input device events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked and not self.game_active:
            # Reset game statistics
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active = True
            # Reset elements
            self.bullets.empty()
            self.aliens.empty()
            # Create new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            # Hide mouse cursor
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()            

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        ''' Create a new bullet and add it to the group of bullets '''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.shoot_sound.play(maxtime=200)

    def _update_bullets(self):
        self.bullets.update()
        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        ''' handling bullet alien collision'''
        # If any bullet hit aliens, remove both
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
            self.alien_hit.play()

        # if a fleet has been destroyed
        if not self.aliens:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level
            self.stats.level += 1
            self.sb.pre_level()

    def _ship_hit(self):
        ''' Respond to the ship being hit by an alien'''
        self.ship_hit.play()
        if self.stats.ship_left > 0:
            # reduce left out ships
            self.stats.ship_left -= 1
            self.sb.prep_ships()
            # Remove all remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()
            # Create new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            # Pause a while
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _update_aliens(self):
        ''' check if the fleet is at an edtge, then update position'''
        self._check_fleet_edges()
        self.aliens.update()

        # check alien ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # Look for aliens hitting bottom
        self._check_aliens_bottom()


    def _check_fleet_edges(self):
        ''' Respond if any aliens have reached an edge'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        ''' Drop the entire fleet and change direction'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        ''' check if any aliens have reached the bottom of the screen'''
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # handle the same way ship got hit
                self._ship_hit()
                break

    def _update_screen(self):
        # Redraw the screen  
        self.screen.fill(self.bg_color)
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)

        self.sb.show_score()

        if not self.game_active:
            self.play_button.draw_button()

        # flush the drawn screen
        pygame.display.flip()

    def run_game(self):
        ''' Main loop is here'''
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            # Update the screen with all latest events
            self._update_screen()
             # to make sure that this loop runs exactly 60 times per second
            self.clock.tick(60)

if __name__ == '__main__':
    # Create game instance and run the game
    ai = AlienInvasion()
    ai.run_game()

