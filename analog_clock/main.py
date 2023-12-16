import pygame
from datetime import datetime
import math

pygame.init()
display = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()


while True:

    display.fill((0, 0, 0))
    pygame.draw.circle(display, (255, 0, 0), (320, 240), 220, 5)
    pygame.draw.circle(display, (255, 0, 0), (320, 240), 10, 5)

    current_time = datetime.now().strftime("%H:%M:%S")
    pygame.display.set_caption(current_time)
    hours, minutes, seconds = current_time.split(":")
    seconds = int(seconds)
    minutes = int(minutes)
    hours = int(hours)

    # seconds
    angleS = (seconds / 60) * (2 * math.pi)
    xS = 320 + math.cos(angleS - math.pi/2) * 200
    yS = 240 + math.sin(angleS - math.pi/2) * 200
    pygame.draw.line(display, (0, 0, 255), (320, 240), (xS, yS), 2)

    # minutes
    angleM = (minutes / 60) * (2 * math.pi)
    xM = 320 + math.cos(angleM - math.pi/2) * 200
    yM = 240 + math.sin(angleM - math.pi/2) * 200
    pygame.draw.line(display, (0, 0, 255), (320, 240), (xM, yM), 3)

    # hours
    hours = hours % 12 + minutes / 60
    angleH = (hours / 12) * (2 * math.pi)
    xH = 320 + math.cos(angleH - math.pi/2) * 150
    yH = 240 + math.sin(angleH - math.pi/2) * 150
    pygame.draw.line(display, (0, 0, 255), (320, 240), (xH, yH), 5)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    clock.tick(60)
