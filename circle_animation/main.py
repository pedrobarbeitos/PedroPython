# WRITE YOUR SOLUTION HERE:

import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

angle = 0
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    for r in range(10):
        robot_angle = angle + (r * 2 * math.pi / 10)
        x = 320 + math.cos(robot_angle) * 130 - robot.get_width() / 2
        y = 240 + math.sin(robot_angle) * 130 - robot.get_height() / 2

        window.blit(robot, (x, y))

    pygame.display.flip()

    angle += 0.01
    clock.tick(60)
