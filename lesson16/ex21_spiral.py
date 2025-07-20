import math
import pygame
import random


width, height = 800, 600
GREEN = (0, 255, 0)

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Draw spiral")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))

    x, y = width // 2, height // 2
    length = 5
    angle = random.uniform(0, 2 * math.pi)

    for i in range(100):
        end_x = x + length * math.cos(angle)
        end_y = y + length * math.sin(angle)
        pygame.draw.line(screen, 
                         GREEN, 
                         (x, y), 
                         (end_x, end_y))
        angle += math.pi / 20
        length += 0.5
        x, y = end_x, end_y
    
        pygame.display.flip()
        pygame.time.delay(50)

pygame.quit()
