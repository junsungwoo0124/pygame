
import pygame
import random

#변수 설정 (튜플)
WHITE = (255,255,255)
BLACK = (0, 0, 0)
YELLOW = (255, 255,0)

SCREEN_WIDTH = 600
SCREEN_HEIGH = 800
SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGH)

#변수 초기화
score = 0
khimchie_num = 1
gameover = False

#파이게임 초기화
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("go")
frame = pygame.time.Clock()
pygame.key.set_repeat(1)

#글꼴 설정
small_font = pygame.font.SysFont("Agency FB", 36)
large_font = pygame.font.SysFont("HYNAML", 72)

#이미지 불러오기
player_url = 'resources/d_images/saram.png'
player_img = pygame.image.load(player_url)
player_pos = player_img.get_rect(centerx = SCREEN_WIDTH //2,
                                 bottom = SCREEN_HEIGH)
# 적 이미지 불러오기
khimchie_url = "resources/d_images/khimchie.png"
khimchie_img = pygame.image.load(khimchie_url)
#khimchies 는 적의 좌표와 속도를 리스트로 저장하는 리스트다
khimchies_info = []
for one in range(khimchie_num):
    khimchie_pos = khimchie_img.get_rect(left = random.randint(0,SCREEN_WIDTH - khimchie_img.get_width()),
                                         bottom = -100* one)
    khimchie_speed = random.randint(5, 15)
    khimchies_info.append([khimchie_pos,khimchie_speed])

#음악 불러오기
pygame.mixer.init()
bgm_url = 'resources/audio/bgm.mp3'
pygame.mixer.music.load(bgm_url)
pygame.mixer.music.play(-1)

# 게임 루프 생성
while True:
    #이벤트 처리
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if not gameover and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_pos.left -= 5
            elif event.key == pygame.K_RIGHT:
                player_pos.right += 5

    #벽 충돌 처리
    if player_pos.left<0:
        player_pos.left = 0
    elif player_pos.right > SCREEN_WIDTH:
        player_pos.right = SCREEN_WIDTH

    #적 이동하기
    if not gameover:
        for one in khimchies_info:
            one[0].top += one[1]
            if one[0].top > 800:
                one[0].left = random.randint(0, SCREEN_WIDTH - khimchie_img.get_width())
                one[0].top = -100
                score += 1
                if (score % 20 == 0):
                    khimchie_pos = khimchie_img.get_rect(
                        left=random.randint(0, SCREEN_WIDTH - khimchie_img.get_width()),
                        bottom=-100 * one)
                    khimchie_speed = random.randint(5, 15)
                    khimchies_info.append([khimchie_pos, khimchie_speed])

    #적 충돌 처리
    for one in khimchies_info:
        if one[0].colliderect(player_pos):
            gameover = True

    #화면 이미지 출력하기
    screen.fill(BLACK)
    screen.blit(player_img, player_pos)
    for one in khimchies_info:
        screen.blit(khimchie_img, one[0])

    #점수출력
    score_img = small_font.render("SCORE: {}".format(score), True, YELLOW)
    screen.blit(score_img, (10,10))

    #게임 종료
    if gameover:
        gameover_img = large_font.render("김치 싸다구", True, YELLOW)
        screen.blit(gameover_img, (SCREEN_WIDTH // 2 - gameover_img.get_width() // 2,
                                   SCREEN_HEIGH // 2 - gameover_img.get_height() // 2))

    pygame.display.flip()
    frame.tick(60)



