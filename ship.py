"""#Point class representing ship controlled by player"""
from point import Point


class Ship:
    def __init__(self, pos, pos_delta, heading, acceleration):
        self.pos = Point(pos)
        self.pos_delta = Point(pos_delta)
        self.heading = heading
        self.acceleration = acceleration

    def get_pos(self):
        return self.pos

    def get_pos_delta(self):
        return self.pos_delta

    def get_heading(self):
        return self.heading

    def acceleration(self):
        return self.acceleration

    def set_pos(self, pos):
        self.pos = pos

    def set_pos_delta(self, pos_delta):
        self.pos_delta = pos_delta

    def set_heading(self, heading):
        self.heading = heading

    def set_acceleration(self, acceleration):
        self.acceleration = acceleration
