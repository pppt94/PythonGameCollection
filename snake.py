import pygame

pygame.init()

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
snake_size = 10

gamedead = False
head_x = scr_width / 2
head_y = scr_height / 2
inc_x = 0
inc_y = 0
clock = pygame.time.Clock()

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


    head_x += inc_x
    head_y += inc_y
    screen.fill(black)
    pygame.draw.rect(screen, red, [head_x, head_y, snake_size, snake_size])
    pygame.display.update()

    clock.tick(fps)


pygame.quit()
quit()