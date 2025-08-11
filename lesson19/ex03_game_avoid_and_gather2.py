import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Гра з різними сценаріями реакцій на події")

# Кольори
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Об'єкти
player = pygame.Rect(350, 250, 50, 50)
target = pygame.Rect(400, 300, 50, 50)
obstacle = pygame.Rect(200, 150, 50, 50)

# Швидкість руху
speed = 5

# Стан гри
game_over = False

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

    # Умовні реакції
    if player.colliderect(target):
        game_over = True

    if player.colliderect(obstacle):
        player.x = 350
        player.y = 250

    screen.fill(WHITE)
    
    if game_over:
        font = pygame.font.Font(None, 74)
        text = font.render("YOU WIN!", True, GREEN)
        screen.blit(text, (200, 250))
    else:
        pygame.draw.rect(screen, GREEN, player)
        pygame.draw.rect(screen, BLUE, target)
        pygame.draw.rect(screen, RED, obstacle)
    
    pygame.display.flip()
    pygame.time.delay(5)

pygame.quit()
