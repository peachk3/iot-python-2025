import pygame # pygame 기본모듈 추가
from pygame.locals import QUIT # 종료처리
import sys # 운영체제 시스템 명령 

# 기본 변수
# pygmae 초기화
pygame.init()
# 윈도우(서피스) 설정
Surface = pygame.display.set_mode((640, 400)) ## tkinter -> root.geometry('640x400')
# fps(Frames Per Second) : 초당 프레임 - 프레임 속도 일정하게 유지하도록 사용됨
FPSCLOCK = pygame.time.Clock()
# title
pygame.display.set_caption('Pygame Basic') 

def main():
    while True:
        Surface.fill(color='azure')
        # Surface.fill((255, 255, 255))  # #FFFFFF = white (배경색) #0000000 / # 00FFFFFF  '00' -> alpha 투명도
        for event in pygame.event.get(): # 키보드, 마우스 이벤트 체크
            if event.type == QUIT: # WM_DELETE_WINDOW
                pygame.quit() # Ptgame 종료
                sys.exit()   # 윈도우앱 탈출
        
        pygame.display.update() # 지금까지 작성 코드를 윈도우 창에 표시 (화면 전체 업데이트) / (영역)-> 영역 지정시 해당 영역만 업데이트
        FPSCLOCK.tick(30) # 30FPS로 지정

if __name__ == '__main__':
    main()