"""#Point class representing ship controlled by player"""

from point import Point
import pygame


class Ship:
    def __init__(self, screen, pos: Point, pos_delta: Point, heading: float, acceleration: float):
        self.screen = screen
        self.pos: Point = pos
        self.pos_delta: Point = pos_delta
        self.heading: float = heading
        self.acceleration: float = acceleration

        self.image = pygame.image.load('images/ship.png')
        self.circle = self.image.get_circle()

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

    def blitme(self):
        self.screen.blit(self.image, self.circle)