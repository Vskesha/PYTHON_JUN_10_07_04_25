import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Збір кружечків")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

player = pygame.Rect(375, 275, 50, 50)

circles = []
for _ in range(10):
    x = random.randint(0, 750)
    y = random.randint(0, 550)
    circles.append(pygame.Rect(x, y, 50, 50))

score = 0
font = pygame.font.Font(None, 32)

CREATE_CIRCLE = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_CIRCLE, 500)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CREATE_CIRCLE:
            x = random.randint(0, 750)
            y = random.randint(0, 550)
            circles.append(pygame.Rect(x, y, 50, 50))
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5

    for circle in circles.copy():
        if player.colliderect(circle):
            circles.remove(circle)
            score += 1

    screen.fill(WHITE)
    
    for circle in circles:
        pygame.draw.ellipse(screen, BLUE, circle)

    pygame.draw.rect(screen, RED, player)

    score_text = font.render(f"Score: {score}", True, BLUE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    pygame.time.delay(25)    

pygame.quit()
