import pygame

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


class Game():

    def __init__(self):

        self.game_loop()

    def game_loop(self):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = 3
                    return None

            screen.fill(white)
            pygame.display.update()

#Game()