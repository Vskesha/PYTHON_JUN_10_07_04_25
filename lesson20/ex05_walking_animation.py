import pygame
import sys
from pathlib import Path

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Анімація ходьби")

sprite_sheet_path = Path(__file__).parent.joinpath(
    "images/hero/hero_spritesheet.png"
)
sprite_sheet = pygame.image.load(sprite_sheet_path)
walk_images = []
for i in range(6):
    frame = sprite_sheet.subsurface((i * 80, 94, 80, 94))
    frame = pygame.transform.scale(frame, (160, 188))
    walk_images.append(frame)
walk_idx = 0
image_rect = walk_images[0].get_rect()
image_rect.center = (400, 300)

clock = pygame.time.Clock()
fps = 60

WALKING_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(WALKING_EVENT, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == WALKING_EVENT:
            walk_idx = (walk_idx + 1) % len(walk_images)
    
    screen.fill((0, 0, 0))
    screen.blit(walk_images[walk_idx], image_rect)
    pygame.display.flip()
    clock.tick(fps)
