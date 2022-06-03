import pygame
import time
import random

class snake_game:

    def __init__(self, w=800, h=600): # initialize pygame envrionment
        pygame.init()

        # boundary w/h

        self.dis_width = w
        self.dis_height = h
    
        self.snake1_x = 100
        self.snake1_y = 100

        self.snake2_x = 500
        self.snake2_y = 500

        self.snake_block = 10

        self.x1_change = 10
        self.y1_change = 0

        self.x2_change = 10
        self.y2_change = 0

        self.snake_speed = 30
        self.snake1_length = 1
        self.snake2_length = 1


        self.dis=pygame.display.set_mode((self.dis_width,self.dis_height))
        pygame.display.set_caption("Snake game")

    def message(self, msg, color):
        font_style = pygame.font.SysFont(None, 50)
        mesg = font_style.render(msg, True, color)
        self.dis.blit(mesg, [self.dis_width/2-75, self.dis_height/2-30])


    def play(self):
        white=(255, 255, 255)
        black=(0, 0, 0)
        blue=(0, 0, 255)
        red=(255, 0, 0)
        green = (0, 255, 0)
        yellow = (255, 255, 102)


        game_over = False
        clock = pygame.time.Clock()

        foodx = round(random.randrange(0, self.dis_width - self.snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, self.dis_height - self.snake_block) / 10.0) * 10.0

        snake1_list = []
        snake2_list = []

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.x1_change = -self.snake_block
                        self.y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        self.x1_change = self.snake_block
                        self.y1_change = 0
                    elif event.key == pygame.K_UP:
                        self.x1_change = 0
                        self.y1_change = -self.snake_block
                    elif event.key == pygame.K_DOWN:
                        self.x1_change = 0
                        self.y1_change = self.snake_block
                    if event.key == pygame.K_a:
                        self.x2_change = -self.snake_block
                        self.y2_change = 0
                    elif event.key == pygame.K_d:
                        self.x2_change = self.snake_block
                        self.y2_change = 0
                    elif event.key == pygame.K_w:
                        self.x2_change = 0
                        self.y2_change = -self.snake_block
                    elif event.key == pygame.K_s:
                        self.x2_change = 0
                        self.y2_change = self.snake_block

                print(event)
            
            self.snake1_x += self.x1_change
            self.snake1_y += self.y1_change
            self.snake2_x += self.x2_change
            self.snake2_y += self.y2_change

            # if self.snake1_x >= self.dis_width or self.snake1_x < 0 or self.snake1_y >= self.dis_height or self.snake1_y < 0:
            #     game_over = True
            
            # if self.snake2_x >= self.dis_width or self.snake2_x < 0 or self.snake2_y >= self.dis_height or self.snake2_y < 0:
            #     game_over = True

            self.dis.fill(white)
            pygame.draw.rect(self.dis, black, [foodx, foody, self.snake_block, self.snake_block])
            snake1_list.append((self.snake1_x, self.snake1_y))
            if len(snake1_list) > self.snake1_length:
                del snake1_list[0]
            
            snake2_list.append((self.snake2_x, self.snake2_y))
            if len(snake2_list) > self.snake2_length:
                del snake2_list[0]

            # suicide

            for x in snake1_list[:-1]:
                if x == (self.snake1_x, self.snake1_y):
                    game_over = True
            
            for x in snake2_list[:-1]:
                if x == (self.snake2_x, self.snake2_y):
                    game_over = True

            # bump into others
            
            for x in snake1_list:
                if x == snake2_list[-1]:
                    game_over = True

            for x in snake2_list:
                if x == snake1_list[-1]:
                    game_over = True

            # pygame.draw.rect(dis, blue, [x1, y1, 10, 10])

            for x in snake1_list:
                #print(self.snake_length)
                pygame.draw.rect(self.dis, blue, [x[0], x[1], self.snake_block, self.snake_block])

            for x in snake2_list:
                #print(self.snake_length)
                pygame.draw.rect(self.dis, green, [x[0], x[1], self.snake_block, self.snake_block])

            pygame.display.update() 

            if self.snake1_x == foodx and self.snake1_y == foody:
                foodx = round(random.randrange(0, self.dis_width - self.snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, self.dis_height - self.snake_block) / 10.0) * 10.0
                self.snake1_length += 1
                print("Yummy!!")
            elif self.snake2_x == foodx and self.snake2_y == foody:
                foodx = round(random.randrange(0, self.dis_width - self.snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, self.dis_height - self.snake_block) / 10.0) * 10.0
                self.snake2_length += 1
                print("Yummy!!")

            clock.tick(self.snake_speed)

        self.message("You Died", red)
        pygame.display.update()
        time.sleep(2)

        pygame.quit()
        quit() 

if __name__ == '__main__':
    game = snake_game()
    
    # game loop
    game.play()


