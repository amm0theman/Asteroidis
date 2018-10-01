"""Represents player state with four booleans"""


class Command:
    def __init__(self, shoot, accel, right, left):
        self.shoot = bool(shoot)
        self.accel = bool(accel)
        self.right = bool(right)
        self.left = bool(left)

    def get_shoot(self):
        return self.shoot

    def get_accel(self):
        return self.accel

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def set_shoot(self, shoot):
        self.shoot = shoot

    def set_accel(self, accel):
        self.accel = accel

    def set_right(self, right):
        self.right = right

    def set_left(self, left):
        self.left = left
