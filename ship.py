"""#Point class representing ship controlled by player"""
from functools import singledispatch
from point import Point
from bullet import Bullet
from gameStateInterfaces import IShipState
from asteroid import Asteroid
import pygame


class Ship(IShipState):
    def __init__(self, screen, pos: Point, pos_delta: Point, heading: float, acceleration: float):
        self.screen = screen
        self.pos: Point = pos
        self.pos_delta: Point = pos_delta
        self.heading: float = heading
        self.acceleration: float = acceleration

        self.image = pygame.image.load('venv/images/ship.bmp')
        self.image = pygame.transform.scale(self.image, (80, 60))
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    @singledispatch
    def intersect_event(self, arg):
        pass

    @intersect_event.register(Bullet)
    def _(self, arg: Bullet):
        pass

    @intersect_event.register(Asteroid)
    def _(self, arg: Asteroid):
        pass
