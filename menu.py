import pygame
import snake
import text

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

class Menu():

    def __init__(self):


        self.title = text.Text("Python Game Collection", red, (scr_width / 2, scr_height / 2 - 300), 100)
        self.choose_text = text.Text("Choose game!", red, (scr_width / 2, scr_height / 2 - 150), 75)
        self.select = "Master"
        self.menu_loop()

    def menu_loop(self):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if self.select == "Tetris":
                            self.select = "Master"
                        else:
                            self.select = "Snake"
                    elif event.key == pygame.K_LEFT:
                        if self.select == "Snake":
                            self.select = "Master"
                        else:
                            self.select = "Tetris"
                    elif event.key == pygame.K_RETURN:
                        if self.select == "Snake":
                            snake.Game()

            #center (315, 270), (250, 180)
            field = pygame.Rect((315, 330), (250, 180))
            field2 = pygame.Rect((33, 330), (250, 180))
            field3= pygame.Rect((598, 330), (250, 180))
            screen.fill(white)
            self.title.print_text()
            self.choose_text.print_text()
            if self.select == "Master":
                pygame.draw.ellipse(screen, gold, field)
                pygame.draw.ellipse(screen, red, field2)
                pygame.draw.ellipse(screen, red, field3)
            elif self.select == "Tetris":
                pygame.draw.ellipse(screen, red, field)
                pygame.draw.ellipse(screen, gold, field2)
                pygame.draw.ellipse(screen, red, field3)
            else:
                pygame.draw.ellipse(screen, red, field)
                pygame.draw.ellipse(screen, red, field2)
                pygame.draw.ellipse(screen, gold, field3)
            pygame.display.update()



Menu()