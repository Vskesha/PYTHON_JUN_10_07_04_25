# https://www.w3schools.com/colors/colors_picker.asp
import pygame
import time
from pathlib import Path

pygame.init()

pygame.display.set_caption("Моя перша гра")
screen = pygame.display.set_mode((800, 600))

image_path = Path(__file__).parent.joinpath("images/cat.png")
icon_image = pygame.image.load(image_path)
pygame.display.set_icon(icon_image)

screen.fill((0, 0, 255))
pygame.display.flip()

font = pygame.font.SysFont("Courier", 36)
# font_file_path = Path(__file__).parent.joinpath("fonts/turok.ttf")
# font = pygame.font.Font(font_file_path, 36)
text = font.render("Hello, gamers!", True, (255, 255, 255))
screen.blit(text, (50, 50))
pygame.display.flip()

time.sleep(25)
pygame.quit()
