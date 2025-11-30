import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    # Class to manage game assets and behavior
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)
        self.bg_color = (self.settings.bg_color)
        
    def run_game(self):
        # Starts the main loop of the game
        while True:
            self.check_events()
            self.ship.update()
            self.update_screen()
            self.clock.tick(60)
    
    def check_events(self):
        # Read Inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # when the key is pressed
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                # When the key is released
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
                    
    
    def update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        pygame.display.flip()
        

if __name__ == '__main__':
    # Make game instance
    ai = AlienInvasion()
    ai.run_game()