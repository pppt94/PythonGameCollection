import pygame
import random
from Source import text, screen

pygame.init()
clock = pygame.time.Clock()
fps = 5

# import graphics
syn = pygame.image.load('../Graphics/Snake/food_syntax.png')
imp = pygame.image.load('../Graphics/Snake/food_import.png')
ind = pygame.image.load('../Graphics/Snake/food_index.png')
nam = pygame.image.load('../Graphics/Snake/food_name.png')
typ = pygame.image.load('../Graphics/Snake/food_type.png')

foods = [imp, ind, nam, typ]
snake_size = 40


class Snake:

    def __init__(self):

        self.head_x = screen.scr_width / 2
        self.head_y = screen.scr_height / 2
        self.snake_size = 40
        self.snake_body = []
        self.snake_length = 1
        self.head_direction = "UP"
        self.head_img = pygame.image.load('../Graphics/Snake/snake_head.png')
        self.head = self.head_img
        self.body_img = pygame.image.load('../Graphics/Snake/snake_body.png')
        self.body = self.body_img
        self.curves_img = pygame.image.load('../Graphics/Snake/snake_curves.png')
        self.curves = self.curves_img
        self.tail_img = pygame.image.load('../Graphics/Snake/snake_tail.png')
        self.tail = self.tail_img

    def update_position(self, inc_x, inc_y, direction):

        self.head_x += inc_x
        self.head_y += inc_y
        self.head_direction = direction
        snake_current_head = (self.head_x, self.head_y, self.head_direction)
        self.snake_body.append(snake_current_head)
        if len(self.snake_body) > self.snake_length:
            del self.snake_body[0]

    def get_head_direction(self):

        if self.head_direction == "UP":
            self.head = self.head_img
        elif self.head_direction == "DOWN":
            self.head = pygame.transform.rotate(self.head_img, 180)
        elif self.head_direction == "RIGHT":
            self.head = pygame.transform.rotate(self.head_img, 270)
        elif self.head_direction == "LEFT":
            self.head = pygame.transform.rotate(self.head_img, 90)

    def get_body_direction(self, segment_idx):

        if self.snake_body[segment_idx + 1][2] == "UP":
            if segment_idx > - len(self.snake_body):
                if self.snake_body[segment_idx][2] == "UP" or self.snake_body[segment_idx][2] == "DOWN":
                    self.body = self.body_img
                elif self.snake_body[segment_idx][2] == "LEFT":
                    self.body = pygame.transform.rotate(self.curves_img, 90)
                elif self.snake_body[segment_idx][2] == "RIGHT":
                    self.body = pygame.transform.rotate(self.curves_img, 180)
            else:
                self.body = self.body_img
        elif self.snake_body[segment_idx + 1][2] == "DOWN":
            if segment_idx > - len(self.snake_body):
                if self.snake_body[segment_idx][2] == "UP" or self.snake_body[segment_idx][2] == "DOWN":
                    self.body = self.body_img
                elif self.snake_body[segment_idx][2] == "LEFT":
                    self.body = self.curves_img
                elif self.snake_body[segment_idx][2] == "RIGHT":
                    self.body = pygame.transform.rotate(self.curves_img, 270)
            else:
                self.body = self.body_img
        elif self.snake_body[segment_idx + 1][2] == "LEFT":
            if segment_idx > - len(self.snake_body):
                if self.snake_body[segment_idx][2] == "LEFT" or self.snake_body[segment_idx][2] == "RIGHT":
                    self.body = pygame.transform.rotate(self.body_img, 90)
                elif self.snake_body[segment_idx][2] == "UP":
                    self.body = pygame.transform.rotate(self.curves_img, 270)
                elif self.snake_body[segment_idx][2] == "DOWN":
                    self.body = pygame.transform.rotate(self.curves_img, 180)
            else:
                self.body = pygame.transform.rotate(self.body_img, 90)
        elif self.snake_body[segment_idx + 1][2] == "RIGHT":
            if segment_idx > - len(self.snake_body):
                if self.snake_body[segment_idx][2] == "LEFT" or self.snake_body[segment_idx][2] == "RIGHT":
                    self.body = pygame.transform.rotate(self.body_img, 90)
                elif self.snake_body[segment_idx][2] == "UP":
                    self.body = self.curves_img
                elif self.snake_body[segment_idx][2] == "DOWN":
                    self.body = pygame.transform.rotate(self.curves_img, 90)
            else:
                self.body = pygame.transform.rotate(self.body_img, 90)

    def get_tail_direction(self, segment_idx):

        if self.snake_body[segment_idx + 1][2] == "UP":
            self.tail = self.tail_img
        elif self.snake_body[segment_idx + 1][2] == "DOWN":
            self.tail = pygame.transform.rotate(self.tail_img, 180)
        elif self.snake_body[segment_idx + 1][2] == "LEFT":
            self.tail = pygame.transform.rotate(self.tail_img, 90)
        elif self.snake_body[segment_idx + 1][2] == "RIGHT":
            self.tail = pygame.transform.rotate(self.tail_img, 270)

    def draw_snake(self):

        self.get_head_direction()
        screen.screen.blit(self.head, (self.snake_body[-1][0], self.snake_body[-1][1]))

        for segment_idx in range(-2, -len(self.snake_body) - 1, -1):
            if segment_idx > -len(self.snake_body):
                self.get_body_direction(segment_idx)
                segment = self.snake_body[segment_idx]
                screen.screen.blit(self.body, (segment[0], segment[1]))
            else:
                self.get_tail_direction(segment_idx)
                segment = self.snake_body[segment_idx]
                screen.screen.blit(self.tail, (segment[0], segment[1]))
            segment_idx -= 1

    def eating_food(self, food_x, food_y, bonus_food_x, bonus_food_y):

        if (
                self.head_x == food_x and self.head_y == food_y) or \
                self.head_x == bonus_food_x and self.head_y == bonus_food_y:
            self.snake_length += 1

    def check_collision(self):

        cord_list = [(i[0], i[1]) for i in self.snake_body[:-1]]

        if (self.head_x, self.head_y) in cord_list:
            return True
        else:
            return False


