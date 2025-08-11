import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Логіка гри на основі умов")

# Кольори
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Об'єкти
player = pygame.Rect(100, 100, 50, 50)
obstacle = pygame.Rect(300, 300, 50, 50)
goal = pygame.Rect(random.randint(0, 750), random.randint(0, 550), 50, 50)

# Швидкість руху
speed = 5
# Лічильник очок
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    # Умови для взаємодії з об'єктами гри
    if player.colliderect(obstacle):
        player.x, player.y = 100, 100  # Повертаємо гравця на стартову позицію
        score = 0  # Скидаємо очки
    elif player.colliderect(goal):
        goal.x, goal.y = random.randint(0, 750), random.randint(0, 550)  # Переміщуємо ціль на нову позицію
        score += 1  # Додаємо очко

    # Очищення екрану та малювання об'єктів
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, player)
    pygame.draw.rect(screen, RED, obstacle)
    pygame.draw.rect(screen, YELLOW, goal)

    # Відображення очок
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, BLUE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    pygame.time.delay(5)

pygame.quit()
