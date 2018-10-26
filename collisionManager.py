"""#This function will handle the collision of objects"""

from gameState import GameState
from point import Point
import math
import pygame


class CollisionManager:
    def __init__(self):
        pass

    '#compare each intersection'
    def if_intersect(self, game_state: GameState) -> GameState:
        for i in game_state.asteroids:
            if pygame.sprite.collide_mask(game_state.my_ship, i):
                game_state.my_ship.pos = Point(400, 500)
                game_state.my_ship.pos_delta = Point(0, 0)
                game_state.my_ship.heading = -math.pi/2

        for i in game_state.asteroids:
            if pygame.sprite.collide_mask(game_state.enemy_ship, i):
                game_state.enemy_ship.pos = Point(600, 500)
                game_state.enemy_ship.pos_delta = Point(0, 0)
                game_state.enemy_ship.heading = -math.pi/2

        for i in game_state.asteroids:
            for j in game_state.bullets:
                if pygame.sprite.collide_mask(i, j):
                    game_state.asteroids.remove(i)
                    game_state.bullets.remove(j)
        return game_state



