import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Обробка натискання клавіш")

font = pygame.font.Font(None, 50)
text = ""

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                text = "Натиснуто стрілку вліво"
            elif event.key == pygame.K_RIGHT:
                text = "Натиснуто стрілку вправо"
            elif event.key == pygame.K_UP:
                text = "Натиснуто стрілку вгору"
            elif event.key == pygame.K_DOWN:
                text = "Натиснуто стрілку вниз"
            elif event.key == pygame.K_SPACE:
                text = "Натиснуто пробіл"

    screen.fill((0, 0, 0))
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (400, 300)
    screen.blit(text_surface, text_rect)

    pygame.display.flip()

pygame.quit()
