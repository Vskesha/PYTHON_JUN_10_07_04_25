import pygame
import sys
from pathlib import Path

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Умовна анімація")

folder_path = Path(__file__).parent.joinpath("images/hero")
idle_image = pygame.image.load(folder_path.joinpath("idle.png"))
jump_image = pygame.image.load(folder_path.joinpath("jump.png"))
crouch_image = pygame.image.load(folder_path.joinpath("crouch.png"))
attack_image = pygame.image.load(folder_path.joinpath("attack.png"))

x = 300
y = y_start = 500
vertical_speed = 40
is_jumping = False
is_crouching = False
is_attacking = False
y_speed = 0
gravity = 4
image = idle_image

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
                y_speed = vertical_speed
                image = jump_image
            elif event.key == pygame.K_DOWN and not is_jumping:
                is_crouching = True
                image = crouch_image
            elif event.key == pygame.K_a and not (is_jumping or is_crouching):
                is_attacking = True
                image = attack_image
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                is_crouching = False
                image = idle_image
            elif event.key == pygame.K_a:
                is_attacking = False
                image = idle_image
    
    if is_jumping:
        y -= y_speed
        y_speed -= gravity
        if y >= y_start:
            y = y_start
            is_jumping = False
            image = idle_image

    screen.fill((255, 255, 255))
    screen.blit(image, (x, y - image.get_height()))
    pygame.display.flip()
    clock.tick(fps)
