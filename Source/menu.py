import pygame
from Source import snake, pytris, python_mind, screen

pygame.init()


class Menu:
    """Class used to building & navigating menu."""

    def __init__(self):

        self.select = "Tetris"
        self.menu_eater = pygame.image.load('../Graphics/Menu/menu_eater.png')
        self.menu_pytris = pygame.image.load('../Graphics/Menu/menu_pytris.png')
        self.menu_mind = pygame.image.load('../Graphics/Menu/menu_mind.png')
        self.game_mind = python_mind.Game()
        self.game_snake = snake.Game()
        self.game_tetris = pytris.Game()
        self.menu_loop()

    def menu_loop(self):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
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
                        elif self.select == "Tetris":
                            self.game_tetris.game_loop()

            screen.screen.blit(self.menu_pytris, (0, 0))

            if self.select == "Master":
                screen.screen.blit(self.menu_mind, (0, 0))
            elif self.select == "Tetris":
                screen.screen.blit(self.menu_pytris, (0, 0))
            else:
                screen.screen.blit(self.menu_eater, (0, 0))
            pygame.display.update()


Menu()
