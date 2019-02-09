import pygame
from Source import screen

pygame.init()


class Text:

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
        screen.screen.blit(self.text_font, self.text_rect)

    def change_colour(self, colour):

        self.colour = colour
