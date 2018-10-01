import pygame
import time

'# Initialize game window and settings etc.'
pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Asteroids")


def render():
    window.fill((0, 0, 0))
    pygame.display.update()


def update_game(time, dt):
    True


running = True
time = time.time()
while running:
        update_game(time)

        for event in pygame.event.get():
            '# When x button pushed quit game'
            if event.type == pygame.QUIT:
                running = False



        '# Clear the screen before drawing stuff'
        render()

pygame.quit()
