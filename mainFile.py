import pygame

pygame.init()

window = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Asteroids")

x = 50
y = 50
width = 40
height = 60
velocity = 5


def draw_screen():
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
    pygame.display.update()


running = True
while running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        '# When x button pushed quit game'
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= velocity
    if keys[pygame.K_RIGHT]:
        x += velocity
    if keys[pygame.K_UP]:
        y -= velocity
    if keys[pygame.K_DOWN]:
        y += velocity

    '# Clear the screen before drawing stuff'
    draw_screen()

pygame.quit()
