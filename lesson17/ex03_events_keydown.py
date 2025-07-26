import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Обробка натискання клавіш")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("Натиснута клавіша вгору")
            elif event.key == pygame.K_DOWN:
                print("Натиснута клавіша вниз")

pygame.quit()
