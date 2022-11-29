import pygame
from random import randrange
from pygame. constants import QUIT

pygame.init()

screen = wight, hight = 800,600
BLACK = 0, 0, 0
WHITE = 255, 255, 255

main_surfase = pygame.display.set_mode(screen)

ball = pygame.Surface((20,20))
ball.fill ((WHITE))
ball_rect = ball.get_rect()
ball_speed = [1, 1]

is_working = True
while is_working:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

    ball_rect = ball_rect.move(ball_speed)

    if ball_rect.bottom >= hight or ball_rect.top <= 0:
        ball_speed[1] = -ball_speed[1]
        ball.fill ((randrange(255), randrange(255), randrange(255)))

    if ball_rect.right >= wight or ball_rect.left <= 0:
        ball_speed[0] = -ball_speed[0]
        ball.fill ((randrange(255), randrange(255), randrange(255)))

    main_surfase.fill((BLACK))
    main_surfase.blit(ball, ball_rect)
    pygame.display.flip()