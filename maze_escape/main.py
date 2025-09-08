import pygame
import random
from pathlib import Path

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("maze")

bg_color = (0, 0, 0)
cell_size = 40

assets_folder = Path(__file__).parent.joinpath("assets")

wall_img = pygame.image.load(assets_folder.joinpath("wall.png"))
wall_img = pygame.transform.scale(wall_img, (cell_size, cell_size))

key_img = pygame.image.load(assets_folder.joinpath("key.png"))
key_img = pygame.transform.scale(key_img, (cell_size, cell_size))

door_img = pygame.image.load(assets_folder.joinpath("door.png"))
door_img = pygame.transform.scale(door_img, (cell_size, cell_size))

player_img = [pygame.image.load(assets_folder.joinpath(f"player{i}.png")) for i in range(1, 5)]
player_img = [pygame.transform.scale(player, (cell_size, cell_size)) for player in player_img]
player_id = 0

pygame.display.set_icon(key_img)

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
height = len(maze)
width = len(maze[0])

free_cells = []
for y in range(height):
    for x in range(width):
        if maze[y][x] == 0:
            free_cells.append((x, y))

key_position = random.choice(free_cells[1:-1])
door_position = free_cells[-1]
player_x, player_y = free_cells[0]
has_key = False

clock = pygame.time.Clock()
fps = 15

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and player_x > 0 and maze[player_y][player_x - 1] == 0:
                player_x -= 1
            if event.key == pygame.K_RIGHT and player_x < width - 1 and maze[player_y][player_x + 1] == 0:
                player_x += 1
            if event.key == pygame.K_UP and player_y > 0 and maze[player_y - 1][player_x] == 0:
                player_y -= 1
            if event.key == pygame.K_DOWN and player_y < height - 1 and maze[player_y + 1][player_x] == 0:
                player_y += 1


    screen.fill(bg_color)
    
    for y in range(height):
        for x in range(width):
            if maze[y][x] == 1:
                screen.blit(wall_img, (x * cell_size, y * cell_size))

    if not has_key:
        if (player_x, player_y) == key_position:
            has_key = True
        else:
            screen.blit(key_img, (key_position[0] * cell_size, key_position[1] * cell_size))

    screen.blit(door_img, (door_position[0] * cell_size, door_position[1] * cell_size))

    screen.blit(player_img[player_id], (player_x * cell_size, player_y * cell_size))
    player_id = (player_id + 1) % len(player_img)
    
    if has_key and (player_x, player_y) == door_position:
        running = False

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
