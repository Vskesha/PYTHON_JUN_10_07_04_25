import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

running = True
x_position = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), (x_position, 300, 50, 50))
    pygame.display.flip()

    x_position += 5
    if x_position > 800:
        x_position = 0

    pygame.time.delay(20)

pygame.quit()
