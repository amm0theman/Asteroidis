"""takes care of movement for next frame of game play"""
from gameState import GameState
from ship import Ship
import math
from command import Command
from point import Point


class MovementManager:
    def __init__(self, render_pace, window_x, window_y):
        self.renderPace = render_pace
        self.window_x = window_x
        self.window_y = window_y
        self.command_ship1: Command = Command()
        self.command_ship2: Command = Command()

    def calculate_ship_movement(self, ship: Ship):
        ship.pos += ship.pos_delta * self.renderPace
        ship.pos = self.calculate_wrap(ship.pos)
        return ship

    def calculate_rotation(self, game_state: GameState) -> GameState:
        if self.command_ship1.right:
            game_state.my_ship.heading -= 1
        elif self.command_ship1.left:
            game_state.my_ship.heading += 1
        if self.command_ship2.right:
            game_state.enemy_ship.heading -= 1
        elif self.command_ship2.left:
            game_state.enemy_ship.heading += 1
        return game_state

    @staticmethod
    def calculate_heading_vector(ship: Ship) -> Point:
        theta = ship.heading
        magnitude = ship.acceleration
        heading_vector = Point(magnitude * math.cos(theta), magnitude * math.sin(theta))
        return heading_vector

    def calculate_pos_delta(self, game_state: GameState) -> GameState:
        if self.command_ship1.accel:
            game_state.my_ship.pos_delta += self.calculate_heading_vector(game_state.my_ship)
        if self.command_ship2.accel:
            game_state.enemy_ship.pos_delta += self.calculate_heading_vector(game_state.enemy_ship)
        return game_state

    def calculate_movement(self, game_state: GameState) -> GameState:
        """Calculates movement for all game objects in the game state"""
        '# Calculate ships movements'
        game_state.my_ship = self.calculate_ship_movement(game_state.my_ship)
        game_state.enemy_ship = self.calculate_ship_movement(game_state.enemy_ship)

        '# Calculate movement for asteroids and for bullets'
        for i in game_state.asteroids:
            i.pos += i.pos_delta * self.renderPace
            i.pos = self.calculate_wrap(i.pos)
        for i in game_state.bullets:
            i.pos += i.pos_delta * self.renderPace
            i.pos = self.calculate_wrap(i.pos)

        return game_state

    def calculate_wrap(self, position: Point) -> Point:
        window_min = 0
        if position.x < window_min:
            position.x = self.window_x
        elif position.x > self.window_x:
            position.x = window_min
        if position.y < window_min:
            position.y = self.window_y
        elif position.y > self.window_y:
            position.y = window_min
        return position
