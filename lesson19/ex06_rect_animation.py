import pygame

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
x = 0
y = 300
speed = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Анімація об'єкта")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, (x, y, 50, 50))

    x += speed
    if x > WIDTH:
        x = -50
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
