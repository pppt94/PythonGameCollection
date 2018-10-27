import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('I am snake. Python Snake.')

#define colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


gamedead = False
head_x = 50
head_y = 50
inc_x = 0
inc_y = 0
clock = pygame.time.Clock()

while not gamedead:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamedead = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                inc_y = 10
                inc_x = 0
            elif event.key == pygame.K_UP:
                inc_y = -10
                inc_x = 0
            elif event.key == pygame.K_LEFT:
                inc_x = -10
                inc_y = 0
            elif event.key == pygame.K_RIGHT:
                inc_x = 10
                inc_y = 0


    head_x += inc_x
    head_y += inc_y
    pygame.draw.rect(screen, red, [head_x, head_y, 15, 15])
    pygame.display.update()

    clock.tick(5)


pygame.quit()
quit()