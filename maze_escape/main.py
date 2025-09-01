import pygame

pygame.init()

# Створення вікна гри
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Втеча з лабіринту')

# Фоновий колір
background_color = (0, 0, 0)  # Чорний колір фону

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заповнюємо екран фоном
    screen.fill(background_color)

    # Оновлюємо екран
    pygame.display.flip()

pygame.quit()
