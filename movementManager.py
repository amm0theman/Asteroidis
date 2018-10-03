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

    def calculate_ship_movement(self, ship: Ship):
        ship.pos = ship.pos + ship.pos_delta * self.renderPace
        return ship

    def calculate_asteroid_movement(self, asteroid: Asteroid):
        asteroid.pos = asteroid.pos + asteroid.pos_delta * self.renderPace
        return asteroid

    def calculate_movement(self):
        """Calculates movement for all game objects in the game state"""

        '# Calculate ships movements'
        self.gameState.my_ship = self.calculate_ship_movement(self.gameState.my_ship)
        self.gameState.enemy_ship = self.calculate_ship_movement(self.gameState.enemy_ship)

        '# Calculate movement for asteroids and for bullets'
        for i in self.gameState.asteroid:
            i.pos = i.pos + i.pos_delta * self.renderPace
        for i in self.gameState.bullets:
            i.pos = i.pos + i.pos_delta * self.renderPace


