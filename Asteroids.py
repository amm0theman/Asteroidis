"""Asteroid object in the game"""
from point import Point


class Asteroid:
    def __init__(self, pos, pos_delta, size):
        self.pos = Point(pos)
        self.pos_delta = Point(pos_delta)
        self.size = float(size)

    def get_pos(self):
        return self.pos

    def get_pos_delta(self):
        return self.pos_delta

    def get_size(self):
        return self.size

    def set_pos(self, pos):
        self.pos = pos

    def set_pos_delta(self, pos_delta):
        self.pos_delta = pos_delta

    def set_size(self, size):
        self.size = size
