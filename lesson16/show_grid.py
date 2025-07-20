import pygame

width, height = 800, 600
step = 100
WHITE = (255, 255, 255)
font_height = 20

pygame.init()
font = pygame.font.SysFont("Courier", font_height)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Coordinate Grid")

for x in range(0, width, step):
    pygame.draw.line(screen, WHITE, (x, 0), (x, height))
    text = font.render(str(x), True, WHITE)
    screen.blit(text, (x - font_height // 2, 0))

for y in range(0, height, step):
    pygame.draw.line(screen, WHITE, (0, y), (width, y))
    text = font.render(str(y), True, WHITE)
    screen.blit(text, (0, y))

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
