import pygame
from gameState import GameState
from movementManager import MovementManager


class GameLoop:
    def __init__(self):
        '# Initialize game window and settings etc.'
        self.screen = pygame.display.set_mode(
            (1000, 1000))
        pygame.display.set_caption("Asteroids")
        self.render_pace: float = 1/60
        self.game_active = True
        self.game_state = GameState(None, None, None, None)
        self.movement_manager = MovementManager(self.game_state, self.render_pace)

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
        self.game_state = self.movement_manager.calculate_movement()

    def render_game(self):
        pass

    """Main game loop"""
    def run_game(self):
        pygame.init()

        while self.game_active:
            self.handle_events()
            self.update_game()
            self.render_game()
