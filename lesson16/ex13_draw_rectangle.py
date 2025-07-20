import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Малювання прямокутника")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    
    pygame.draw.rect(screen, (255, 0, 0), (200, 150, 400, 300), 5)
    pygame.display.flip()

pygame.quit()
