import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Wildlife Information")

bg = pygame.image.load("background.jpg")
animal = pygame.image.load("animal.png")

bg = pygame.transform.scale(bg, (800, 600))
animal = pygame.transform.scale(animal, (300, 250))

font = pygame.font.Font(None, 50)
text = font.render("Wildlife Information", True, (255, 255, 255))

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg, (0, 0))
    screen.blit(animal, (250, 200))
    screen.blit(text, (220, 50))

    pygame.display.update()
    clock.tick(60)

pygame.quit()