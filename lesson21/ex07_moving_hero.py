import pygame
from pathlib import Path

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Image load")

clock = pygame.time.Clock()

image_path = Path(__file__).parent.joinpath(
    "images/mario/mario.gif"
)
hero_image = pygame.image.load(image_path)
hero_rect = hero_image.get_rect()
hero_rect.x = 100
hero_rect.y = 100

speed = 5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        hero_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        hero_rect.x += speed
    if keys[pygame.K_UP]:
        hero_rect.y -= speed
    if keys[pygame.K_DOWN]:
        hero_rect.y += speed

    screen.fill((0, 0, 0))
    screen.blit(hero_image, hero_rect)
    pygame.display.flip()
    clock.tick(25)

pygame.quit()
