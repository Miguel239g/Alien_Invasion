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
            # Read Inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                self.screen.fill(self.bg_color)
                self.ship.blitme()
                pygame.display.flip()
                self.clock.tick(self.settings.frame_rate)

if __name__ == '__main__':
    # Make game instance
    ai = AlienInvasion()
    ai.run_game()