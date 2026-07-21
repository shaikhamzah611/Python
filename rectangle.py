import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen,(0,167,169),pygame.Rect(20,20,70,70))
    pygame.display.flip()