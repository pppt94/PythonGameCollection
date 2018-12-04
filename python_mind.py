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
        self.result_img = pygame.image.load('Graphics/result.png')
        self.white_img = pygame.image.load('Graphics/white.png')
        self.black_img = pygame.image.load('Graphics/black.png')
        self.gray_img = pygame.image.load('Graphics/gray.png')
        self.game_array = []
        self.player_array = [0, 0, 0, 0]
        self.result_array = []
        self.type_idx = 0
        self.fill_arrays()

    def fill_arrays(self):

        self.game_array = random.choices(self.type_array, k=4)


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

        if position[0] >= dimensionx and position[0] <= dimensionx + 55:
            if position[1] >= dimensiony and position[1] <= dimensiony + 55 :

                screen.blit(self.type_array[self.type_idx], (dimensionx, dimensiony))

                self.player_array[column] = self.type_array[self.type_idx]

                self.type_idx = self.type_idx + 1 if self.type_idx <= 4 else 0

        return None

    def compare_array(self):

        self.result_array.clear()
        temp_array = self.game_array.copy()
        for i in range(0, 4):
            if self.player_array[i] == temp_array[i]:
                self.result_array.append(self.black_img)
                temp_array[i] = None

        for i in range(0, 4):
            if self.player_array[i] in temp_array:
                self.result_array.append(self.white_img)
                idx = temp_array.index(self.player_array[i])
                temp_array[idx] = None

        while len(self.result_array) < 4:
            self.result_array.append(self.gray_img)

        self.player_array = [0, 0, 0, 0]


    def print_result(self, level):

        screen.blit(self.result_img, (655, 635 - (78 * level)))
        if level >= 1:
            screen.blit(self.result_array[0], (666, 646 - (78 * (level-1))))
            screen.blit(self.result_array[1], (692, 646 - (78 * (level-1))))
            screen.blit(self.result_array[2], (666, 676 - (78 * (level-1))))
            screen.blit(self.result_array[3], (692, 676 - (78 * (level-1))))
            pygame.display.update()


class Game():

    def __init__(self):

        self.menu = pygame.image.load('Graphics/mind02.png')
        self.level = 0
        self.state = 0
        self.t = Types()
        #self.game_loop()

    def game_loop(self):

        while True:
            if self.state == 0:
                self.start_game()
            elif self.state == 1:
                self.game_over()
            elif self.state == 2:
                self.game_succes()
            elif self.state == 3:
                self.help_game()
            elif self.state == 4:
                self.state = 0
                return None

    def start_game(self):

        self.level = 0
        self.state = 0
        self.t = Types()
        screen.blit(self.menu, (0, 0))
        # SHOW
        #self.t.print_game_array()
        self.t.print_result(self.level)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = 3
                    return None
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.t.check_change_coloru(pygame.mouse.get_pos(), self.level)
                    position = pygame.mouse.get_pos()
                    if position[0] >= 170 and position[0] <= 315:
                        if position[1] >= 380 and position[1] <= 490:
                            self.level += 1
                            self.t.compare_array()
                            self.t.print_result(self.level)
                    if position[0] >= 130 and position[0] <= 275:
                        if position[1] >= 25 and position[1] <= 170:
                            self.state = 0
                            return None
                    if position[0] >= 30 and position[0] <= 215:
                        if position[1] >= 515 and position[1] <= 680:
                            self.state = 4
                            return None

            pygame.display.update()




#Game()