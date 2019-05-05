from collections import deque
from map import Map
import random


class Snake:
    def __init__(self, map):
        self.map = map
        self.tail = [None] * map.width * map.height
        self.tail[0] = (map.width // 2, map.height // 2)
        self.map.occupied.add(self.tail[0])
        self.tail_length = 0
        self.start = False
        self.end = False

    def snake_eats_apple(self, apple):
        if self.tail[0] == apple.position:
            apple.generate(self.map)
            self.tail_length += 1
        if self.tail_length == self.map.width * self.map.height - 1:
            self.end = True
        Snake.move_snake(self)

    def move_snake(self):
        temp = self.tail[0]
        for i in range(1, self.tail_length + 1):
            temp_2 = self.tail[i]
            self.tail[i] = temp
            self.map.occupied.add(temp)
            temp = temp_2

    def go(self, side):
        self.start = True
        delete = self.tail[self.tail_length]
        if delete in self.map.occupied:
            self.map.occupied.remove(delete)
        if side == 'left':
            self.tail[0] = (self.tail[0][0] - 1, self.tail[0][1])
        if side == 'right':
            self.tail[0] = (self.tail[0][0] + 1, self.tail[0][1])
        if side == 'down':
            self.tail[0] = (self.tail[0][0], self.tail[0][1] + 1)
        if side == 'up':
            self.tail[0] = (self.tail[0][0], self.tail[0][1] - 1)
        self.end = self.end_of_game()
        self.map.occupied.add(self.tail[0])

    def end_of_game(self):
        if self.tail[0][0] < 0 or self.tail[0][0] == self.map.width:
            return True
        elif self.tail[0][1] < 0 or self.tail[0][1] == self.map.height:
            return True
        elif self.start and self.tail[0] in self.map.occupied:
            return True
        return False

    def find_neighbour(self, node, occupied, side):
        if side == 'left':
            neighbour = (node[0] - 1, node[1])
        elif side == 'right':
            neighbour = (node[0] + 1, node[1])
        elif side == 'up':
            neighbour = (node[0], node[1] - 1)
        elif side == 'down':
            neighbour = (node[0], node[1] + 1)
        if neighbour in occupied:
            return None
        elif neighbour[0] < 0 or neighbour[0] == self.map.width:
            return None
        elif neighbour[1] < 0 or neighbour[1] == self.map.height:
            return None
        return neighbour

    def bfs(self, goal):
        start = self.tail[0]
        visited = {start}
        queue = deque([(start, [])])
        sides = ['left', 'right', 'up', 'down']
        while queue:
            current, path = queue.popleft()
            visited.add(current)
            for i in range(4):
                neighbour = self.find_neighbour(current, self.map.occupied, sides[i])
                if neighbour and neighbour not in visited:
                        if neighbour == goal:
                            return path + [current, neighbour]
                        queue.append((neighbour, path + [current]))
                        visited.add(neighbour)
        return None

    def dfs(self, goal):
            start = self.tail[0]
            visited = {start}
            stack = deque([(start, [])])
            sides = ['left', 'right', 'up', 'down']
            while stack:
                current, path = stack.pop()
                visited.add(current)
                for i in range(4):
                    neighbour = self.find_neighbour(current, self.map.occupied, sides[i])
                    if neighbour and neighbour not in visited:
                        if neighbour == goal:
                            return path + [current, neighbour]
                        stack.append((neighbour, path + [current]))
                        visited.add(neighbour)
            return None

    def longest_path(self, goal):
        if self.tail_length == 0 or self.tail_length == 1:
            for s in ['left', 'right', 'up', 'down']:
                tail_end = self.find_neighbour(goal, self.map.occupied, s)
                if tail_end:
                    path = self.bfs(tail_end)
                    break
        else:
            self.map.occupied.remove(goal)
            path = self.bfs(goal)
        i = 0
        side = 'left'
        occupied = set(path)
        occupied = occupied.union(self.map.occupied)
        while True:
            new_node = self.find_neighbour(path[i], occupied, side)
            new_node2 = self.find_neighbour(path[i + 1], occupied, side)
            if new_node == new_node2 and new_node is not None:
                path.insert(i + 1, new_node)
                occupied.add(new_node)
                side = 'left'
            elif new_node and new_node2:
                path.insert(i + 1, new_node)
                path.insert(i + 2, new_node2)
                occupied.add(new_node)
                occupied.add(new_node2)
                side = 'left'
            else:
                if side == 'left':
                    side = 'right'
                elif side == 'right':
                    side = 'up'
                elif side == 'up':
                    side = 'down'
                else:
                    side = 'left'
                    i += 1
                if i == len(path) - 1:
                    break
        return path


class Apple:
    def __init__(self, map):
        self.position = None
        Apple.generate(self, map)

    def generate(self, map):
        x = random.randrange(0, map.width)
        y = random.randrange(0, map.height)
        while (x, y) in map.occupied:
            x = random.randrange(0, map.width)
            y = random.randrange(0, map.height)
        self.position = (x, y)

