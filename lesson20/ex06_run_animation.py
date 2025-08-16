import pygame
import sys
from pathlib import Path

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Анімація бігу")

images_folder = Path(__file__).parent.joinpath(
    "images/sonic"
)
run_images = []
for i in range(8):
    image_path = images_folder.joinpath(f"sonic{i}.png")
    frame = pygame.image.load(image_path)
    run_images.append(frame)
run_idx = 0
image_rect = run_images[0].get_rect()
image_rect.center = (400, 300)

clock = pygame.time.Clock()
fps = 60

RUNNING_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(RUNNING_EVENT, 65)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == RUNNING_EVENT:
            run_idx = (run_idx + 1) % len(run_images)
    
    screen.fill((0, 0, 0))
    screen.blit(run_images[run_idx], image_rect)
    pygame.display.flip()
    clock.tick(fps)
