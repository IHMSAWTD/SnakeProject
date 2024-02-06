import os
import time

import pygame
from random import randrange
import random
import string
import sys
from PIL import ImageGrab

# for i in range(1,20):
#     os.mkdir(f'/home/ub/PycharmProjects/SnakeProject/validation/{i}')



n_spep_after_eat = 0
steps = 0
RES = 800
SIZE = 50

x,y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0,RES,SIZE), randrange(0,RES,SIZE)

dirs = {'W':True,'S':True,'D':True,'A':True}

lenght = 1

snake = [(x,y)]

dx, dy = 0, 0
fps = 5

pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()

def generate_random_string(length=10):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return random_string



def take_screen():
    random_name = generate_random_string()
    filename = f'..//validation/{lenght}/{random_name}.jpg'
    bbox = (560, 180,1360, 975)
    image = ImageGrab.grab(bbox=bbox)
    image.save(filename)

while True:
    sc.fill(pygame.Color('black'))
    [(pygame.draw.rect(sc, pygame.Color('green'), (i,j,SIZE,SIZE))) for i,j in snake]
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE))

    pygame.display.flip()
    clock.tick(fps)
    t1, t2 = x, y
    l2 = lenght
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))

    snake = snake[-lenght:]
   # print(f'{x}-----------{t1}')
    #print(x == t1)
    # if lenght != l2 :
    #     steps +=1
    #    # image = ImageGrab(bbox = (10,10, 1000,1000))
    #     #name = f"1_{lenght}"
    #     #image.save(f'images/')
    # print(steps)


    if t1 != x or t2 !=y:
        steps +=1
        if steps != n_spep_after_eat -1 and steps != n_spep_after_eat+1 :
            take_screen()



    print(lenght)
    if snake[-1] == apple:
        n_spep_after_eat = steps
        lenght += 1

        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)

        #take_screen()
    if steps == n_spep_after_eat+1:
        pass
        #take_screen()

    if x < 0 or x > RES - SIZE or y<0 or y >  RES - SIZE:
        #take_screen()
        break

    if len(snake) != len(set(snake)):
        break


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    key = pygame.key.get_pressed()
    #print(key.__str__())
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'D': True, 'A': True}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W':False,'S':True,'D':True,'A':True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W':True,'S':True,'D':False,'A':True}
    if key[pygame.K_d] and dirs['D']:
        dirs = {'W':True,'S':True,'D':True,'A':False}
        dx, dy = 1, 0


