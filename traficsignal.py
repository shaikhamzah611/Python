import pygame

pygame.init()

# Screen
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Smart Traffic Signal Simulator")

clock = pygame.time.Clock()

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (80, 80, 80)
BLUE = (0, 100, 255)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
YELLOW = (255, 255, 0)


# Sprite class
class Car(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((80, 40))
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 330

        self.velocity = 4

    def update(self):
        self.rect.x += self.velocity


# Create car
car = Car()

# Sprite group
car_group = pygame.sprite.Group()
car_group.add(car)


# Custom event
CHANGE_SIGNAL = pygame.USEREVENT + 1

signal = GREEN
car_stopped = False

running = True

while running:

    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Custom event
        if event.type == CHANGE_SIGNAL:

            signal = RED
            car.velocity = 0
            car_stopped = True

    # Check boundary
    if car.rect.right >= 700 and not car_stopped:

        car.image.fill(RED)

        # Send custom event
        pygame.event.post(
            pygame.event.Event(CHANGE_SIGNAL)
        )

        # Put car back
        car.rect.x = 50

    # Draw background
    screen.fill(WHITE)

    # Draw road
    pygame.draw.rect(
        screen,
        GREY,
        (0, 280, 800, 150)
    )

    # Road markings
    for x in range(0, 800, 80):
        pygame.draw.rect(
            screen,
            WHITE,
            (x, 350, 40, 5)
        )

    # Traffic signal box
    pygame.draw.rect(
        screen,
        BLACK,
        (650, 40, 100, 220)
    )

    # Red light
    if signal == RED:
        pygame.draw.circle(
            screen,
            RED,
            (700, 90),
            30
        )
    else:
        pygame.draw.circle(
            screen,
            BLACK,
            (700, 90),
            30
        )

    # Yellow light
    pygame.draw.circle(
        screen,
        YELLOW,
        (700, 150),
        30
    )

    # Green light
    if signal == GREEN:
        pygame.draw.circle(
            screen,
            GREEN,
            (700, 210),
            30
        )
    else:
        pygame.draw.circle(
            screen,
            BLACK,
            (700, 210),
            30
        )

    # Update and draw car
    if not car_stopped:
        car_group.update()

    car_group.draw(screen)

    pygame.display.update()

    clock.tick(60)

pygame.quit()