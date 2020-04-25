#피하기 게임 - rock03.py
#운석 이미지 그리기
import pygame
import random
#변수 설정
WHITE = (225,225,225)
black = (0,0,0)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

#파이게임 초기화 및 화면 설정
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

#키 반복 설정하기
pygame.key.set_repeat(1)

#이미지 불러오기
#화면 중앙 하단 배치 : conterx, bottom속성 사용하기
player_url = 'resources/d_images/saram.png'
player_img = pygame.image.load(player_url)
player_pos = player_img.get_rect(centerx = SCREEN_WIDTH // 2,
                                 bottom = SCREEN_HEIGHT)
#운석 이미지 불러오기
khimchie_url = 'resources/d_images/khimchie.png'
khimchie_img = pygame.image.load(khimchie_url)
#rock = list()
khimchies = []
for cnt in range(3):
    khimchie_pos = khimchie_img.get_rect(left = 200 * cnt +100, top = 100)
    khimchies.append(khimchie_pos)
    print(khimchie_pos)

#게임 루프
while True:
    #화면 배경색으로 채우기
    screen.fill(black)

    # 키 입력 처리
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        exit()
    elif event.type == pygame.KEYDOWN:
        # 방향키로 캐릭터 이동하기
        if event.key == pygame.K_LEFT:
            player_pos.left -= 5
        elif event.key == pygame.K_RIGHT:
            player_pos.left += 5
        # 벽 충돌 처리
        if player_pos.left < 0:
            player_pos.left = 0
        elif player_pos.right > SCREEN_WIDTH:
            player_pos.right = SCREEN_WIDTH

    #적 내려오기
    for one in khimchies:
        one.top +=10
        if one.bottom > SCREEN_HEIGHT:
            one.top = -100
            one.left = random.randint(0, SCREEN_WIDTH - khimchie_img.get_width())

    #이미지 그리기 및 화면 업데이트
    screen.blit(player_img, player_pos)

    for one in khimchies:
        screen.blit(khimchie_img, one)
    pygame.display.flip()

    #프레임 설정
    clock.tick(60)

