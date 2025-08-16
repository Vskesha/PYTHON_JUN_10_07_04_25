import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Налаштування FPS")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

x, y = 0, 300
px_per_ms = 0.2
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
fps = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    distance = pygame.time.get_ticks() * px_per_ms
    x = distance % 800   
    pygame.draw.rect(screen, BLUE, (x, y, 50, 50))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        fps += 1
    elif keys[pygame.K_DOWN]:
        fps -= 1

    fps_text = font.render(f"FPS: {fps}", True, (0, 0, 0))
    screen.blit(fps_text, (10, 10))

    pygame.display.flip()
    clock.tick(fps)
    