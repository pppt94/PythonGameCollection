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
orange = (255, 120, 0)
gray = (128, 128, 128)

class Types():

    def __init__(self):

        self.type_array = [black, orange, red, green, blue, gold]
        self.game_array = []
        self.player_array = []
        self.fill_arrays()

    def fill_arrays(self):

        self.game_array = random.choices(self.type_array, k=4)
        self.player_array = [gray, gray, gray, gray]

    def print_array(self, step):

        p = 400

        for x in self.game_array:
            pygame.draw.circle(screen, x, (p, 600), 10)
            p+=50

        p = 400

        for x in self.player_array:
            pygame.draw.circle(screen, x, (p, 300), 10)
            p += 50

    def change_coloru(self, position):

        if position[0] >= 390 and position[0] <= 410:
            if position[1] >= 290 and position[1] <= 310:
                pygame.draw.circle(screen, red, (400, 300), 10)


class Game():

    def __init__(self):


        self.t = Types()
        self.game_loop()

    def game_loop(self):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = 3
                    return None

            screen.fill(white)
            self.t.print_array(3)
            self.t.change_coloru(pygame.mouse.get_pos())
            pygame.display.update()
            print(pygame.mouse.get_pos())

Game()