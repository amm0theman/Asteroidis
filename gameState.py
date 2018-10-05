"""#Shows the Game state for each object"""
from typing import List
from ship import Ship
from bullet import Bullet
from asteroid import Asteroid


class GameState:
    def __init__(self, my_ship, enemy_ship, bullets, asteroids):
        self.my_ship: Ship = my_ship
        self.enemy_ship: Ship = enemy_ship
        self.bullets: List[Bullet] = bullets
        self.asteroids: List[Asteroid] = asteroids

    def get_ship_state(self):
        return self.my_ship

    def get_enemy_ship_state(self):
        return self.enemy_ship

    def get_bullet_state(self):
        return self.bullets

    def get_asteroid_state(self):
        return self.asteroids

    def set_ship_state(self, my_ship):
        self.my_ship = my_ship

    def set_enemy_ship_state(self, enemy_ship):
        self.enemy_ship = enemy_ship

    def set_bullet_state(self, bullets):
        self.bullets = bullets

    def set_asteroid_state(self, asteroid):
        self.asteroids = asteroid
