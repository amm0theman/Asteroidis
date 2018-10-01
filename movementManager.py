"""takes care of movement for next frame of game play"""
from gameState import GameState
from ship import Ship
from asteroid import Asteroid
from command import Command


class MovementManager:
    def __init__(self, game_state, render_pace, command):
        self.gameState: GameState = game_state
        self.renderPace = render_pace
        self.command: Command = command

    def set_pace(self, render_pace):
        self.renderPace = render_pace

    @staticmethod
    def calculate_ship_movement(ship: Ship):
        ship.pos = ship.pos + ship.pos_delta
        return ship

    @staticmethod
    def calculate_asteroid_movement(asteroid: Asteroid):
        asteroid.pos = asteroid.pos + asteroid.pos_delta
        return asteroid

    def calculate_movement(self):
        self.gameState.my_ship = self.calculate_ship_movement(self.gameState.my_ship)
        self.gameState.enemy_ship = self.calculate_ship_movement(self.gameState.enemy_ship)

        for i in self.gameState.asteroid
            i.
        for i in self.gameState.bullets:
            pass
