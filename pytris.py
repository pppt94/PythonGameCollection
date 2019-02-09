import pygame
import random
import text

pygame.init()
pygame.display.init()
pygame.display.list_modes()
clock = pygame.time.Clock()

#define screen
scr_width = 880
scr_height = 720
screen = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption('Error Eater')
fps = 5
block_size = 30
x_cor = 290
y_cor = 90

#define colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gold = (255, 215, 0)
orange = (255, 120, 0)
gray = (128, 128, 128)
brown = (150, 75, 0)

#define shapes
I = [['..X..',
      '..X..',
      '..X..',
      '..X..',
      '.....'],
     ['.....',
      'XXXX.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.XX..',
      '.XX..',
      '.....']]

S = [['.....',
      '.....',
      '..XX.',
      '.XX..',
      '.....'],
     ['.....',
      '..X..',
      '..XX.',
      '...X.',
      '.....']]

Z = [['.....',
      '.....',
      '.XX..',
      '..XX.',
      '.....'],
     ['.....',
      '..X..',
      '.XX..',
      '.X...',
      '.....']]

T = [['.....',
      '..X..',
      '.XXX.',
      '.....',
      '.....'],
     ['.....',
      '..X..',
      '..XX.',
      '..X..',
      '.....'],
     ['.....',
      '.....',
      '.XXX.',
      '..X..',
      '.....'],
     ['.....',
      '..X..',
      '.XX..',
      '..X..',
      '.....']]

J = [['.....',
      '..X..',
      '..X..',
      '.XX..',
      '.....'],
     ['.....',
      '.X...',
      '.XXX.',
      '.....',
      '.....'],
     ['.....',
      '..XX.',
      '..X..',
      '..X..',
      '.....'],
     ['.....',
      '.....',
      '.XXX.',
      '...X.',
      '.....']]

L = [['.....',
      '..X..',
      '..X..',
      '..XX.',
      '.....'],
     ['.....',
      '.....',
      '.XXX.',
      '.X...',
      '.....'],
     ['.....',
      '.XX..',
      '..X..',
      '..X..',
      '.....'],
     ['.....',
      '...X.',
      '.XXX.',
      '.....',
      '.....']]



shapes = [I, O, S, Z, T, J, L]
colors = [red, green, blue, gold, orange, gray, brown]

class Block():

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.shape = random.choice(shapes)
        self.color = colors[shapes.index(self.shape)]
        self.rotation = 0

    def convert_shape(self):

        positions = []
        format = self.shape[self.rotation % len(self.shape)]

        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == 'X':
                    positions.append((self.x + j, self.y + i))

        for i, pos in enumerate(positions):
            positions[i] = (pos[0] - 2, pos[1] - 4)

        return positions

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

    def draw_grid(self):

        for i in range(1, len(self.grid)):
            pygame.draw.line(screen, (128, 128, 128), (x_cor, y_cor+i*block_size), (x_cor+300, y_cor+i*block_size))
            for j in range(1, len(self.grid[i])):
                pygame.draw.line(screen, (128, 128, 128), (x_cor+j*block_size, y_cor), (x_cor+j*block_size, y_cor+600))

    def draw_board(self):

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                pygame.draw.rect(screen, self.grid[i][j], (x_cor+j*block_size, y_cor+i*block_size, block_size, block_size), 0)

    def draw_next_shape(self, shape):

        format = shape.shape[shape.rotation % len(shape.shape)]

        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == 'X':
                    pygame.draw.rect(screen, shape.color, (660 +j*block_size, 200+i*block_size, block_size, block_size), 0)

    def check_space(self, shape):

        free_position = []
        for i in range(20):
            for j in range(10):
                if self.grid[i][j] == (0, 0, 0):
                    free_position.append((j, i))

        conv_shape = shape.convert_shape()

        for position in conv_shape:
            if position not in free_position:
                if position[1] > -1:
                    return False

        return True

    def check_full(self):

        for x, y in self.blocks_positions:
            if y < 1:
                return True
        return False

    def check_row(self):

        rows = 0

        for i in range(len(self.grid)-1, -1, -1):
            row = self.grid[i]
            if (0, 0, 0) not in row:
                rows += 1
                level = i
                for j in range(len(row)):
                    try:
                        del self.blocks_positions[(j, i)]
                    except:
                        continue
        if rows > 0:
            for x, y in sorted(list(self.blocks_positions))[::-1]:
                if y < level:
                    new_pos = (x, y + rows)
                    self.blocks_positions[new_pos] = self.blocks_positions.pop((x, y))

        return rows * 10

