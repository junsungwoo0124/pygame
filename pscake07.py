import pygame
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("뱀으로 세계정복하기")
clock = pygame.time.Clock()

#변수 초기화
BLACK = (0, 0, 0)       #배경 색
GRAY = (128, 128, 128)      #격자 색
BLUE = (30, 7, 255)      #뱀 색
GREEN = (0, 255, 0)     #먹이 색
YELLOW = (255,255,0)    #글자색
RED = (120, 60, 40)

LEFT = 0
RIGHT = 1
UP = 3
DOWN = 4
direction = DOWN


GAMEOVER = False

score = 0
score_font = pygame.font.SysFont("comicsans", 40)
GAMEOVER_font = pygame.font.SysFont("comicsans", 100)

CELL_SIZE = 40
COL_COUNT = SCREEN_WIDTH // CELL_SIZE
ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE

#뱀 좌표 리스트(화면 중앙)
bodies = [(COL_COUNT // 2, ROW_COUNT // 2)]

#먹이 10개 리스트 만들기
foods = []

# 먹이 추가 함수
def add_food():
    while True:
        c_idx = random.randint(0, COL_COUNT - 1)
        r_idx = random.randint(0, ROW_COUNT - 1)
        f_pos = (c_idx, r_idx)
        if f_pos not in bodies and f_pos not in foods:
            foods.append(f_pos)
            break

for _ in range(10):
    add_food()

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    if event.type == pygame.KEYDOWN and not GAMEOVER:
        if event.key == pygame.K_LEFT:
            direction = LEFT
        if event.key == pygame.K_RIGHT:
            direction = RIGHT
        if event.key == pygame.K_UP:
            direction = UP
        if event.key == pygame.K_DOWN:
            direction = DOWN


    # 뱀 머리 추출 후 다음 방향 이동
    head = bodies[0]
    c_idx, r_idx = head[0], head[1]
    if direction == LEFT:
        c_idx -= 1
    elif direction == RIGHT:
        c_idx += 1
    elif direction == UP:
        r_idx -= 1
    elif direction == DOWN:
        r_idx += 1


    head_pos = (c_idx, r_idx)

    if head_pos in bodies or \
            c_idx < 0 or \
            r_idx < 0 or \
            c_idx > COL_COUNT or \
            r_idx > ROW_COUNT:
        GAMEOVER = True

    bodies.insert(0, head_pos)

    if head_pos in foods:
        score += 10
        foods.remove(head_pos)
        add_food()
    else:
        bodies.pop()

    #화면 초기화
    screen.fill(BLACK)

    #격자 그리기
    for c_idx in range(COL_COUNT):
        for r_idx in range(ROW_COUNT):
            rect = (c_idx * CELL_SIZE, r_idx * CELL_SIZE,
                    CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, rect, 1)
    #  뱀 그리기
    for one in bodies:
        rect = (one[0] * CELL_SIZE, one[1] * CELL_SIZE,
                CELL_SIZE, CELL_SIZE)
        if one == bodies[0]:
            pygame.draw.rect(screen, RED, rect)
        else:
            pygame.draw.rect(screen, BLUE, rect)
        pygame.display.update()

    #   먹이 그리기
    for one in foods:
        rect = (one[0] * CELL_SIZE, one[1] * CELL_SIZE,
                CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, GREEN, rect)


    score_img = score_font.render(f"SCORE: {score}", True, YELLOW)
    screen.blit(score_img, (10, 10))

    if GAMEOVER:
        GAMEOVER_img = GAMEOVER_font.render(f"GAMEOVER", True, YELLOW)
        screen.blit(GAMEOVER_img, (SCREEN_WIDTH // 2 - SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 - SCREEN_HEIGHT // 4))


    pygame.display.update()
    clock.tick(10)

pygame.quit()

