import pygame

pygame.init()
clock = pygame.time.Clock()

#define screen
scr_width = 800
scr_height = 600
screen = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption('I am snake. Python Snake.')
fps = 5

#define colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#define snake
snake_size = 20

def gameLoop():

    gamedead = False
    head_x = scr_width / 2
    head_y = scr_height / 2
    inc_x = 0
    inc_y = 0

    while not gamedead:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamedead = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    inc_y = snake_size
                    inc_x = 0
                elif event.key == pygame.K_UP:
                    inc_y = -snake_size
                    inc_x = 0
                elif event.key == pygame.K_LEFT:
                    inc_x = -snake_size
                    inc_y = 0
                elif event.key == pygame.K_RIGHT:
                    inc_x = snake_size
                    inc_y = 0

        if head_x >= scr_width or head_x <= 0 or head_y >= scr_height or head_y <= 0:
            gameOver()

        head_x += inc_x
        head_y += inc_y
        screen.fill(black)
        pygame.draw.rect(screen, red, [head_x, head_y, snake_size, snake_size])
        pygame.display.update()

        clock.tick(fps)

def gameOver():

    while True:
        screen.fill(white)
        font = pygame.font.SysFont(None, 25)
        screen_text = font.render("Press ESC or SPACE", True, red)
        screen.blit(screen_text, [scr_width/2, scr_height/2])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameLoop()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

gameLoop()
pygame.quit()
quit()