from collections import deque
import pygame
import random
import math


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# SETTINGS -----------------------------------------------
win_width = 1024    # ширина вікна
win_height = 768    # висота вікна
fps = 50            # frames per second (частота відтворення кадрів)

ball_radius = 30       # радіус м'ячика
ball_speed = 1         # стартова швидкість м'ячика
speed_multiplier = 1   # коефіцієнт збільшення швидкості м'ячика
max_speed = 5          # максимальна швидкість м'ячика
gravity = 0.4          # гравітація

circle_radius_decrease = 0.3       # зменшення радіуса кілець за кадр
circle_thickness = 3               # товщина кілець
distance_between_circles = 40      # відстань між кільцями
max_circle_rotation_speed = 0.015  # максимальна швидкість повороту кілець
circle_gap = math.pi / 3           # кут порожнини в кільці

# ---------------------------------------------------------
half_width = win_width // 2
half_height = win_height // 2
max_circle_radius = math.sqrt(half_height ** 2 + half_width ** 2)


class Circle:
    def __init__(
            self,
            x: int = half_width,
            y: int = half_height,
            radius: int = max_circle_radius,
            thickness: int = circle_thickness,
            color: tuple = None,
            rotation_speed: float = None,
            start_angle: float = None,
            gap: float = circle_gap,
        ) -> None: 

        self.x = x
        self.y = y
        self.center = (x, y)
        self.radius = radius
        self.thickness = thickness
        self.color = color or (
            random.randrange(0, 255), 
            random.randrange(0, 255), 
            random.randrange(0, 255)
        )
        self.rotation_speed = rotation_speed or random.uniform(
            -max_circle_rotation_speed, 
            max_circle_rotation_speed
        )
        self.start_angle = start_angle or random.uniform(0, 2 * math.pi)
        self.gap = gap

    def rotate(self) -> None:
        self.start_angle += self.rotation_speed
        if self.start_angle > 2 * math.pi:
            self.start_angle -= 2 * math.pi
        elif self.start_angle < 0:
            self.start_angle += 2 * math.pi

    def draw(self) -> None:
        rect = pygame.Rect(
            self.x - self.radius,
            self.y - self.radius,
            self.radius * 2,
            self.radius * 2,
        )
   
        pygame.draw.arc(
            screen,
            self.color,
            rect,
            self.start_angle,
            self.start_angle + 2 * math.pi - self.gap,
            self.thickness,
        )
    
    def decrease_radius(self) -> None:
        self.radius -= circle_radius_decrease


class Ball:
    def __init__(self, x: int, y: int, radius: int, speed: float, angle: float) -> None:
        
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.angle = angle
        self.x_velocity = self.speed * math.cos(self.angle)
        self.y_velocity = self.speed * math.sin(self.angle)

    def draw(self):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius)
    
    def move(self) -> None:
        self.x += self.x_velocity
        self.y += self.y_velocity
        self.y_velocity += gravity
    
    def check_collision_with(self, circle: Circle):
        
        distance = circle.radius - self.radius - math.sqrt(
            (self.x - circle.x) ** 2 + (self.y - circle.y) ** 2
        )

        return distance <= 0
    
    def passes_through(self, circle: Circle) -> bool:
        dx = self.x - circle.x
        dy = circle.y - self.y
        angle = math.degrees(math.atan2(dy, dx))
        if angle < 0:
            angle += 360
        start = math.degrees(circle.start_angle)
        end = start - math.degrees(circle.gap)
        # print(f"angle - {angle:>5.2f}, start - {start:>5.2f}, end - {end:>5.2f}")
        if end < angle < start:
            return True
        if end < 0 and end < angle - 360 < start:
            return True

        return False
    
    def reflect_from(self, circle: Circle):
        dx = self.x - circle.x
        dy = self.y - circle.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        norm_dx = dx / distance
        norm_dy = dy / distance

        dot = norm_dx * self.x_velocity + norm_dy * self.y_velocity

        self.y_velocity -= 2 * dot * norm_dy
        self.y_velocity = min(max_speed, self.y_velocity)
        self.x_velocity -= 2 * dot * norm_dx - self.y_velocity * 0.015

        overlap = distance + self.radius - circle.radius
        ball.x -= norm_dx * overlap
        ball.y -= norm_dy * overlap

    def increase_speed(self, multiplier: float) -> None:
        self.x_velocity *= multiplier
        self.y_velocity *= multiplier


pygame.init()
screen = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Baller")

clock = pygame.time.Clock()

ball = Ball(
    random.randint(half_width - 50, half_width + 50),
    random.randint(half_height - 50, half_height + 50),
    ball_radius,
    ball_speed,
    random.uniform(0, math.pi * 2)
)

circles = deque()
cr = max_circle_radius
for _ in range(10):
    circles.appendleft(Circle(radius=cr))
    cr -= distance_between_circles

running = True
distance = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    distance += circle_radius_decrease
    if not circles or distance >= distance_between_circles:
        circles.append(Circle())
        distance = 0

    screen.fill(BLACK)

    while circles[0].radius < 50:
        circles.popleft()
    
    for circle in circles:
        circle.draw()
        circle.decrease_radius()
        circle.rotate()

    ball.move()

    if ball.check_collision_with(circles[0]):
        ball.increase_speed(speed_multiplier)
        if ball.passes_through(circles[0]):
            circles.popleft()
        else:
            ball.reflect_from(circles[0])

    ball.draw()
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
