# 1024 x  600크기의 창만들기
import pygame
import time

pygame.init()
width = 1024
heigh = 600
win_size = (width,heigh)
screen = pygame.display.set_mode(win_size)

pygame.draw.rect(screen, (200,200,200), [10,10,500,50], 2)
pygame.display.flip()

time.sleep(2)