import pygame
import sys
from pathlib import Path

WIDTH, HEIGHT = 400, 600
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Анімація зображення")

bgfolder = Path(__file__).parent.joinpath("images/homer")
frames = []

for i in range(10):
    frame_path = bgfolder.joinpath(f"frame_{i:0>2}_delay-0.01s.gif")
    frame = pygame.image.load(frame_path)
    frames.append(frame)

frame_index = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    bg_image = frames[frame_index]
    frame_index = (frame_index + 1) % len(frames)
    rect = bg_image.get_rect()
    rect.center = (screen.get_width() / 2, screen.get_height() / 2)
    screen.blit(bg_image, rect)

    pygame.display.flip()
    pygame.time.delay(60)
