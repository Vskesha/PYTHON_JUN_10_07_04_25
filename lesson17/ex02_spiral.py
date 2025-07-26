import colorsys
import pygame
import math

from random import randint

# Ініціалізація Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Малювання спіралі")

x, y = 400, 300
length = 5
angle = 0 
color = (0, 255, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if length > 70:
        screen.fill((0, 0, 0))
        x, y = 400, 300
        length = 5
        angle = 0
    # color = colorsys.hsv_to_rgb((length - 5) / 20, 1.0, 1.0)
    # color = tuple(c * 255 for c in color)
    # if length % 5 == 0:
    #     color = (randint(0, 255), randint(0, 255), randint(0, 255))
    end_x = x + length * math.cos(math.radians(angle))
    end_y = y + length * math.sin(math.radians(angle))
    pygame.draw.line(screen, color, (x, y), (end_x, end_y), 5)
    x, y = end_x, end_y
    angle += 10
    length += 0.5

    pygame.display.flip()
    pygame.time.delay(50)

pygame.quit()