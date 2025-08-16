import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Використання таймерів")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

x, y = 0, 300
speed = 2

clock = pygame.time.Clock()
fps = 60

MOVE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_EVENT, 10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOVE_EVENT:
            x += speed
            if x > 800:
                x = -50
        
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (x, y, 50, 50))
    pygame.display.flip()
    clock.tick(fps)
