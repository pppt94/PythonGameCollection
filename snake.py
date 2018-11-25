import pygame
import random

pygame.init()
clock = pygame.time.Clock()

#define screen
scr_width = 880
scr_height = 720
screen = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption('Error Eater')
fps = 5

#define colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gold = (255, 215, 0)

#define snake
snake_size = 40

class Snake():

    def __init__(self, snake_size):

        self.head_x = scr_width / 2
        self.head_y = scr_height / 2
        self.snake_size = snake_size
        self.snake_body = []
        self.snake_length = 1
        self.head_direction = "UP"
        self.head_img = pygame.image.load('Graphics/snake_head.png')
        self.head = self.head_img
        self.body_img = pygame.image.load('Graphics/snake_body.png')
        self.body = self.body_img
        self.curves_img = pygame.image.load('Graphics/snake_curves.png')
        self.curves = self.curves_img
        self.tail_img = pygame.image.load('Graphics/snake_tail.png')
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
                if self.snake_body[segment_idx ][2] == "UP" or self.snake_body[segment_idx][2] == "DOWN":
                    self.body = self.body_img
                elif self.snake_body[segment_idx][2] == "LEFT":
                    self.body = pygame.transform.rotate(self.curves_img, 90)
                elif self.snake_body[segment_idx][2] == "RIGHT":
                    self.body = pygame.transform.rotate(self.curves_img, 180)
            else:
                self.body = self.body_img
        elif self.snake_body[segment_idx + 1][2] == "DOWN":
            if segment_idx > - len(self.snake_body):
                if self.snake_body[segment_idx ][2] == "UP" or self.snake_body[segment_idx][2] == "DOWN":
                    self.body = self.body_img
                elif self.snake_body[segment_idx][2] == "LEFT":
                    self.body = self.curves_img
                elif self.snake_body[segment_idx][2] == "RIGHT":
                    self.body = pygame.transform.rotate(self.curves_img, 270)
            else:
                self.body = self.body_img
        elif self.snake_body[segment_idx + 1][2] == "LEFT":
            if segment_idx > - len(self.snake_body):
                if self.snake_body[segment_idx ][2] == "LEFT" or self.snake_body[segment_idx][2] == "RIGHT":
                    self.body = pygame.transform.rotate(self.body_img, 90)
                elif self.snake_body[segment_idx][2] == "UP":
                    self.body = pygame.transform.rotate(self.curves_img, 270)
                elif self.snake_body[segment_idx][2] == "DOWN":
                    self.body = pygame.transform.rotate(self.curves_img, 180)
            else:
                self.body = pygame.transform.rotate(self.body_img, 90)
        elif self.snake_body[segment_idx + 1][2] == "RIGHT":
            if segment_idx > - len(self.snake_body):
                if self.snake_body[segment_idx ][2] == "LEFT" or self.snake_body[segment_idx][2] == "RIGHT":
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
        screen.blit(self.head, (self.snake_body[-1][0], self.snake_body[-1][1]))

        for segment_idx in range(-2, -len(self.snake_body) - 1, -1):
            if segment_idx > -len(self.snake_body):
                self.get_body_direction(segment_idx)
                segment = self.snake_body[segment_idx]
                screen.blit(self.body, (segment[0], segment[1]))
            else:
                self.get_tail_direction(segment_idx)
                segment = self.snake_body[segment_idx]
                screen.blit(self.tail, (segment[0], segment[1]))
            segment_idx -= 1

    def eating_food(self, food_x, food_y, bonus_food_x, bonus_food_y):

        if (self.head_x == food_x and self.head_y == food_y) or self.head_x == bonus_food_x and self.head_y == bonus_food_y:
            self.snake_length += 1


    def check_colision(self):

        cord_list = [(i[0], i[1]) for i in self.snake_body[:-1]]

        if (self.head_x, self.head_y) in cord_list:
            return True
        else:
            return False

class Food():

    def __init__(self):

        self.food_x = None
        self.food_y = None
        self.bonus_food_x = None
        self.bonus_food_y = None
        self.food_size = 40
        self.generate()
        self.generate_bonus_food()
        self.syn = pygame.image.load('Graphics/food_syntax.png')
        self.imp = pygame.image.load('Graphics/food_import.png')
        self.ind = pygame.image.load('Graphics/food_index.png')
        self.nam = pygame.image.load('Graphics/food_name.png')
        self.typ = pygame.image.load('Graphics/food_type.png')
        self.current_food = self.imp


    def generate(self):

        self.food_x = round(random.randrange(0, scr_width-self.food_size) / self.food_size)*self.food_size
        self.food_y = round(random.randrange(0, scr_height-self.food_size) / self.food_size)*self.food_size

    def generate_bonus_food(self):

        self.bonus_food_x = round(random.randrange(0, scr_width-self.food_size) / self.food_size)*self.food_size
        self.bonus_food_y = round(random.randrange(0, scr_height-self.food_size) / self.food_size)*self.food_size


    def draw_food(self):

        screen.blit(self.current_food, (self.food_x, self.food_y))

    def draw_bonus_food(self):

        screen.blit(self.syn, (self.bonus_food_x, self.bonus_food_y))

    def snake_eating(self, snake_x, snake_y, snake_size):

        if self.food_x == snake_x and self.food_y == snake_y:
            self.current_food = random.choice([self.imp, self.ind, self.nam, self.typ])
            self.generate()
            return True


    def snake_eating_bonus(self, snake_x, snake_y, snake_size):

        if self.bonus_food_x == snake_x and self.bonus_food_y == snake_y:
            return True

