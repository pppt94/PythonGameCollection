import pygame
import random

pygame.init()
clock = pygame.time.Clock()

#define screen
scr_width = 800
scr_height = 600
screen = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption('I am snake. Python Snake.')
fps = 5

#define colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#define snake
snake_size = 20

class Snake():

    def __init__(self, snake_size):

        self.head_x = scr_width / 2
        self.head_y = scr_height / 2
        self.snake_size = snake_size
        self.snake_body = []
        self.snake_length = 1

    def update_position(self, inc_x, inc_y):

        self.head_x += inc_x
        self.head_y += inc_y

        snake_current_head = (self.head_x, self.head_y)
        self.snake_body.append(snake_current_head)
        if len(self.snake_body) > self.snake_length:
            del self.snake_body[0]

    def draw_snake(self):

        for segment in self.snake_body:
            pygame.draw.rect(screen, red, [segment[0], segment[1], self.snake_size, self.snake_size])

    def eating_food(self, food_x, food_y, food_size):

        if self.head_x == food_x and self.head_y == food_y:
            self.snake_length += 1


class Food():

    def __init__(self):

        self.food_x = None
        self.food_y = None
        self.food_size = 20
        self.generate()


    def generate(self):

        self.food_x = round(random.randrange(0, scr_width-self.food_size) / self.food_size)*self.food_size
        self.food_y = round(random.randrange(0, scr_height-self.food_size) / self.food_size)*self.food_size


    def draw_food(self):

        pygame.draw.rect(screen, green, [self.food_x, self.food_y, self.food_size, self.food_size])

    def snake_eating(self, snake_x, snake_y, snake_size):

        if self.food_x == snake_x and self.food_y == snake_y:
            self.generate()

class Game():

    def __init__(self):

        self.state = 1
        self.game_loop()

    def game_loop(self):

        while True:
            if self.state == 1:
                self.start_game()
            elif self.state == 2:
                self.game_over()
            elif self.state == 3:
                self.game_exit()

    def start_game(self):

        inc_x = 0
        inc_y = 0
        food = Food()
        snake = Snake(snake_size)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = 3
                    return None
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        inc_y = snake_size
                        inc_x = 0
                    elif event.key == pygame.K_UP:
                        inc_y = -snake_size
                        inc_x = 0
                    elif event.key == pygame.K_LEFT:
                        inc_x = -snake_size
                        inc_y = 0
                    elif event.key == pygame.K_RIGHT:
                        inc_x = snake_size
                        inc_y = 0



            if snake.head_x >= scr_width or snake.head_x <= 0 or snake.head_y >= scr_height or snake.head_y <= 0:
                self.state = 2
                return None

            snake.update_position(inc_x, inc_y)
            screen.fill(black)
            snake.eating_food(food.food_x, food.food_y, food.food_size)
            food.snake_eating(snake.head_x, snake.head_y, snake.snake_size)
            snake.draw_snake()
            food.draw_food()
            pygame.display.update()

            clock.tick(fps)

    def game_over(self):

        while True:
            screen.fill(white)
            font = pygame.font.SysFont(None, 25)
            screen_text = font.render("Press ESC or SPACE", True, red)
            screen.blit(screen_text, [scr_width/2, scr_height/2])
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

    def game_exit(self):
        pygame.quit()
        quit()

Game()
