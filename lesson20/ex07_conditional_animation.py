import pygame
import sys
from pathlib import Path

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Умовна анімація")

folder_path = Path(__file__).parent.joinpath("images/hero")
idle_image = pygame.image.load(folder_path.joinpath("idle.png"))
jump_image = pygame.image.load(folder_path.joinpath("jump.png"))

x, y = 300, 300
is_jumping = False
jump_height = 0
max_jump_height = 100

clock = pygame.time.Clock()
fps = 30

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                jump_height = max_jump_height
    
    if is_jumping:
        y -= 5
        jump_height -= 5
        if jump_height <= 0:
            is_jumping = False
        image = jump_image
    else:
        if y < 300:
            y += 5
        image = idle_image

    screen.fill((255, 255, 255))
    screen.blit(image, (x, y))
    pygame.display.flip()
    clock.tick(fps)
