import pygame
import time
import random
pygame.init()

# boundary w/h

dis_width = 800
dis_height = 600

x1 = dis_width/2
y1 = dis_height/2

snake_block = 10

x1_change = 0
y1_change = 0

snake_speed = 30
snake_length = 1


font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2-75, dis_height/2-30])

dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("Snake game")

white=(255, 255, 255)
black=(0, 0, 0)
blue=(0, 0, 255)
red=(255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 102)

game_over = False
clock = pygame.time.Clock()

foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

snake_list = []

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -snake_block
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = snake_block

        print(event)
    
    x1 += x1_change
    y1 += y1_change

    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True

    dis.fill(white)
    pygame.draw.rect(dis, black, [foodx, foody, snake_block, snake_block])
    snake_list.append((x1, y1))
    if len(snake_list) > snake_length:
        del snake_list[0]
    
    for x in snake_list[:-1]:
        if x == (x1, y1):
            game_over = True

    # pygame.draw.rect(dis, blue, [x1, y1, 10, 10])

    for x in snake_list:
        print(snake_length)
        pygame.draw.rect(dis, blue, [x[0], x[1], snake_block, snake_block])

    pygame.display.update() 

    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        snake_length += 1
        print("Yummy!!")

    clock.tick(snake_speed)

message("You Died", red)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()