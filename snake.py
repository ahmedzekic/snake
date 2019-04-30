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
        #self.end_of_game = True

    def snake_eats_apple(self, apple):
        if self.tail[0] == apple.position:
            apple.generate(self.map)
            self.tail_length += 1
        Snake.move_snake(self)

    def move_snake(self):
        temp = self.tail[0]
        for i in range(1, self.tail_length + 1):
            temp_2 = self.tail[i]
            self.tail[i] = temp
            if i == self.tail_length:
                self.map.occupied.add(temp)
            temp = temp_2

    def go(self, side):
        self.start = True
        delete = self.tail[self.tail_length]
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
        '''self.map.occupied.remove(self.tail[self.tail_length])
        self.map.occupied.add(self.tail[0])'''
        #Snake.move_snake(self)

    def end_of_game(self):
        if self.tail[0][0] < 0 or self.tail[0][0] == self.map.width:
            return True
        elif self.tail[0][1] < 0 or self.tail[0][1] == self.map.height:
            return True
        elif self.start and self.tail[0] in self.map.occupied:
            return True
        return False


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
