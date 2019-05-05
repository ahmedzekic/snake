import pygame
from snake import *


def ai_snake(map, snake, apple, algorithm, frequency):
    pygame.init()
    window = pygame.display.set_mode((map.width * 10, map.height * 10))
    pygame.display.set_caption("SNAKE")
    window.fill((255, 255, 255))
    pygame.display.update()
    if algorithm == snake.longest_path:
        goal = snake.tail[snake.tail_length]
    else:
        goal = apple.position
    path = algorithm(goal)
    k = 1
    side = None
    while not snake.end:
        pygame.time.delay(150)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
        window.fill((255, 255, 255))
        pygame.display.update()
        if not path:
            snake.go(side)
        elif snake.tail[0][0] < path[k][0]:
            snake.go('right')
            side = 'right'
        elif snake.tail[0][0] > path[k][0]:
            snake.go('left')
            side = 'left'
        elif snake.tail[0][1] < path[k][1]:
            snake.go('down')
            side = 'down'
        elif snake.tail[0][1] > path[k][1]:
            snake.go('up')
            side = 'up'

        pygame.draw.rect(window, (0, 255, 0), (snake.tail[0][0] * 10, snake.tail[0][1] * 10, 10, 10))
        for i in range(1, snake.tail_length + 1):
            pygame.draw.rect(window, (0, 255, 0), (snake.tail[i][0] * 10, snake.tail[i][1] * 10, 10, 10), 1)
        for o in map.obstacles:
            pygame.draw.rect(window, (255, 0, 0), (o[0] * 10, o[1] * 10, 10, 10))
        snake.snake_eats_apple(apple)
        pygame.draw.rect(window, (0, 0, 255), (apple.position[0] * 10, apple.position[1] * 10, 10, 10))
        if path and k == len(path) - 1 or k == frequency:
            k = 1
            if algorithm == snake.longest_path:
                goal = snake.tail[snake.tail_length]
            else:
                goal = apple.position
            path = algorithm(goal)
        else:
            k += 1
        if not snake.end:
            pygame.display.update()
    pygame.time.delay(500)
    pygame.quit()


def play(map, snake, apple):
    pygame.init()
    window = pygame.display.set_mode((M.width * 10, M.height * 10))
    pygame.display.set_caption("SNAKE")
    window.fill((255, 255, 255))
    pygame.display.update()
    left, right, up, down = False, False, False, False
    while not snake.end:
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
                snake.go('left')
            elif right:
                snake.go('right')
            elif up:
                snake.go('up')
            elif down:
                snake.go('down')
            pygame.draw.rect(window, (0, 0, 255), (apple.position[0] * 10, apple.position[1] * 10, 10, 10)) # drawing apple
            for i in range(0, S.tail_length + 1):
                pygame.draw.rect(window, (0, 255, 0), (snake.tail[i][0] * 10, snake.tail[i][1] * 10, 10, 10), 1)
            for o in map.obstacles:
                pygame.draw.rect(window, (255, 0, 0), (o[0] * 10, o[1] * 10, 10, 10))
            snake.snake_eats_apple(A)
            if not snake.end:
                pygame.display.update()
    pygame.time.delay(500)
    pygame.quit()


M = Map(30, 30)
M.add_obstacle((0, 2), (6, 2), False)
S = Snake(M)
A = Apple(M)
ai_snake(M, S, A, S.longest_path, 0)
#ai_snake(M, S, A, S.bfs, 1)
#ai_snake(M, S, A, S.dfs, 0)
#play(M, S, A)