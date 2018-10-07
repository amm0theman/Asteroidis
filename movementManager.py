"""takes care of movement for next frame of game play"""
from gameState import GameState
from ship import Ship
import math
from command import Command


class MovementManager:
    def __init__(self, render_pace):
        self.renderPace = render_pace
        self.command_ship1: Command = Command()
        self.command_ship2: Command = Command()

    def calculate_ship_movement(self, ship: Ship):
        ship.pos += ship.pos_delta * self.renderPace
        return ship

    def calculate_rotation(self, game_state: GameState) -> GameState:
        if self.command_ship1.right:
            game_state.my_ship.heading -= 1 * 3.14
        elif self.command_ship2.left:
            game_state.my_ship.heading += 1 * 3.14
        return game_state

    def calculate_heading_vector(self, ship: Ship):
        theta = ship.heading
        magnitude = ship.acceleration
        heading_vector = (magnitude * math.cos(theta), magnitude * math.sin(theta))
        return heading_vector

    def calculate_pos_delta(self, game_state: GameState):
        if self.command_ship1.accel:
            game_state.my_ship.pos_delta += self.calculate_heading_vector(game_state.my_ship)
        if self.command_ship2.accel:
            game_state.enemy_ship.pos_delta += self.calculate_heading_vector(game_state.enemy_ship)
        return game_state

    def calculate_movement(self, game_state: GameState):
        """Calculates movement for all game objects in the game state"""
        '# Calculate ships movements'
        game_state.my_ship = self.calculate_ship_movement(game_state.my_ship)
        game_state.enemy_ship = self.calculate_ship_movement(game_state.enemy_ship)

        '# Calculate movement for asteroids and for bullets'
        for i in game_state.asteroids:
            i.pos = i.pos + i.pos_delta * self.renderPace
        for i in game_state.bullets:
            i.pos = i.pos + i.pos_delta * self.renderPace

        return game_state

