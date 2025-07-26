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
            if event.mod & pygame.KMOD_CTRL and event.key == pygame.K_c:
                print("Натиснуто Ctrl+C")
            if event.mod & pygame.KMOD_CTRL and event.key == pygame.K_v:
                print("Натиснуто Ctrl+V")
            elif event.mod & pygame.KMOD_SHIFT and event.key == pygame.K_SPACE:
                print("Натиснуто Shift+Space")

pygame.quit()
