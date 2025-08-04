import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Позиція миші")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
        
    mouse_position = pygame.mouse.get_pos()
    mouse_buttons = pygame.mouse.get_pressed()

    # if mouse_buttons[0]:
    #     pressed1 = "Натиснута"
    # else:
    #     pressed1 = "Не натиснута"
    pressed1 = "Натиснута" if mouse_buttons[0] else "Не натиснута"
    pressed2 = "Натиснута" if mouse_buttons[2] else "Не натиснута"

    font = pygame.font.Font(None, 36)

    text_position = font.render(f"Позиція миші: {mouse_position}", True, (0, 0, 0))
    screen.blit(text_position, (20, 20))

    text_button1 = font.render(f"Ліва кнопка: {pressed1}", True, (0, 0, 0))
    screen.blit(text_button1, (20, 60))

    text_button2 = font.render(f"Права кнопка: {pressed2}", True, (0, 0, 0))
    screen.blit(text_button2, (20, 100))

    pygame.display.flip()

pygame.quit()
