import pygame
import snake
import python_mind
import text

pygame.init()
clock = pygame.time.Clock()

#define screen
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption('Main Menu')
fps = 5

#define colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gold = (255, 215, 0)

class Menu():

    def __init__(self):

        self.select = "Tetris"
        self.menu_eater = pygame.image.load('Graphics/menu_eater.png')
        self.menu_pytris = pygame.image.load('Graphics/menu_pytris.png')
        self.menu_mind = pygame.image.load('Graphics/menu_mind.png')
        self.game_mind = python_mind.Game()
        self.game_snake = snake.Game()
        self.menu_loop()

    def menu_loop(self):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if self.select == "Master":
                            self.select = "Tetris"
                        else:
                            self.select = "Snake"
                    elif event.key == pygame.K_LEFT:
                        if self.select == "Snake":
                            self.select = "Tetris"
                        else:
                            self.select = "Master"
                    elif event.key == pygame.K_RETURN:
                        if self.select == "Snake":
                            self.game_snake.game_loop()
                        elif self.select == "Master":
                            self.game_mind.game_loop()
                    elif event.key == pygame.K_q:
                        pygame.quit()

            screen.blit(self.menu_pytris, (0, 0))

            if self.select == "Master":
                screen.blit(self.menu_mind, (0, 0))
            elif self.select == "Tetris":
                screen.blit(self.menu_pytris, (0, 0))
            else:
                screen.blit(self.menu_eater, (0, 0))
            pygame.display.update()

Menu()
