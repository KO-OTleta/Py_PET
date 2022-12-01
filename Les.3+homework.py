import pygame
import random
from os import listdir
from pygame. constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

FPS = pygame.time.Clock()
screen = wight, hight = 800,600
PURPLE = 128, 0, 128
font = pygame.font.SysFont('Verdana', 32)
main_surfase = pygame.display.set_mode(screen)
IMGS_PATH = 'goose'
goose_imgs = [pygame.image.load(IMGS_PATH + '/' + file).convert_alpha() for file in listdir(IMGS_PATH)]
goose = goose_imgs[0]
goose_rect = goose.get_rect()
goose_speed = 5

def create_enemy():
    enemy = pygame.transform.scale(pygame.image.load('enemy.png').convert_alpha(), (100, 40))
    enemy_rect = pygame.Rect(wight, random.randint(0, hight), *enemy.get_size())
    enemy_speed = random.randint(1, 4)
    return [enemy, enemy_rect, enemy_speed]

CREATE_ENEMY = pygame.USEREVENT +1
pygame.time.set_timer(CREATE_ENEMY,2000) 

def create_bonus():
    bonus = pygame.transform.scale(pygame.image.load('bonus.png').convert_alpha(), (120, 200)) # як масштаюувати картинку по коофіцієнту? 
    bonus_rect = pygame.Rect(random.randint(10, wight/2), -250, *bonus.get_size()) # підняти спавн бонуса для комфортнішого відображення 
    bonus_speed = random.randint(1, 3)
    return [bonus, bonus_rect, bonus_speed]

bg = pygame.transform.scale(pygame.image.load('background.png').convert(), screen)
bgX = 0
bgX2 = bg.get_width()
bg_speed = 3

CREATE_BONUS = pygame.USEREVENT +2
pygame.time.set_timer(CREATE_BONUS, 3000) 

CHANGE_IMGS = pygame.USEREVENT +3
pygame.time.set_timer(CHANGE_IMGS, 125) 
img_index = 0

enemies = []
bonuses = []
scores = 0 

is_working = True
while is_working:

    FPS.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())

        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())

        if event.type == CHANGE_IMGS:
            img_index += 1
            if img_index == len(goose_imgs):
                img_index = 0
            goose = goose_imgs[img_index]

    pressed_keys = pygame.key.get_pressed()
    bgX -= bg_speed
    bgX2 -= bg_speed

    if bgX < -bg.get_width():
        bgX = bg.get_width()

    if bgX2 < -bg.get_width():
        bgX2 = bg.get_width()

    main_surfase.blit(bg, (bgX, 0))
    main_surfase.blit(bg, (bgX2, 0))

    main_surfase.blit(goose, goose_rect)
    main_surfase.blit(font.render(str(scores), True, PURPLE), (wight - 70, 0))  # зміна кольору лічильника бонусів

    for enemy in enemies:
        enemy[1] = enemy[1].move(-enemy[2], 0)
        main_surfase.blit(enemy[0], enemy[1])

        if enemy[1].left < -150:                     # відсунути деспавн за межі екрану для комфортнішого відображення
            enemies.pop(enemies.index(enemy))

        if goose_rect.colliderect(enemy[1]): 
            is_working = False

    for bonus in bonuses:
        bonus[1] = bonus[1].move(0, bonus[2])
        main_surfase.blit(bonus[0], bonus[1])

        if bonus[1].bottom > hight + 250:             # відсунути деспавн за межі екрану для комфортнішого відображення
            bonuses.pop(bonuses.index(bonus))

        if goose_rect.colliderect(bonus[1]):
            bonuses.pop(bonuses.index(bonus))
            scores += 1
    
    if pressed_keys[K_DOWN] and not goose_rect.bottom >= hight:
        goose_rect = goose_rect.move(0, goose_speed)

    if pressed_keys[K_UP] and not goose_rect.top <= 0:
        goose_rect = goose_rect.move(0, -goose_speed)

    if pressed_keys[K_LEFT] and not goose_rect.left <= 0:
        goose_rect = goose_rect.move(-goose_speed, 0)

    if pressed_keys[K_RIGHT] and not goose_rect.right >= wight:
        goose_rect = goose_rect.move(goose_speed, 0)

    pygame.display.flip()