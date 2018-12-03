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

        self.type_array = [pygame.image.load('Graphics/list.png'), pygame.image.load('Graphics/int.png'),
                           pygame.image.load('Graphics/float.png'), pygame.image.load('Graphics/complex.png'),
                           pygame.image.load('Graphics/tuple.png'), pygame.image.load('Graphics/string.png')]
        self.game_array = []
        self.player_array = [None, None, None, None]
        self.result_array = []
        self.type_idx = 0
        self.fill_arrays()

    def fill_arrays(self):

        self.game_array = random.choices(self.type_array, k=4)
        #self.player_array = [gray, gray, gray, gray]

    def print_game_array(self):

        p = 100

        for x in self.game_array:
            screen.blit(x, (p, 100))
            p += 60

    def check_change_coloru(self, position, level):

        column = 0
        dimensiony = 643 - (78 * level)
        for i in range(386, 626, 60):
            self.change_colour(position, i, dimensiony, column)
            column += 1

    def change_colour(self, position, dimensionx, dimensiony, column):
        print(pygame.mouse.get_pos(), dimensiony)

        if position[0] >= dimensionx and position[0] <= dimensionx + 55:
            if position[1] >= dimensiony and position[1] <= dimensiony + 55 :

                screen.blit(self.type_array[self.type_idx], (dimensionx, dimensiony))

                self.player_array[column] = self.type_array[self.type_idx]

                self.type_idx = self.type_idx + 1 if self.type_idx <= 4 else 0

        return None


    def check_end_round(self, position):
        if position[0] >= 50 and position[0] <= 70:
            if position[1] >= 50 and position[1] <= 70:
                return True

    def compare_array(self):

        for i in range(0, 4):
            if self.game_array[i] == self.player_array[i]:
                self.result_array.append(1)



class Game():

    def __init__(self):

        self.menu = pygame.image.load('Graphics/mind02.png')
        self.list = pygame.image.load('Graphics/list.png')
        self.level = 0
        self.step = 0
        self.t = Types()
        self.game_loop()

    def game_loop(self):


        self.t.print_game_array()
        screen.blit(self.menu, (0, 0))
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
                self.t.print_game_array()
                self.step += 1


            pygame.display.update()

#Game()