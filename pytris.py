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

class Blocks():

    def __init__(self, x, y, shape):

        self.x = x
        self.y = y
        self.shape = shape
        self.color = []
        self.rotation = 0

class Board():

    def __init__(self):

        self.grid = []
        self.blocks_positions = {}

    def create_grid(self):

        self.grid = [[(0, 0, 0) for row in range(10)] for column in range(20)]

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if (j, i) in self.blocks_positions:
                    cube = self.blocks_positions[(j, i)]
                    self.grid[i][j] = cube

        return self.grid

class Game():

    def __init__(self):
        self.state = 0

    def game_loop(self):

        while True:
            if self.state == 0:
                self.start_game()
            elif self.state == 1:
                self.game_over()
            elif self.state == 2:
                self.help_game()
            elif self.state == 3:
                self.state = 0
                return None

    def start_game(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = 3
                    return None
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        pass
                    elif event.key == pygame.K_LEFT:
                        pass
                    elif event.key == pygame.K_DOWN:
                        pass
                    elif event.key == pygame.K_SPACE:
                        pass