class Game():

    def __init__(self):
        self.menu = pygame.image.load('Graphics/pytris_menu.png')
        self.over = pygame.image.load('Graphics/pytris_over.png')
        self.help = pygame.image.load('Graphics/pytris_help.png')
        self.state = 0
        self.score = 0
        self.pause = 0


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

        self.score = 0
        change_piece = False
        board = Board()
        curr_piece = Block(5, 0)
        next_piece = Block(5, 0)
        fall_time = 0
        fall_speed = 0.27

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = 3
                    return None
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        curr_piece.x += 1
                        if not board.check_space(curr_piece):
                            curr_piece.x -= 1
                    elif event.key == pygame.K_LEFT:
                        curr_piece.x -= 1
                        if not board.check_space(curr_piece):
                            curr_piece.x += 1
                    elif event.key == pygame.K_DOWN:
                        curr_piece.y += 1
                        if not board.check_space(curr_piece):
                            curr_piece.y -= 1
                    elif event.key == pygame.K_SPACE:
                        curr_piece.rotation += 1
                        if not board.check_space(curr_piece):
                            curr_piece.rotation -= 1
                    elif event.key == pygame.K_p:
                        self.pause = 1
                        while self.pause == 1:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    self.state = 3
                                    return None
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_p:
                                        self.pause = 0
                                        break

                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    if position[0] >= 55 and position[0] <= 205:
                        if position[1] >= 15 and position[1] <= 165:
                            self.state = 2
                            return None
                        elif position[1] >= 195 and position[1] <= 345:
                            return None
                        elif position[1] >= 375 and position[1] <= 525:
                            self.state = 0
                            return None
                        elif position[1] >= 555 and position[1] <= 705:
                            self.state = 3
                            return None

            fall_time += clock.get_rawtime()
            clock.tick()
            if fall_time / 1000 > fall_speed:
                fall_time = 0
                curr_piece.y += 1
                if not (board.check_space(curr_piece)) and curr_piece.y > 0:
                    curr_piece.y -= 1
                    change_piece = True

            curr_piece_position = curr_piece.convert_shape()

            for i in range(len(curr_piece_position)):
                x, y = curr_piece_position[i]
                if y > -1:
                    board.grid[y][x] = curr_piece.color

            if change_piece:
                for i in curr_piece_position:
                    pos = (i[0], i[1])
                    board.blocks_positions[pos] = curr_piece.color
                curr_piece = next_piece
                next_piece = Block(5, 0)
                change_piece = False
                inc = board.check_row()
                self.score += inc
                if inc > 0:
                    fall_speed -= 0.01

            if board.check_full():
                self.state = 1
                return None

            screen.fill(black)
            board.draw_board()
            board.create_grid()
            board.draw_grid()
            board.draw_next_shape(next_piece)
            text.Text(str(self.score), red, (735, 545), 100).print_text()
            screen.blit(self.menu, (0, 0))
            pygame.display.update()

    def game_over(self):

        screen.blit(self.over, (0, 0))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.state = 0
                        return None
                    if event.key == pygame.K_ESCAPE:
                        self.state = 3
                        return None
                if event.type == pygame.QUIT:
                    self.state = 3
                    return None

    def help_game(self):

        screen.blit(self.help, (0, 0))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.state = 0
                        return None
                if event.type == pygame.QUIT:
                    self.state = 3
                    return None
