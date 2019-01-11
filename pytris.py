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

    def draw_grid(self):

        self.grid = [[(0, 0, 0) for row in range(10)] for column in range(20)]