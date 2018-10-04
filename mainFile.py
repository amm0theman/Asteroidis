import pygame
from gameState import GameState
from movementManager import MovementManager


class Game:
    """Contains game loop and game objects, and manages them"""
    def __init__(self):
        self.screen = pygame.display.set_mode(
            (1000, 1000))
        pygame.display.set_caption("Asteroids")
        self.game_active = True
        self.game_state = GameState(None, None, None, None)
        self.MovementManager = MovementManager(None, None, None)

    def handle_events(self):
        for event in pygame.event.get():
            '# When x button pushed quit game'
            if event.type == pygame.QUIT:
                self.game_active = False

        '# Sets the screen to next render'
        pygame.display.flip()

    """Update Models for next frame"""
    def update_game(self):
        pass

    """Draw next frame and game objects"""
    def render_game(self):
        pass

    """Main game loop"""
    def run_game(self):
        pygame.init()

        while self.game_active:
            self.handle_events()
            self.update_game()
            self.render_game()
