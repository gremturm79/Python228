import time
import random
import pygame

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((800, 600))
pygame.display.update()
pygame.display.set_caption('Snake game by Pythonist')

x1 = dis_width / 2
y1 = dis_height / 2
snake_block = 10

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()
snake_speed = 30

font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 2, dis_height / 2])


game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            if event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            if event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            if event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
    pygame.display.update()
    clock.tick(snake_speed)

message('You lost', red)
pygame.display.update()
time.sleep(2)


pygame.quit()
quit()
