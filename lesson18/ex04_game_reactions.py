import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ігрові реакції")

square = pygame.Rect(350, 250, 100, 100)
color = (0, 128, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if square.collidepoint(event.pos):
                color = (255, 0, 0)

        elif event.type == pygame.MOUSEBUTTONUP:
            color = (0, 128, 255)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                square.x -= 50
            elif event.key == pygame.K_RIGHT:
                square.x += 50
            elif event.key == pygame.K_UP:
                square.y -= 50
            elif event.key == pygame.K_DOWN:
                square.y += 50

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, color, square)
    pygame.display.flip()

pygame.quit()
