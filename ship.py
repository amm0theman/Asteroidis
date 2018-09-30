"""#Point class representing ship controlled by player"""
from point import Point


class Ship:
    def __init__(self, pos, pos_delta, heading, acceleration):
        self.pos = Point(pos)
        self.pos_delta = Point(pos_delta)
        self.heading = heading
        self.acceleration = acceleration
