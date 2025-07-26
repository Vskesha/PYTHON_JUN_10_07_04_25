import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Комбінації клавіш")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
        if keys[pygame.K_c]:
            print("Комбінація Ctrl+C натиснута")
    
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            print("Комбінація Ctrl+Shift натиснута")
    
    if keys[pygame.K_LALT] or keys[pygame.K_RALT]:
        if keys[pygame.K_F4]:
            print("Комбінація Alt+F4 натиснута")
            running = False

    screen.fill((0, 0, 0))
    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()