class Food:

    def __init__(self):

        self.food_x = None
        self.food_y = None
        self.bonus_food_x = None
        self.bonus_food_y = None
        self.food_size = 40
        self.current_food = None
        self.current_food = imp

    def generate(self, snake):

        cord_list = [(i[0], i[1]) for i in snake.snake_body]
        while True:
            x = round(random.randrange(0, screen.scr_width - self.food_size) / self.food_size) * self.food_size
            y = round(random.randrange(0, screen.scr_height - self.food_size) / self.food_size) * self.food_size
            if (x, y) not in cord_list:
                break
        self.food_x = x
        self.food_y = y

    def generate_bonus_food(self, snake):

        cord_list = [(i[0], i[1]) for i in snake.snake_body]
        while True:
            x = round(random.randrange(0, screen.scr_width - self.food_size) / self.food_size) * self.food_size
            y = round(random.randrange(0, screen.scr_height - self.food_size) / self.food_size) * self.food_size
            if (x, y) not in cord_list:
                break
        self.bonus_food_x = x
        self.bonus_food_y = y

    def draw_food(self):

        if self.current_food is None:
            self.current_food = imp
        screen.screen.blit(self.current_food, (self.food_x, self.food_y))

    def draw_bonus_food(self):

        screen.screen.blit(syn, (self.bonus_food_x, self.bonus_food_y))

    def snake_eating(self, snake_x, snake_y):

        if self.food_x == snake_x and self.food_y == snake_y:
            self.current_food = random.choice(foods)
            return True

    def snake_eating_bonus(self, snake_x, snake_y):

        if self.bonus_food_x == snake_x and self.bonus_food_y == snake_y:
            return True


class Score:

    def __init__(self):
        self.result = 0

    def get_score_str(self):
        str_res = str(self.result)

        return "Score: " + str_res

    def get_score(self):
        return self.result

    def update_score(self):
        self.result += 10

    def update_score_special(self):
        self.result += 20

    def show_score(self):
        text_1 = text.Text(self.get_score_str(), screen.red, (screen.scr_width / 2, 40), 90)

        text_1.print_text()


