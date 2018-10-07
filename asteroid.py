"""Asteroid object in the game"""
from point import Point
import pygame


class Asteroid:
    def __init__(self, screen, pos: Point, pos_delta: Point, size):
        self.screen = screen
        self.pos: Point = pos
        self.pos_delta: Point = pos_delta
        self.size = size

        self.image = pygame.image.load('venv/images/asteroid.png')
        self.image = pygame.transform.scale(self.image, (self.size, self.size - 25))

    def blitme(self):
        self.screen.blit(self.image, (self.pos.x, self.pos.y))
