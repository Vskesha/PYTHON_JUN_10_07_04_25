"""
Напишіть програму, яка анімує текст, 
щоб він з'являвся та зникав на екрані.
"""

import pygame
from pathlib import Path

text = "Hello, Pygame!"

pygame.init()
width, height = 1024, 768
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Blinking text")

font_file_path = Path(__file__).parent.joinpath("fonts/turok.ttf")
font = pygame.font.Font(font_file_path, 130)

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
alpha = 0
step = 5

text_img = font.render(text, True, GREEN)
text_rect = text_img.get_rect(center=(width // 2, height // 2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLACK)

    alpha += step
    if alpha == 0 or alpha == 255:
        step = -step
    text_img.set_alpha(alpha)
    screen.blit(text_img, text_rect)
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()