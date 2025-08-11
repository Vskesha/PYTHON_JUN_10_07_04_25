import pygame
from pathlib import Path

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Використання спрайтів")

sprite_path = Path(__file__).parent.joinpath("images/hero.jpg")
sprite_image = pygame.image.load(sprite_path)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = sprite_image
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

# Створення групи спрайтів та додавання нашого спрайта
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Оновлення спрайтів
    all_sprites.update()
    
    # Очищення екрану
    screen.fill((255, 255, 255))
    
    # Малювання спрайтів
    all_sprites.draw(screen)
    
    # Оновлення екрану
    pygame.display.flip()
    pygame.time.delay(5)

pygame.quit()
