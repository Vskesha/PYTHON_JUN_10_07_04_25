import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Взаємодія між об'єктами")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

player = pygame.Rect(100, 100, 100, 100)
target = pygame.Rect(400, 300, 100, 100)

speed = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    if player.colliderect(target):
        target_color = RED
    else:
        target_color = BLUE

    screen.fill(WHITE)

    pygame.draw.rect(screen, target_color, target)
    pygame.draw.rect(screen, GREEN, player)

    pygame.display.flip()
    pygame.time.delay(5)

pygame.quit()