class Score():

    def __init__(self):

        self.result = 0

    def get_score_str(self):

        str_res = str(self.result)

        return "Score: "+str_res

    def get_score(self):

        return self.result

    def update_score(self):

        self.result += 10

    def update_score_special(self):

        self.result += 20

    def show_score(self):

        text_1 = Text(self.get_score_str(), red, (scr_width / 2, 40), 90)

        text_1.print_text()



class Text():

    def __init__(self, text, colour, position, size):

        self.text = text
        self.colour = colour
        self.position = position
        self.size = size
        self.text_font = None
        self.text_rect = None

    def text_obj(self):

        font = pygame.font.SysFont(None, self.size)

        self.text_font = font.render(self.text, True, self.colour)
        self.text_rect = self.text_font.get_rect()

    def print_text(self):

        self.text_obj()
        self.text_rect.center = (self.position[0]), (self.position[1])
        screen.blit(self.text_font, self.text_rect)

    def change_colour(self, colour):

        self.colour = colour

class Game():

    def __init__(self):

        self.state = 0
        self.back = pygame.image.load('Graphics/back.png')
        self.game_loop()
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
                self.game_exit()
            elif self.state == 4:
                self.help_game()

    def menu_game(self):

        text_1 = Text("Welcome", red, (scr_width / 2, scr_height / 2-100), 90)
        text_2 = Text("Play Game!", red, (scr_width / 2, scr_height / 2 + 50), 40)
        text_3 = Text("Quit Game", red, (scr_width / 2, scr_height / 2 + 150), 40)
        text_4 = Text("Help", red, (scr_width / 2, scr_height / 2 + 100), 40)

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

            screen.fill(white)
            text_1.print_text()
            if select == "Play Game!":
                text_2.change_colour(gold)
            else:
                text_2.change_colour(red)
            text_2.print_text()
            if select == "Help":
                text_4.change_colour(gold)
            else:
                text_4.change_colour(red)
            text_4.print_text()
            if select == "Quit Game":
                text_3.change_colour(gold)
            else:
                text_3.change_colour(red)
            text_3.print_text()
            pygame.display.update()

    def help_game(self):

        text_1 = Text("How to play???", red, (scr_width / 2, 40), 90)
        text_2 = Text("Eat errors.", red, (scr_width / 2, 140), 40)
        text_3 = Text("Use arrow keys.", red, (scr_width / 2, 240), 40)
        text_4 = Text("Press ESC to go back.", red, (scr_width / 2, 640), 40)

        while True:
            screen.fill(white)
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
        snake = Snake(snake_size)
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



            if snake.head_x >= scr_width or snake.head_x < 0 or snake.head_y >= scr_height or snake.head_y < 0:
                self.state = 2
                return None

            if snake.check_colision():
                self.state = 2
                return None
            timer +=1

            snake.update_position(inc_x, inc_y, direction)
            screen.blit(self.back, (0, 0))
            snake.eating_food(food.food_x, food.food_y, food.bonus_food_x, food.bonus_food_y)
            if food.snake_eating(snake.head_x, snake.head_y, snake.snake_size):
                score.update_score()
            if timer > 20:
                if food.snake_eating_bonus(snake.head_x, snake.head_y, snake.snake_size):
                    score.update_score_special()
                    food.generate_bonus_food()
                    timer = 0
                if timer > 20:
                    food.draw_bonus_food()
                if timer > 40:
                    food.generate_bonus_food()
                    timer = 0

            snake.draw_snake()
            food.draw_food()
            score.show_score()
            self.score = str(score.get_score())


            pygame.display.update()
            if snake.check_colision():
                self.state = 2
                return None

            clock.tick(fps)

    def game_over(self):

        text_1 = Text("Game Over", red, (scr_width / 2, scr_height / 2 - 50), 90)
        text_2 = Text("Press SPACE for Play Again or ESC for Quit Game", red, (scr_width / 2, scr_height / 2 + 50), 25)
        text_3 = Text("Your score: ", red, (scr_width / 2 - 50, scr_height / 2 + 100), 25)
        text_4 = Text(self.score, red, (scr_width / 2 + 50, scr_height / 2 + 100), 25)

        while True:
            screen.fill(white)
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

    def game_pause(self):

        text_1 = Text("Game Paused", red, (scr_width / 2, scr_height / 2 - 50), 40)
        text_2 = Text("Press SPACE for return to the game!", red, (scr_width / 2, scr_height / 2 + 50), 25)

        while True:
            screen.fill(white)
            text_1.print_text()
            text_2.print_text()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return None

    def game_exit(self):
        pygame.quit()
        quit()

Game()
