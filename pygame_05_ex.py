import pygame
width, height = 640,480
size = (width, height)
screen = pygame.display.set_mode(size)

google = pygame.image.load('exresources/images/e.png')

while True:
    screen.fill((0,0,0))
    google_width = google.get_width()
    google_height = google.get_height()
    for y in range(height // google_height+1):
        for x in range(width // google_width+1):
            screen.blit(google, ((x * 100), (y * 100)))
    pygame.display.flip()

    #닫기 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
