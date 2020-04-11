#파이게임 원하는 이미지 불러오기

import pygame
pygame.init()

#창 설정하기
width, height = 640, 480
size = (width, height)
screen = pygame.display.set_mode(size)

#이미지 불러오기
player = pygame.image.load('exresources/images/asf.png')

#창 종료 이벤트 처리까지 유지하기
while True:
    #화면을 채우고 다시 그리기
    screen.fill((255,255,255))
    screen.blit(player, (100,100))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)