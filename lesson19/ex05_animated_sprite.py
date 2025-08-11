import pygame
from pathlib import Path

pygame.init()
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Викориистання спрайтів")

sprites_folder = Path(__file__).parent.joinpath("images/bird")
sprite_images = []

for i in range(26):
    image_path = sprites_folder.joinpath(f"frame_{i:0>2}_delay-0.04s.gif")
    image = pygame.image.load(image_path)
    sprite_images.append(image)


class AnimatedPlayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = sprite_images
        self.current_image_idx = 0
        self.image = self.images[self.current_image_idx]
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)

    def update(self):
        current_time = pygame.time.get_ticks()
        frame_time = 50
        total_frames = current_time // frame_time
        self.current_image_idx = total_frames % len(self.images)
        self.image = self.images[self.current_image_idx]

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 1
        if keys[pygame.K_RIGHT]:
            self.rect.x += 1
        if keys[pygame.K_UP]:
            self.rect.y -= 1
        if keys[pygame.K_DOWN]:
            self.rect.y += 1


player = AnimatedPlayer()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    all_sprites.update()

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    pygame.time.delay(5)

pygame.quit()
