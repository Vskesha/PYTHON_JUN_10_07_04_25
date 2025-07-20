import pygame
import time
from pathlib import Path

pygame.init()

pygame.display.set_caption("Моя перша гра")
screen = pygame.display.set_mode((800, 600))

image_path = Path(__file__).parent.joinpath("images/cat.png")
print(image_path)
icon_image = pygame.image.load(image_path)
pygame.display.set_icon(icon_image)

time.sleep(25)
pygame.quit()
