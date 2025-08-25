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

items = [
    pygame.Rect(600, 150, 100, 100),
    pygame.Rect(150, 400, 100, 100),
]
items_collected = 0

inventory = []

font = pygame.font.Font(None, 36)
speed = 10
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                if inventory:
                    used_item = inventory.pop(0)
                    print(f"Used: {used_item}")
            if event.key == pygame.K_d:
                if inventory:
                    dropped_item = inventory.pop()
                    x = hero_rect.x + hero_rect.width
                    y = hero_rect.y
                    items.append(pygame.Rect(x, y, 100, 100),)
                    print(f"Dropped: {dropped_item}")
    
    
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
            items_collected += 1
            inventory.append("Item")
    
    for item in items[:]:
        if hero_rect.colliderect(item):
            items.remove(item)
            items_collected += 1
            inventory.append("Item")

    screen.fill((255, 255, 255))
    
    if chest_opened:
        pygame.draw.rect(screen, (0, 255, 0), chest)
    else:
        pygame.draw.rect(screen, (139, 69, 19), chest)

    for item in items:
        pygame.draw.rect(screen, (255, 215, 0), item)

    screen.blit(hero_image, hero_rect)

    score_text = font.render(
        f"Items collected: {items_collected}",
        True,
        (0, 0, 0)
    )
    screen.blit(score_text, (10, 10))

    inventory_text = font.render(
        f"Inventory: {', '.join(inventory)}",
        True, 
        (0, 0, 0)
    )
    screen.blit(inventory_text, (10, 50))

    pygame.display.flip()
    clock.tick(25)

pygame.quit()
