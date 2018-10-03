import pygame
import time
import ship

'# Initialize game window and settings etc.'
pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Asteroids")


def render():
    window.fill((0, 0, 0))
    pygame.display.update()


def update_game():
    True


running = True
while running:
    time.sleep(.016666666666)
    update_game()

    ship.blitme()

    for event in pygame.event.get():
        '# When x button pushed quit game'
        if event.type == pygame.QUIT:
            running = False

    '# Clear the screen before drawing stuff'
    render()

pygame.quit()
