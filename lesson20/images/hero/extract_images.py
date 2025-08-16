import pygame
from pathlib import Path

pygame.init()

curr_folder = Path(__file__).parent
sprite_sheet_path = curr_folder.joinpath("hero_spritesheet.png")
sprite_sheet = pygame.image.load(sprite_sheet_path)

mul = 2
images = {}
images["idle.png"] = (10, 18, 66, 82)
images["jump.png"] = (174, 297, 238, 354)
images["crouch.png"] = (12, 397, 80, 451)
images["attack.png"] = (10, 209, 75, 274)
images["shoot.png"] = (202, 419, 210, 427)
images["bullet.png"] = (222, 421, 233, 425)

for filename, (x1, y1, x2, y2) in images.items():
    width = x2 - x1 + 1
    height = y2 - y1 + 1
    image = sprite_sheet.subsurface((x1, y1, width, height))
    image = pygame.transform.scale(image, (width * mul, height * mul))
    pygame.image.save(image, curr_folder.joinpath(filename))

pygame.quit()
