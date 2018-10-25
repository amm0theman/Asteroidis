"""#This function will handle the collision of objects"""

from gameState import GameState
from point import Point
import pygame


class CollisionManager:
    def __init__(self):
        pass

    '#compare each intersection'
    def if_intersect(self, game_state: GameState) -> GameState:
        for i in game_state.asteroids:
            if pygame.sprite.collide_mask(game_state.my_ship, i):
                game_state.my_ship.pos = Point(400, 500)
        return game_state

