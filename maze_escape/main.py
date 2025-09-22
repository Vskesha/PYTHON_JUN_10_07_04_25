import pygame
import random
from pathlib import Path

from maze_generator import generate_maze

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("maze")

bg_color = (0, 0, 0)


assets_folder = Path(__file__).parent.joinpath("assets")

# pygame.mixer.music.load(assets_folder.joinpath("background.mp3"))
# pygame.mixer.music.set_volume(0.3)
# pygame.mixer.music.play(-1)

sound_key = pygame.mixer.Sound(assets_folder.joinpath("sound_key.mp3"))
pygame.mixer.music.set_volume(1)

sound_door = pygame.mixer.Sound(assets_folder.joinpath("sound_door.mp3"))
pygame.mixer.music.set_volume(1)

background_img = pygame.image.load(assets_folder.joinpath("background.png"))
background_img = pygame.transform.scale(background_img, (800, 600))


def draw_button(screen, text, color, x, y, w, h):
    pygame.draw.rect(screen, color, (x, y, w, h))
    font = pygame.font.SysFont(None, 36)
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(
        text_surface,
        (
            x + (w - text_surface.get_width()) / 2,
            y + (h - text_surface.get_height()) / 2
        )
    )


def main_menu():
    menu_is_running = True
    while menu_is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_is_running = False
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 150 <= x <= 650 and 200 <= y <= 300:
                    menu_is_running = False
                if 150 <= x <= 650 and 350 <= y <= 450:
                    menu_is_running = False
                    exit()
            
        screen.blit(background_img, (0, 0))
        draw_button(screen, "Почати гру", (0, 150, 0), 150, 200, 500, 100)
        draw_button(screen, "Вийти", (200, 0, 0), 150, 350, 500, 100)
        pygame.display.flip()


def win_menu(final_text):
    win_menu_is_running = True
    while win_menu_is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                win_menu_is_running = False
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 150 <= x <= 650 and 350 <= y <= 450:
                    win_menu_is_running = False
                    exit()
            

        screen.blit(background_img, (0, 0))
        draw_button(screen, final_text, (0, 150, 0), 150, 200, 500, 100)
        draw_button(screen, "Вийти", (200, 0, 0), 150, 350, 500, 100)
        pygame.display.flip()


def level(level_number):
    start_time = pygame.time.get_ticks()
    maze_h = 9 + level_number * 2
    maze_w = maze_h * 4 // 3
    
    maze = generate_maze(maze_h, maze_w)
    cell_size = min(
        600 / maze_h,
        800 / maze_w
    )

    wall_img = pygame.image.load(assets_folder.joinpath("wall.png"))
    key_img = pygame.image.load(assets_folder.joinpath("key.png"))
    door_img = pygame.image.load(assets_folder.joinpath("door.png"))
    dog_img = pygame.image.load(assets_folder.joinpath("dog.png"))
    fog_img = pygame.image.load(assets_folder.joinpath("fog.png"))
    player_img = [pygame.image.load(assets_folder.joinpath(f"player{i}.png")) for i in range(1, 5)]


    wall_img = pygame.transform.scale(wall_img, (cell_size, cell_size))
    key_img = pygame.transform.scale(key_img, (cell_size, cell_size))
    door_img = pygame.transform.scale(door_img, (cell_size, cell_size))
    dog_img = pygame.transform.scale(dog_img, (cell_size, cell_size))
    fog_img = pygame.transform.scale(fog_img, (cell_size, cell_size))
    player_img = [pygame.transform.scale(player, (cell_size, cell_size)) for player in player_img]


    player_id = 0
    height = len(maze)
    width = len(maze[0])

    free_cells = []
    for y in range(height):
        for x in range(width):
            if maze[y][x] == 0:
                free_cells.append((x, y))

    cells_left = free_cells[1:-1]
    key_position = random.choice(cells_left)
    cells_left.remove(key_position)
    fake_door_position = random.choice(cells_left)
    
    fdy, fdx = fake_door_position
    for y, x in (
        (fdy - 1, fdx),
        (fdy + 1, fdx),
        (fdy, fdx + 1),
        (fdy, fdx - 1)
    ):
        if (y, x) in cells_left:
            dog_position = (y, x)
            break

    door_position = free_cells[-1]
    player_x, player_y = free_cells[0]
    has_key = False
    can_break_wall = True

    visible_cells = set()
    visible_radius = max(6 - level_number, 1)

    clock = pygame.time.Clock()
    fps = 15

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and player_x > 0 and maze[player_y][player_x - 1] == 0:
                    player_x -= 1
                if event.key == pygame.K_RIGHT and player_x < width - 1 and maze[player_y][player_x + 1] == 0:
                    player_x += 1
                if event.key == pygame.K_UP and player_y > 0 and maze[player_y - 1][player_x] == 0:
                    player_y -= 1
                if event.key == pygame.K_DOWN and player_y < height - 1 and maze[player_y + 1][player_x] == 0:
                    player_y += 1
                if event.key == pygame.K_SPACE and pygame.time.get_ticks() - start_time > 20000 and can_break_wall:
                    can_break_wall = False
                    for y, x in (
                        (player_y - 1, player_x),
                        (player_y + 1, player_x),
                        (player_y, player_x + 1),
                        (player_y, player_x - 1)
                    ):  
                        maze[y][x] = 0

        screen.fill(bg_color)

        visible_cells.clear()
        for y in range(player_y - visible_radius, player_y + visible_radius + 1):
            for x in range(player_x - visible_radius, player_x + visible_radius + 1):
                visible_cells.add((x, y))
        
        for y in range(height):
            for x in range(width):
                if maze[y][x] == 1:
                    screen.blit(wall_img, (x * cell_size, y * cell_size))

        if not has_key:
            if (player_x, player_y) == key_position:
                has_key = True
                sound_key.play()
            else:
                screen.blit(key_img, (key_position[0] * cell_size, key_position[1] * cell_size))

        screen.blit(door_img, (door_position[0] * cell_size, door_position[1] * cell_size))
        screen.blit(door_img, (fake_door_position[0] * cell_size, fake_door_position[1] * cell_size))
        
        screen.blit(dog_img, (dog_position[0] * cell_size, dog_position[1] * cell_size))
        
        screen.blit(player_img[player_id], (player_x * cell_size, player_y * cell_size))
        player_id = (player_id + 1) % len(player_img)
        
        for y in range(height):
            for x in range(width):
                if (x, y) not in visible_cells:
                    screen.blit(fog_img, (x * cell_size, y * cell_size))

        if (player_x, player_y) == dog_position:
            return True

        if has_key and (player_x, player_y) == door_position:
            sound_door.play()
            running = False

        pygame.display.flip()
        clock.tick(fps)


main_menu()

for i in range(1, 11):
    if level(i):
        win_menu("Ти програв")
        break
else:
    win_menu("Вітаю! Ти пройшов лабіринт")

pygame.quit()
