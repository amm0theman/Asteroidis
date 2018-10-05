"""takes care of movement for next frame of game play"""
from gameState import GameState
from ship import Ship
from asteroid import Asteroid
from command import Command


class MovementManager:
    def __init__(self, render_pace):
        self.renderPace = render_pace
        self.command_ship1: Command = None
        self.command_ship2: Command = None

    def calculate_ship_movement(self, ship: Ship):
        ship.pos = ship.pos + ship.pos_delta * self.renderPace
        return ship

    def calculate_rotation(self):
        pass

    def calculate_movement(self, game_state):
        """Calculates movement for all game objects in the game state"""

        '# Calculate ships movements'
        game_state.my_ship = self.calculate_ship_movement(game_state.my_ship)
        game_state.enemy_ship = self.calculate_ship_movement(game_state.enemy_ship)

        '# Calculate movement for asteroids and for bullets'
        for i in game_state.asteroid:
            i.pos = i.pos + i.pos_delta * self.renderPace
        for i in game_state.bullets:
            i.pos = i.pos + i.pos_delta * self.renderPace

        return game_state
