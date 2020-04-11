import pygame

pygame.init()

width, height = 640, 480
size = (width, height)
screen = pygame.display.set_mode(size)

while True:
    #창 배경색 변경
    W = (255,225,205)
    screen.fill(W)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)