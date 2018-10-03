import pygame
from ship import Ship
from point import Point


def run_game():
    pygame.init()

    '# Initialize game window and settings etc.'
    screen = pygame.display.set_mode(
        (500, 500))
    pygame.display.set_caption("Asteroids")

    ship = Ship(screen, Point(50, 50), Point(50, 50), 2.5, 1.5)

    running = True

    while running:

        ship.blitme()

        for event in pygame.event.get():
            '# When x button pushed quit game'
            if event.type == pygame.QUIT:
                running = False

        '# Sets the screen to next render'
        pygame.display.flip()


run_game()



