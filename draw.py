import pygame
from snake import *


M = Map(30, 30)
S = Snake(M)
A = Apple(M)
M.add_obstacle((3, 3), (10, 8), False)
M.add_obstacle((12, 12), (2, 19), False)
pygame.init()
window = pygame.display.set_mode((M.width * 10, M.height * 10))
pygame.display.set_caption("SNAKE")
window.fill((255, 255, 255))
pygame.display.update()
left, right, up, down = False, False, False, False
while not S.end:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
        window.fill((255, 255, 255))
        pygame.display.update()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and not right:
            left, right, up, down = True, False, False, False
        elif pressed[pygame.K_RIGHT] and not left:
            left, right, up, down = False, True, False, False
        elif pressed[pygame.K_UP] and not down:
            left, right, up, down = False, False, True, False
        elif pressed[pygame.K_DOWN] and not up:
            left, right, up, down = False, False, False, True

        if left:
            S.go('left')
        elif right:
            S.go('right')
        elif up:
            S.go('up')
        elif down:
            S.go('down')
        pygame.draw.rect(window, (0, 0, 255), (A.position[0] * 10, A.position[1] * 10, 10, 10)) # drawing apple
        for i in range(0, S.tail_length + 1):
            pygame.draw.rect(window, (0, 255, 0), (S.tail[i][0] * 10, S.tail[i][1] * 10, 10, 10), 1)
        for o in M.obstacles:
            pygame.draw.rect(window, (255, 0, 0), (o[0] * 10, o[1] * 10, 10, 10))
        S.snake_eats_apple(A)
        """for s in M.occupied:
            print(s, len(M.occupied))"""
        if not S.end:
            pygame.display.update()
pygame.time.delay(500)
pygame.quit()