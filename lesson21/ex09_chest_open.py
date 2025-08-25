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

chest = pygame.Rect(650, 450, 100, 100)
chest_opened = False

speed = 10
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
    if keys[pygame.K_SPACE]:
        if hero_rect.colliderect(chest) and not chest_opened:
            chest_opened = True
    
    screen.fill((0, 0, 0))
    
    if chest_opened:
        pygame.draw.rect(screen, (0, 255, 0), chest)
    else:
        pygame.draw.rect(screen, (139, 69, 19), chest)

    screen.blit(hero_image, hero_rect)

    pygame.display.flip()
    clock.tick(25)

pygame.quit()
