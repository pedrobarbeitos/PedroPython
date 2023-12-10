# WRITE YOUR SOLUTION HERE:

# # WRITE YOUR SOLUTION HERE:

# WRITE YOUR SOLUTION HERE:

# WRITE YOUR SOLUTION HERE:

# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:

import pygame
import random


# Initialize
pygame.init()
window = pygame.display.set_mode((640, 480))

# Load image of roboto
ball = pygame.image.load("ball.png")

x = 0
y = 0
velocityX = 2
velocityY = 2
clock = pygame.time.Clock()


# Game Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Window Background color
    window.fill((0, 0, 0))

    # Draw my ball
    window.blit(ball, (x, y))

    # Update the display
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
