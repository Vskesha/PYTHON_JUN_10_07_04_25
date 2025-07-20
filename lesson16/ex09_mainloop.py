# https://www.w3schools.com/colors/colors_picker.asp
import pygame
import time
from pathlib import Path

pygame.init()

pygame.display.set_caption("Моя перша гра")
screen = pygame.display.set_mode((800, 600))

icon_image_path = Path(__file__).parent.joinpath("images/cat.png")
icon_image = pygame.image.load(icon_image_path)
pygame.display.set_icon(icon_image)

screen.fill((0, 0, 255))
pygame.display.flip()

font = pygame.font.SysFont("Arial", 36)
text = font.render("Hello, gamers!", True, (255, 255, 255))
screen.blit(text, (50, 50))
pygame.display.flip()

bg_image_path = Path(__file__).parent.joinpath("images/bg_cat.png")
bg_image = pygame.image.load(bg_image_path)
# bg_image = pygame.transform.smoothscale(bg_image, (600, 600))
screen.blit(bg_image, (100, 0))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time.sleep(0.1)

pygame.quit()
