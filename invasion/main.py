import pygame
import random

# Initialize
pygame.init()
window = pygame.display.set_mode((640, 480))

# Load image of robot
robot = pygame.image.load("robot.png")


def create_robot():
    return {"x": random.randint(0, 640 - robot.get_width()), "y": 0, "y_velocity": 2, "x_velocity": 0}


robots = [create_robot() for _ in range(random.randint(1, 15))]

clock = pygame.time.Clock()

# Game Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if random.randint(1, 20) == 1:
        robots.append(create_robot())

    # Window Background color
    window.fill((0, 0, 0))

    for robot_info in robots:
        window.blit(robot, (robot_info["x"], robot_info["y"]))
        robot_info["y"] += robot_info["y_velocity"]

        if robot_info["y"] + robot.get_height() >= 480 and robot_info["y_velocity"] != 0:
            robot_info["y"] = 480 - robot.get_height()
            robot_info["y_velocity"] = 0
            robot_info["x_velocity"] = random.choice(
                [-1, 1])

        if robot_info["y_velocity"] == 0:
            robot_info["x"] += robot_info["x_velocity"]

            if robot_info["x"] < -robot.get_width() or robot_info["x"] > 640:
                robots.remove(robot_info)

    # Update the display
    pygame.display.flip()
    clock.tick(60)
