# 이벤트 처리

import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_UP, K_RIGHT, K_DOWN 
import sys

x_coord = 640
y_coord = 400
pygame.init()
Surface = pygame.display.set_mode((x_coord, y_coord))
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Pygame Event') 
pygame.key.set_repeat(10, 10)  # 키보드 연속 움직임 풀링

def main():
    # 시작점 설정
    xpos = 50
    ypos = 50
    circle_size = 20
    while True:
        Surface.fill((255, 255, 255))
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                pygame.quit() 
                sys.exit()   

            elif event.type == KEYDOWN: # 키보드 입력이 시작되었으면
                if event.key == K_LEFT: # xpos - num
                    if xpos <= circle_size: xpos = circle_size # 20 -> circle 사이즈
                    else: xpos = xpos - 10 # xpos -= 10
                if event.key == K_RIGHT:
                    if xpos >= (x_coord - circle_size): xpos = (x_coord - circle_size)
                    else: xpos += 10 # xpos = xpos - 10
                if event.key == K_UP:
                    if ypos <= circle_size: ypos = circle_size
                    else: ypos -= 10
                if event.key == K_DOWN:
                    if ypos >= (y_coord - circle_size): ypos = (y_coord - circle_size)
                    else: ypos = ypos + 10
                # elif 사용 - 동시 입력시 움직임 오류 발생 가능성 O
        
        pygame.draw.circle(Surface, 'lightblue', (xpos, ypos), circle_size)

        pygame.display.update()
        FPSCLOCK.tick(30) 

if __name__ == '__main__':
    main()