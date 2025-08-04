import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Взаємодія з мишею")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("Ліва кнопка миші натиснута")
            elif event.button == 3:
                print("Права кнопка миші натиснута")
        elif event.type == pygame.MOUSEMOTION:
            mouse_position = event.pos
            print("Позиція миші:", mouse_position)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                print("Ліва кнопка миші відпущена")
            elif event.button == 3:
                print("Права кнопка миші відпущена")

    screen.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()
