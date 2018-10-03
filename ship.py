"""#Point class representing ship controlled by player"""
from functools import singledispatch
from point import Point
from bullet import Bullet
import pygame


class Ship:
    def __init__(self, screen, pos: Point, pos_delta: Point, heading: float, acceleration: float):
        self.screen = screen
        self.pos: Point = pos
        self.pos_delta: Point = pos_delta
        self.heading: float = heading
        self.acceleration: float = acceleration

        self.image = pygame.image.load('venv/images/ship.bmp')
        self.image = pygame.transform.scale(self.image, (80, 60))
        self.rect = self.image.get_rect()

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
        self.screen.blit(self.image, self.rect)
        
    @singledispatch
    def intersect_event(self, arg):
        pass

    @intersect_event.register(Bullet)
    def _(self, arg: Bullet):
        pass
