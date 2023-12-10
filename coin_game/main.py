# Complete your game here
import pygame
import random


class Survive:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("SURVIVAL")

        self.clock = pygame.time.Clock()
        self.game_font = pygame.font.SysFont("Arial", 24)
        self.game_font_small = pygame.font.SysFont("Arial", 16)

        self.points = 0
        self.difficulty = 200
        self.text_points = self.game_font.render(
            f"Points: {self.points}", True, (255, 0, 0))

        self.game_state = "start"

        self.window = pygame.display.set_mode((800, 600))
        self.robot = pygame.image.load("robot.png").convert_alpha()
        self.coin = pygame.image.load("coin.png").convert_alpha()
        self.monster = pygame.image.load("monster.png").convert_alpha()

        self.x = 400 - self.robot.get_width()/2
        self.y = 250
        self.coin_x = 700
        self.coin_y = 300
        self.line_x = 400

        self.to_right = False
        self.to_left = False
        self.to_up = False
        self.to_down = False

        self.monsters = [self.create_monsters() for _ in range(5)]

        self.game_loop()

    def game_loop(self):
        while True:
            if self.game_state == "start":
                self.start_screen()
            elif self.game_state == "main":
                self.main_loop()
            elif self.game_state == "death":
                self.death_screen()
            else:
                break  # Exit the game loop if the state is not recognized

    def start_screen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.game_state = "main"

        self.window.fill((0, 0, 0))

        start_description1 = self.game_font_small.render(
            "Welcome to Survival, where feeding coins to your robot is a matter of life and pixelated death!", True, (255, 255, 255))
        start_description1_rect = start_description1.get_rect(
            center=(400, 80))

        start_description2 = self.game_font_small.render(
            "Monsters and mayhem await. Dodge death and collect coins, or face the high-score hall of shame!", True, (255, 255, 255))
        start_description2_rect = start_description2.get_rect(
            center=(400, 120))

        start_description3 = self.game_font_small.render(
            "Brace for escalating chaos as each coin grab and monster dodge cranks up the difficulty dial to 'impossible'!", True, (255, 255, 255))
        start_description3_rect = start_description3.get_rect(
            center=(400, 160))

        start_description4 = self.game_font_small.render(
            "Press enter when ready and start the coin-chomping, monster-dodging dance of doom!", True, (255, 255, 255))
        start_description4_rect = start_description4.get_rect(
            center=(400, 200))

        start_description5 = self.game_font_small.render(
            "A random game by Pedro Barbeitos", True, (255, 255, 255))
        start_description5_rect = start_description5.get_rect(
            center=(400, 550))

        start_text = self.game_font.render(
            "Press Enter to Start", True, (255, 255, 255))
        start_text_rect = start_text.get_rect(
            center=(400, 400))

        self.window.blit(start_text, start_text_rect)
        self.window.blit(start_description1, start_description1_rect)
        self.window.blit(start_description2, start_description2_rect)
        self.window.blit(start_description3, start_description3_rect)
        self.window.blit(start_description4, start_description4_rect)
        self.window.blit(start_description5, start_description5_rect)
        self.window.blit(self.robot, (400 - self.robot.get_width()/2, 250))

        pygame.display.flip()
        self.clock.tick(60)

    def death_screen(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.reset_game()

        self.window.fill((0, 0, 0))

        final_points = self.game_font.render(
            f"{self.points} POINTS", True, (255, 255, 255))
        final_points_rect = final_points.get_rect(
            center=(400, 100))

        start_description1 = self.game_font_small.render(
            f"A mere {self.points} points. Did you mistake the monsters for a welcoming committee?", True, (255, 255, 255))
        start_description1_rect = start_description1.get_rect(
            center=(400, 150))

        start_description2 = self.game_font_small.render(
            "That's not a high score, it's a cry for a do-over!", True, (255, 255, 255))
        start_description2_rect = start_description2.get_rect(
            center=(400, 190))

        start_text = self.game_font.render(
            "Press Enter to go again", True, (255, 255, 255))
        start_text_rect = start_text.get_rect(
            center=(400, 400))

        self.window.blit(final_points, final_points_rect)
        self.window.blit(start_text, start_text_rect)
        self.window.blit(start_description1, start_description1_rect)
        self.window.blit(start_description2, start_description2_rect)
        self.window.blit(self.robot, (400 - self.robot.get_width()/2, 250))

        pygame.display.flip()
        self.clock.tick(60)

    def reset_game(self):
        self.points = 0
        self.line_x = 400
        self.x = 400 - self.robot.get_width()/2
        self.y = 250
        self.difficulty = 200
        self.monsters = [self.create_monsters() for _ in range(5)]
        self.text_points = self.game_font.render(
            f"Points: {self.points}", True, (255, 0, 0))
        self.to_right = False
        self.to_left = False
        self.to_up = False
        self.to_down = False
        self.game_state = "main"

    def create_monsters(self):
        side = random.choice(['top', 'bottom', 'left', 'right'])
        if side == 'top':
            return {"x": random.randint(0, 800 - self.monster.get_width()), "y": 0, "x_velocity": 0, "y_velocity": 1}
        elif side == 'bottom':
            return {"x": random.randint(0, 800 - self.monster.get_width()), "y": 600, "x_velocity": 0, "y_velocity": -1}
        elif side == 'left':
            return {"x": 0, "y": random.randint(0, 600 - self.monster.get_height()), "x_velocity": 1, "y_velocity": 0}
        elif side == 'right':
            return {"x": 800, "y": random.randint(0, 600 - self.monster.get_height()), "x_velocity": -1, "y_velocity": 0}

    def main_loop(self):
        for event in pygame.event.get():
            self.check_events(event)

        self.robot_position()
        self.update_monsters()
        self.check_colisions()
        self.check_monster_collisions()
        self.increase_difficulty()
        self.draw_window()
        self.line_x -= 1

        if self.line_x <= 10:
            self.game_state = "death"

        pygame.display.flip()
        self.clock.tick(60)

    def update_monsters(self):

        if random.randint(1, self.difficulty) == 1:
            self.monsters.append(self.create_monsters())

        for monster_info in self.monsters[:]:
            monster_info["x"] += monster_info["x_velocity"]
            monster_info["y"] += monster_info["y_velocity"]

            if (monster_info["x"] < 0 or monster_info["x"] > 800 or
                    monster_info["y"] < 0 or monster_info["y"] > 600):
                self.monsters.remove(monster_info)

    def check_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.to_left = True
            elif event.key == pygame.K_RIGHT:
                self.to_right = True
            elif event.key == pygame.K_UP:
                self.to_up = True
            elif event.key == pygame.K_DOWN:
                self.to_down = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.to_left = False
            elif event.key == pygame.K_RIGHT:
                self.to_right = False
            elif event.key == pygame.K_UP:
                self.to_up = False
            elif event.key == pygame.K_DOWN:
                self.to_down = False

        elif event.type == pygame.QUIT:
            pygame.quit()
            exit()

    def robot_position(self):
        if self.x <= (800 - self.robot.get_width()) and self.to_right:
            self.x += 2
        if self.x >= 0 and self.to_left:
            self.x -= 2
        if self.y >= 40 and self.to_up:
            self.y -= 2
        if self.y <= (600 - self.robot.get_height()) and self.to_down:
            self.y += 2

    def check_colisions(self):
        robot_rect = pygame.Rect(
            self.x, self.y, self.robot.get_width(), self.robot.get_height())
        coin_rect = pygame.Rect(self.coin_x, self.coin_y,
                                self.coin.get_width(), self.coin.get_height())

        if robot_rect.colliderect(coin_rect):
            self.coin_x = random.randint(100, 700)
            self.coin_y = random.randint(100, 500)
            self.points += 1
            self.line_x = 400
            self.text_points = self.game_font.render(
                f"Points: {self.points}", True, (255, 0, 0))

    def check_monster_collisions(self):
        robot_rect = pygame.Rect(
            self.x + 8, self.y + 8, self.robot.get_width() - 8, self.robot.get_height() - 8)

        for monster_info in self.monsters:
            monster_rect = pygame.Rect(
                monster_info["x"] + 8, monster_info["y"] + 8, self.monster.get_width() - 8, self.monster.get_height() - 8)

            if robot_rect.colliderect(monster_rect):
                self.game_state = "death"
                break

    def increase_difficulty(self):
        if self.points > 5 and self.points < 10:
            self.difficulty = 100
        if self.points > 10 and self.points < 20:
            self.difficulty = 75
        if self.points > 20 and self.points < 30:
            self.difficulty = 40
        if self.points > 30 and self.points < 40:
            self.difficulty = 20

    def draw_window(self):
        self.window.fill((128, 128, 128))
        self.window.blit(self.coin, (self.coin_x, self.coin_y))
        self.window.blit(self.robot, (self.x, self.y))

        for monster_info in self.monsters:
            self.window.blit(
                self.monster, (monster_info["x"], monster_info["y"]))

        pygame.draw.rect(self.window, (0, 100, 0), (0, 0, 800, 40))
        pygame.draw.rect(self.window, (255, 0, 0), (10, 13, 400, 12), 1)
        pygame.draw.line(self.window, (255, 0, 0),
                         (10, 18), (self.line_x, 18), 10)

        self.window.blit(self.text_points, (650, 7))

        pygame.display.flip()


if __name__ == "__main__":
    Survive()
