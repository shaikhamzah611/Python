import pygame

pygame.init()

WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Sprite Adventure")

WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
RED = (255, 0, 0)
GREEN = (0, 200, 0)

x = 250
y = 150
width = 50
height = 50
speed = 1

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed


    x = max(0, min(x, WIDTH - width))
    y = max(0, min(y, HEIGHT - height))

    if x == 0:
        color = RED
    elif x == WIDTH - width:
        color = GREEN
    else:
        color = BLUE


    screen.fill(WHITE)

    pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))

    pygame.draw.rect(screen, (0, 0, 0),
                     pygame.Rect(x, y, width, height), 3)

    pygame.display.update()

pygame.quit()