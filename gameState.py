"""#Shows the Game state for each object"""

from ship import Ship
from bullets import Bullet
from asteroid import Asteroid


class GameState:
    def __init__(self, my_ship, enemy_ship, bullets, asteroid)
        self.my_ship = Ship(my_ship)
        self.enemy_ship = Ship(enemy_ship)
        self.bullets = Bullet(bullets)
        self.asteroid = Asteroid(asteroid)

    def get_ship_state(self):
        return self.my_ship

    def get_enemy_ship_state(self):
        return self.enemy_ship

    def get_bullet_state(self):
        return self.bullets

    def get_asteroid_state(self):
        return self.asteroid

    def set_ship_state(self, my_ship):
        self.my_ship = my_ship

    def set_enemy_ship_state(self, enemy_ship):
        self.enemy_ship = enemy_ship

    def set_bullet_state(self, bullets):
        self.bullets = bullets

    def set_asteroid_state(self, asteroid):
        self.asteroid = asteroid