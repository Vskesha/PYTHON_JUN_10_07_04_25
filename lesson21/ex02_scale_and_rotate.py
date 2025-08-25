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
hero_image = pygame.transform.scale(hero_image, (400, 400))
hero_image = pygame.transform.rotate(hero_image, 45)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))
    screen.blit(hero_image, (100, 100))
    pygame.display.flip()
    clock.tick(25)

pygame.quit()
