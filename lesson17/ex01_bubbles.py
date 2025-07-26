import pygame
import random

width, height = 800, 600
max_speed = 5

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Анімація кольорових кругів")

circles = []
for i in range(5):
    circle = {}
    radius = random.randint(30, 50)
    
    circle["radius"] = radius
    circle["x"] = random.randint(radius, width - radius)
    circle["y"] = random.randint(radius, height - radius)
    circle["speed_x"] = random.randint(-max_speed, max_speed)
    circle["speed_y"] = random.randint(-max_speed, max_speed)
    circle["color"] = (random.randint(0, 255),
                       random.randint(0, 255),
                       random.randint(0, 255))
    circles.append(circle)

print(*circles, sep="\n")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for circle in circles:
        pygame.draw.circle(screen, 
                           circle["color"], 
                           (circle["x"], circle["y"]), 
                           circle["radius"])
        circle["x"] += circle["speed_x"]
        circle["y"] += circle["speed_y"]
    
        if (circle["x"] - circle["radius"] < 0 
                or circle["x"] + circle["radius"] > width):
            circle["speed_x"] *= -1
        
        if (circle["y"] - circle["radius"] < 0 
                or circle["y"] + circle["radius"] > height):
            circle["speed_y"] *= -1
    
    pygame.display.flip()
    pygame.time.delay(20)

pygame.quit()
