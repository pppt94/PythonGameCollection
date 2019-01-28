import pygame

pygame.init()
clock = pygame.time.Clock()
#define screen
scr_width = 880
scr_height = 720
screen = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption('Error Eater')
fps = 5

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
        return (self.text_font, self.text_rect)

    def change_colour(self, colour):

        self.colour = colour
