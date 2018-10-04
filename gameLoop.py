import pygame
from gameState import GameState
from point import Point
from ship import Ship


class GameLoop:
    def __init__(self):
        '# Initialize game window and settings etc.'
        self.screen = pygame.display.set_mode(
            (1000, 1000))
        pygame.display.set_caption("Asteroids")
        self.game_active = True
        self.ship = Ship(self.screen, Point(40, 60), Point(50, 100), 100, 5)
        self.enemy_ship = Ship(self.screen, Point(100, 60), Point(100, 100), 100, 5)
        self.game_state = GameState(self.ship, self.enemy_ship, 50,50)

    def handle_events(self):
        for event in pygame.event.get():
            '# When x button pushed quit game'
            if event.type == pygame.QUIT:
                self.game_active = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.game_active = True

        '# Sets the screen to next render'
        pygame.display.flip()

    def update_game(self):
        pass

    def render_game(self):
        pass

    """Main game loop"""
    def run_game(self):
        pygame.init()

        while self.game_active:
            self.handle_events()
            self.update_game()
            self.render_game()
