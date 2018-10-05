"""Bullet object in the game"""
from point import Point


class Bullet:
    def __init__(self, screen, pos, pos_delta, ttl):
        self.screen = screen
        self.pos: Point = pos
        self.pos_delta: Point = pos_delta
        self.ttl = float(ttl)

    def get_pos(self):
        return self.pos

    def get_pos_delta(self):
        return self.pos_delta

    def get_ttl(self):
        return self.ttl

    def set_pos(self, pos):
        self.pos = pos

    def set_pos_delta(self, pos_delta):
        self.pos_delta = pos_delta

    def set_ttl(self, ttl):
        self.ttl = ttl
