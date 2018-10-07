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

    def blitme(self):
        self.screen.blit(self.image, (self.pos.x, self.pos.y))
