import pygame
import random
from Source import screen

pygame.init()
clock = pygame.time.Clock()


class Types:

    def __init__(self):

        self.type_array = [pygame.image.load('../Graphics/PythonMind/list.png'),
                           pygame.image.load('../Graphics/PythonMind/int.png'),
                           pygame.image.load('../Graphics/PythonMind/float.png'),
                           pygame.image.load('../Graphics/PythonMind/complex.png'),
                           pygame.image.load('../Graphics/PythonMind/tuple.png'),
                           pygame.image.load('../Graphics/PythonMind/string.png')]
        self.result_img = pygame.image.load('../Graphics/PythonMind/result.png')
        self.white_img = pygame.image.load('../Graphics/PythonMind/white.png')
        self.black_img = pygame.image.load('../Graphics/PythonMind/black.png')
        self.gray_img = pygame.image.load('../Graphics/PythonMind/gray.png')
        self.game_array = []
        self.player_array = [0, 0, 0, 0]
        self.result_array = []
        self.type_idx = 0
        self.fill_arrays()

    def fill_arrays(self):

        self.game_array = random.sample(self.type_array, 4)

    def print_game_array(self):

        p = 290

        for x in self.game_array:
            screen.screen.blit(x, (p, 290))
            p += 60

    def check_change_colour(self, position, level):

        column = 0
        dimension_y = 643 - (78 * level)
        for i in range(386, 626, 60):
            self.change_colour(position, i, dimension_y, column)
            column += 1

    def change_colour(self, position, dimension_x, dimension_y, column):

        if dimension_x <= position[0] <= dimension_x + 55:
            if dimension_y <= position[1] <= dimension_y + 55:

                screen.screen.blit(self.type_array[self.type_idx], (dimension_x, dimension_y))
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

        screen.screen.blit(self.result_img, (655, 635 - (78 * level)))
        if level >= 1:
            screen.screen.blit(self.result_array[0], (666, 646 - (78 * (level-1))))
            screen.screen.blit(self.result_array[1], (692, 646 - (78 * (level-1))))
            screen.screen.blit(self.result_array[2], (666, 676 - (78 * (level-1))))
            screen.screen.blit(self.result_array[3], (692, 676 - (78 * (level-1))))
            pygame.display.update()


class Game:

    def __init__(self):

        self.menu = pygame.image.load('../Graphics/PythonMind/mind02.png')
        self.over = pygame.image.load('../Graphics/PythonMind/mind_over.png')
        self.success = pygame.image.load('../Graphics/PythonMind/mind_success.png')
        self.help = pygame.image.load('../Graphics/PythonMind/mind_help.png')
        self.level = 0
        self.state = 0
        self.t = Types()

    def game_loop(self):

        while True:
            if self.state == 0:
                self.start_game()
            elif 1 <= self.state <= 3:
                self.game_mode()
            elif self.state == 4:
                self.state = 0
                return None

    def start_game(self):

        self.level = 0
        self.state = 0
        self.t = Types()
        screen.screen.blit(self.menu, (0, 0))
        self.t.print_result(self.level)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = 4
                    return None
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.t.check_change_colour(pygame.mouse.get_pos(), self.level)
                    position = pygame.mouse.get_pos()
                    if 170 <= position[0] <= 315:
                        if 380 <= position[1] <= 490:
                            self.level += 1
                            self.t.compare_array()
                            self.t.print_result(self.level)
                    if 130 <= position[0] <= 275:
                        if 25 <= position[1] <= 170:
                            self.state = 0
                            return None
                    if 30 <= position[0] <= 215:
                        if 515 <= position[1] <= 680:
                            self.state = 4
                            return None
                    if 20 <= position[0] <= 142:
                        if 340 <= position[1] <= 460:
                            self.state = 3
                            return None

            if self.level >= 9:
                self.state = 1
                return None
            if self.t.result_array == [self.t.black_img] * 4:
                self.state = 2
                return None
            pygame.display.update()

    def game_mode(self):

        if self.state == 1:
            screen.screen.blit(self.over, (0, 0))
            self.t.print_game_array()
        elif self.state == 2:
            screen.screen.blit(self.success, (0, 0))
            self.t.print_game_array()
        else:
            screen.screen.blit(self.help, (0, 0))

        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.state = 0
                        return None
                    if event.key == pygame.K_ESCAPE:
                        self.state = 4
                        return None
                if event.type == pygame.QUIT:
                    self.state = 4
                    return None
