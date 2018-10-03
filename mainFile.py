import pygame
from gameState import GameState


class GameLoop:
    def __init__(self):
        '# Initialize game window and settings etc.'
        self.screen = pygame.display.set_mode(
            (1000, 1000))
        pygame.display.set_caption("Asteroids")
        self.game_active = True
        self.game_state = GameState(None, None, None, None)

    def handle_events(self):
        for event in pygame.event.get():
            '# When x button pushed quit game'
            if event.type == pygame.QUIT:
                self.game_active = False

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
