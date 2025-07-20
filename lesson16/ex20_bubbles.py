"""
Намалюйте на екрані п’ять кіл різного кольору, які 
змінюють свій розмір при натисканні клавіш зі стрілками.
"""

import pygame
import random

width, height = 1024, 768
max_speed = 5
number_of_circles = 8
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Анімація кольорових кругів")

circles = []
for i in range(number_of_circles):
    radius = random.randint(30, 50)
    circle = {"radius": radius}
    circle["x"] = random.randint(radius, width - radius)
    circle["y"] = random.randint(radius, height - radius)
    circle["speed_x"] = random.randint(-max_speed, max_speed)
    circle["speed_y"] = random.randint(-max_speed, max_speed)
    circle["color"] = (random.randint(0, 255),
                       random.randint(0, 255),
                       random.randint(0, 255))
    circles.append(circle)

selected = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                circles[selected]["color"] = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                )
            if event.key == pygame.K_LEFT:
                selected = (selected - 1) % number_of_circles
            if event.key == pygame.K_RIGHT:
                selected = (selected + 1) % number_of_circles
            if event.key == pygame.K_UP:
                circles[selected]["radius"] += 5
            if event.key == pygame.K_DOWN:
                circles[selected]["radius"] -= 5

    screen.fill(BLACK)

    for i, circle in enumerate(circles):
        pygame.draw.circle(screen, 
                           circle["color"], 
                           (circle["x"], circle["y"]), 
                           circle["radius"])

        if i == selected:
            pygame.draw.circle(screen,
                               WHITE,
                               (circle["x"], circle["y"]), 
                               circle["radius"] + 2,
                               5)

        circle["x"] += circle["speed_x"]
        circle["y"] += circle["speed_y"]
        
        if circle["x"] - circle["radius"] < 0:
            circle["speed_x"] *= -1
            circle["x"] = circle["radius"]

        if circle["x"] + circle["radius"] > width:
            circle["speed_x"] *= -1
            circle["x"] = width - circle["radius"]

        if circle["y"] - circle["radius"] < 0:
            circle["speed_y"] *= -1
            circle["y"] = circle["radius"]

        if circle["y"] + circle["radius"] > height:
            circle["speed_y"] *= -1
            circle["y"] = height - circle["radius"]

        for j in range(i + 1, number_of_circles):
            dx = circles[i]["x"] - circles[j]["x"]
            dy = circles[i]["y"] - circles[j]["y"]
            distance = (dx ** 2 + dy ** 2) ** 0.5

            if distance < circles[i]["radius"] + circles[j]["radius"]:
                vx1, vy1 = circles[i]["speed_x"], circles[i]["speed_y"]
                vx2, vy2 = circles[j]["speed_x"], circles[j]["speed_y"]
                dx = circles[i]["x"] - circles[j]["x"]
                dy = circles[i]["y"] - circles[j]["y"]

                distance = (dx ** 2 + dy ** 2) ** 0.5

                nx, ny = dx / distance, dy / distance
                tx, ty = -ny, nx

                v1n = vx1 * nx + vy1 * ny
                v1t = vx1 * tx + vy1 * ty

                v2n = vx2 * nx + vy2 * ny
                v2t = vx2 * tx + vy2 * ty

                v1n_after = v2n
                v2n_after = v1n

                circles[i]["speed_x"] = v1n_after * nx + v1t * tx
                circles[i]["speed_y"] = v1n_after * ny + v1t * ty

                circles[j]["speed_x"] = v2n_after * nx + v2t * tx
                circles[j]["speed_y"] = v2n_after * ny + v2t * ty

                overlap = 0.5 * (circles[i]["radius"] + circles[j]["radius"] - distance + 1)
                circles[i]["x"] += overlap * nx
                circles[i]["y"] += overlap * ny
                circles[j]["x"] -= overlap * nx
                circles[j]["y"] -= overlap * ny

    pygame.display.flip()
    pygame.time.delay(20)

pygame.quit()
