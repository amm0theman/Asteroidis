import pygame
from gameState import GameState
from point import Point
from ship import Ship
from asteroid import Asteroid
from bullet import Bullet
from movementManager import MovementManager
from command import Command


class GameLoop:
    def __init__(self):
        '# Initialize game window and settings etc.'
        self.screen = pygame.display.set_mode(
            (1000, 1000))
        pygame.display.set_caption("Asteroids")
        self.render_pace: float = 1/60
        self.game_active = True

        self.ship = Ship(self.screen, Point(40, 60), Point(50, 100), 100, 5)
        self.enemy_ship = Ship(self.screen, Point(100, 60), Point(100, 100), 100, 5)
        self.asteroids = Asteroid(self.screen, Point(100, 100), Point(100, 500), 50)
        self.asteroids = Asteroid(self.screen, Point(100,100), Point(100,500), 50)
        self.bullets = Bullet(self.screen, self.ship.pos, self.ship.pos_delta, 50)
        self.game_state = GameState(self.ship, self.enemy_ship, 50, 50)
        self.movement_manager = MovementManager(self.render_pace)

    def handle_events(self):

        command_ship1 = Command()
        command_ship2 = Command()

        for event in pygame.event.get():
            '# When x button pushed quit game'
            if event.type == pygame.KEYDOWN:
                '#process ship one key down presses'
                if event == pygame.K_w:
                    self.movement_manager.command_ship1.accel = True
                elif event == pygame.K_a:
                    self.movement_manager.command_ship1.right = True
                elif event == pygame.K_d:
                    self.movement_manager.command_ship1.left = True
                elif event == pygame.K_SPACE:
                    self.movement_manager.command_ship1.shoot = True
                elif event == pygame.K_8:
                    '#process ship two key down presses'
                    self.movement_manager.command_ship2.accel = True
                elif event == pygame.K_4:
                    self.movement_manager.command_ship2.left = True
                elif event == pygame.K_6:
                    self.movement_manager.command_ship2.right = True
                elif event == pygame.K_0:
                    self.movement_manager.command_ship2.shoot = True
            elif event.type == pygame.KEYUP:
                '#process ship one key up presses'
                if event == pygame.K_w:
                    self.movement_manager.command_ship1.accel = False
                elif event == pygame.K_a:
                    self.movement_manager.command_ship1.right = False
                elif event == pygame.K_d:
                    self.movement_manager.command_ship1.left = False
                elif event == pygame.K_SPACE:
                    self.movement_manager.command_ship1.shoot = False
                elif event == pygame.K_8:
                    '#process ship two key up presses'
                    self.movement_manager.command_ship2.accel = False
                elif event == pygame.K_4:
                    self.movement_manager.command_ship2.left = False
                elif event == pygame.K_6:
                    self.movement_manager.command_ship2.right = False
                elif event == pygame.K_0:
                    self.movement_manager.command_ship2.shoot = False
                    command_ship1.shoot = False
            elif event.type == pygame.QUIT:
                self.game_active = False
                pygame.quit()

    def update_game(self):
        self.game_state = self.movement_manager.calculate_movement(self.game_state)

    def render_game(self):
        '#render new asteroids at new locations ever call'
        "#render new ship locations and heading directions"
        '#render bullets as they are created and travel until they die'
        pygame.display.flip()
        pass


    """Main game loop"""
    def run_game(self):
        pygame.init()

        Ship.blitme(self.ship)
        Ship.blitme(self.enemy_ship)
        Asteroid.blitme(self.asteroids, 100, 100)

        while self.game_active:
            self.handle_events()
            self.update_game()
            self.render_game()
