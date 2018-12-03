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
        self.type_idx = 0
        self.fill_arrays()

    def fill_arrays(self):

        self.game_array = random.choices(self.type_array, k=4)
        self.player_array = [gray, gray, gray, gray]

    def print_array(self, level):

        p = 400

        for x in self.game_array:
            pygame.draw.circle(screen, x, (p, 600), 10)
            p+=50

        p = 400

        for x in self.player_array:
            pygame.draw.circle(screen, x, (p, 300 + (20 * level)), 10)
            p += 50

    def check_change_coloru(self, position, level):

        column = 0
        dimensiony = 300 + (20 * level)
        for i in range(400, 650, 50):
            self.change_colour(position, i, dimensiony, column)
            column += 1

    def change_colour(self, position, dimensionx, dimensiony, column):

        if position[0] >= dimensionx - 10 and position[0] <= dimensionx + 10:
            if position[1] >= dimensiony - 10 and position[1] <= dimensiony + 10:

                pygame.draw.circle(screen, self.type_array[self.type_idx], (dimensionx, dimensiony), 10)
                self.player_array[column] = self.type_array[self.type_idx]
                self.type_idx = self.type_idx + 1 if self.type_idx <= 4 else 0


    def check_end_round(self, position):
        if position[0] >= 50 and position[0] <= 70:
            if position[1] >= 50 and position[1] <= 70:
                return True

class Game():

    def __init__(self):

        self.level = 0
        self.step = 0
        self.t = Types()
        self.game_loop()

    def game_loop(self):

        screen.fill(white)

        pygame.draw.rect(screen, red, (50, 50, 20, 20))
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = 3
                    return None
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.t.check_change_coloru(pygame.mouse.get_pos(), self.level)
                    if self.t.check_end_round(pygame.mouse.get_pos()):
                        self.level += 1

            if self.step == self.level:
                self.t.print_array(self.level)
                self.step += 1

            pygame.display.update()
            print(pygame.mouse.get_pressed())

Game()