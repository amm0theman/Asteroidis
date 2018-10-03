"""#This function will handle the collision of objects"""

from gameState import GameState
from pygame import pygame


class CollisionManager:
    def __init__(self, game_state):
        self.game_state = GameState(game_state)

    '#compare each intersection'
    def if_intersect(self):
        for i in self.game_state.asteroid:
            if pygame.sprite.collide_circle(self.game_state.my_ship, i):
                '#i die'
                pass

        for i in self.game_state.bullets:
            if pygame.sprite.collide_circle(self.game_state.asteroid, i):
                '#add points? asteroid dies'
                pass

        for i in self.game_state.bullets:
            if pygame.sprite.collide_circle(self.game_state.my_ship, i):
                '#I die'
                pass

        for i in self.game_state.bullets:
            if pygame.sprite.collide_circle(self.game_state.enemy_ship, i):
                '#enemy dies'
                pass

        if pygame.sprite.collide_circle(self.game_state.my_ship, self.game_state.enemy_ship):
            '#both die'
            pass

        if pygame.sprite.collide_circle(self.game_state.enemy_ship, self.game_state.my_ship):
            '#both die still'
            pass