class Game:

    def __init__(self):

        self.state = 0
        self.back = pygame.image.load('../Graphics/Snake/back.png')
        self.menu_back = pygame.image.load('../Graphics/Snake/menu.png')
        self.score = " "

    def game_loop(self):

        while True:
            if self.state == 0:
                self.menu_game()
            elif self.state == 1:
                self.start_game()
            elif self.state == 2:
                self.game_over()
            elif self.state == 3:
                self.state = 0
                return None
            elif self.state == 4:
                self.help_game()

    def menu_game(self):

        text_1 = text.Text("Error Eater", screen.red, (screen.scr_width / 2, screen.scr_height / 2 - 100), 90)
        text_2 = text.Text("Play Game!", screen.red, (screen.scr_width / 2, screen.scr_height / 2 + 50), 40)
        text_3 = text.Text("Quit Game", screen.red, (screen.scr_width / 2, screen.scr_height / 2 + 150), 40)
        text_4 = text.Text("Help", screen.red, (screen.scr_width / 2, screen.scr_height / 2 + 100), 40)

        select = "Play Game!"

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = 3
                    return None
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.state = 1
                        return None
                    elif event.key == pygame.K_DOWN:
                        if select == "Play Game!":
                            select = "Help"
                        else:
                            select = "Quit Game"
                    elif event.key == pygame.K_UP:
                        if select == "Help":
                            select = "Play Game!"
                        elif select == "Quit Game":
                            select = "Help"
                    if event.key == pygame.K_RETURN:
                        if select == "Play Game!":
                            self.state = 1
                            return None
                        if select == "Help":
                            self.state = 4
                            return None
                        if select == "Quit Game":
                            self.state = 3
                            return None

            screen.screen.blit(self.menu_back, (0, 0))
            text_1.print_text()
            if select == "Play Game!":
                text_2.change_colour(screen.gold)
            else:
                text_2.change_colour(screen.red)
            text_2.print_text()
            if select == "Help":
                text_4.change_colour(screen.gold)
            else:
                text_4.change_colour(screen.red)
            text_4.print_text()
            if select == "Quit Game":
                text_3.change_colour(screen.gold)
            else:
                text_3.change_colour(screen.red)
            text_3.print_text()
            pygame.display.update()

    def help_game(self):

        text_1 = text.Text("How to play???", screen.red, (screen.scr_width / 2, 40), 90)
        text_2 = text.Text("Eat errors.", screen.red, (screen.scr_width / 2, 140), 40)
        text_3 = text.Text("Use arrow keys.", screen.red, (screen.scr_width / 2, 240), 40)
        text_4 = text.Text("Press ESC to go back.", screen.red, (screen.scr_width / 2, 640), 40)

        while True:
            screen.screen.fill(screen.white)
            text_1.print_text()
            text_2.print_text()
            text_3.print_text()
            text_4.print_text()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = 3
                    return None
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.state = 0
                        return None

    def start_game(self):

        inc_x = 0
        inc_y = 0
        food = Food()
        snake = Snake()
        food.generate(snake)
        food.generate_bonus_food(snake)
        score = Score()
        direction = None
        timer = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = 3
                    return None
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        inc_y = snake_size
                        inc_x = 0
                        direction = "DOWN"
                    elif event.key == pygame.K_UP:
                        inc_y = -snake_size
                        inc_x = 0
                        direction = "UP"
                    elif event.key == pygame.K_LEFT:
                        inc_x = -snake_size
                        inc_y = 0
                        direction = "LEFT"
                    elif event.key == pygame.K_RIGHT:
                        inc_x = snake_size
                        inc_y = 0
                        direction = "RIGHT"
                    elif event.key == pygame.K_p:
                        self.game_pause()

            if snake.head_x >= screen.scr_width or snake.head_x < 0 or\
                    snake.head_y >= screen.scr_height or snake.head_y < 0:
                self.state = 2
                return None

            if snake.check_collision():
                self.state = 2
                return None
            timer += 1

            snake.update_position(inc_x, inc_y, direction)
            screen.screen.blit(self.back, (0, 0))
            snake.eating_food(food.food_x, food.food_y, food.bonus_food_x, food.bonus_food_y)
            if food.snake_eating(snake.head_x, snake.head_y):
                food.generate(snake)
                score.update_score()
            if timer > 20:
                if food.snake_eating_bonus(snake.head_x, snake.head_y):
                    score.update_score_special()
                    food.generate_bonus_food(snake)
                    timer = 0
                if timer > 20:
                    food.draw_bonus_food()
                if timer > 40:
                    food.generate_bonus_food(snake)
                    timer = 0

            snake.draw_snake()
            food.draw_food()
            score.show_score()
            self.score = str(score.get_score())

            pygame.display.update()
            if snake.check_collision():
                self.state = 2
                return None

            clock.tick(fps)

    def game_over(self):

        text_1 = text.Text("Game Over", screen.red, (screen.scr_width / 2, screen.scr_height / 2 - 50), 90)
        text_2 = text.Text("Press SPACE for Play Again or ESC for Quit Game", screen.red,
                           (screen.scr_width / 2, screen.scr_height / 2 + 50), 25)
        text_3 = text.Text("Your score: ", screen.red, (screen.scr_width / 2 - 50, screen.scr_height / 2 + 100), 25)
        text_4 = text.Text(self.score, screen.red, (screen.scr_width / 2 + 50, screen.scr_height / 2 + 100), 25)

        while True:
            screen.screen.fill(screen.white)
            text_1.print_text()
            text_2.print_text()
            text_3.print_text()
            text_4.print_text()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.state = 1
                        return None
                    if event.key == pygame.K_ESCAPE:
                        self.state = 3
                        return None
                if event.type == pygame.QUIT:
                    self.state = 3
                    return None

    @staticmethod
    def game_pause():

        text_1 = text.Text("Game Paused", screen.red, (screen.scr_width / 2, screen.scr_height / 2 - 50), 40)
        text_2 = text.Text("Press SPACE for return to the game!", screen.red,
                           (screen.scr_width / 2, screen.scr_height / 2 + 50), 25)

        while True:
            screen.screen.fill(screen.white)
            text_1.print_text()
            text_2.print_text()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return None
