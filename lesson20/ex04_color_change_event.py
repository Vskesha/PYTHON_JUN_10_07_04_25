import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Використання таймерів")

WHITE = (255, 255, 255)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
color_idx = 0

x, y = 0, 300
speed = 2

clock = pygame.time.Clock()
fps = 60

MOVE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_EVENT, 10)
COLOR_CHANGE_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(COLOR_CHANGE_EVENT, 1000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOVE_EVENT:
            x += speed
            if x > 800:
                x = -50
        elif event.type == COLOR_CHANGE_EVENT:
            color_idx = (color_idx + 1) % len(colors)
        
    screen.fill(WHITE)
    pygame.draw.rect(screen, colors[color_idx], (x, y, 50, 50))
    pygame.display.flip()
    clock.tick(fps)
