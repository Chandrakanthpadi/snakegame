import pygame
import random

width=400
height=300
INC = 10

blue = (0, 0, 255)
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

f=open('Highscore.txt','r')
hiscore = f.read(1)
f.close()

def gamestart():

    pygame.init()
    dis = pygame.display.set_mode((width,height))
    pygame.display.update()

    x_change=10
    y_change=0

    snake=[[200,150]]
    food=[round(random.randrange(0,width-INC,10)),round(random.randrange(0,height-INC,10))]
    pygame.display.set_caption('Snake game')
    game_over = False

    clock = pygame.time.Clock()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    y_change = INC
                    x_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -INC
                    x_change = 0
                elif event.key == pygame.K_RIGHT:
                    y_change = 0
                    x_change = INC
                elif event.key == pygame.K_LEFT:
                    y_change = 0
                    x_change = -INC
        dis.fill(white)
        a = snake[0][0]+x_change
        b = snake[0][1]+y_change
        if [a, b] in snake:
            game_over=True
        snake.insert(0,[a,b])
        if snake[0] != food:
            snake=snake[:-1]
        else:
            food = [round(random.randrange(0, width - INC, 10)), round(random.randrange(0, height - INC, 10))]
        pygame.draw.circle(dis, red, food, 5, 0)
        if snake[0][0]>=width or snake[0][0]<=0 or snake[0][1]>=height or snake[0][1]<=0:
            game_over = True
        pygame.draw.circle(dis, black,snake[0], 5, 0)
        for x in snake[1:]:
            pygame.draw.circle(dis,blue,x,5,0)
        pygame.display.update()
        clock.tick(10)
    if len(snake)-1>int(hiscore):
        f=open('Highscore.txt','w')
        f.write(str(len(snake)-1))
        f.close()
    pygame.quit()
