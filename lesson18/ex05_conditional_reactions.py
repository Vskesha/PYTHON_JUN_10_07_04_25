import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Взаємодія між об'єктами")

square1 = pygame.Rect(350, 250, 100, 100)
square2 = pygame.Rect(150, 150, 100, 100)
color1 = (0, 128, 255)
color2 = (255, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                square1.x -= 10
            elif event.key == pygame.K_RIGHT:
                square1.x += 10
            elif event.key == pygame.K_UP:
                square1.y -= 10
            elif event.key == pygame.K_DOWN:
                square1.y += 10

    if square1.colliderect(square2):
        color1 = (0, 255, 0)
    else:
        color1 = (0, 128, 255)

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, color2, square2)
    pygame.draw.rect(screen, color1, square1)
    pygame.display.flip()

pygame.quit()
