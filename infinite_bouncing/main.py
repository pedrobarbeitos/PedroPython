
import pygame
import random


pygame.init()
window = pygame.display.set_mode((640, 480))

ball = pygame.image.load("ball.png")

x = 0
y = 0
velocityX = 2
velocityY = 2
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    window.blit(ball, (x, y))

    pygame.display.flip()

    x += velocityX
    y += velocityY
    if x + ball.get_width() >= 640:
        velocityX = -velocityX

    if x <= 0:
        velocityX = -velocityX

    if y + ball.get_height() >= 480:
        velocityY = -velocityY

    if y <= 0:
        velocityY = -velocityY

    clock.tick(60)
