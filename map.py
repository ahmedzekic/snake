class Map:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.occupied = set()
        self.obstacles = set()

    def add_obstacle(self, start, end, fill):
        min_x = min(start[0], end[0])
        max_x = max(start[0], end[0])
        min_y = min(start[1], end[1])
        max_y = max(start[1], end[1])

        if fill:
            for i in range(min_x, max_x + 1):
                for j in range(min_y, max_y + 1):
                    self.occupied.add((i, j))
                    self.obstacles.add((i, j))
        else:
            if min_x == max_x:
                for i in range(min_y, max_y + 1):
                    self.occupied.add((min_x, i))
                    self.obstacles.add((min_x, i))
            elif min_y == max_y:
                for i in range(min_x, max_x + 1):
                    self.occupied.add((i, min_y))
                    self.obstacles.add((i, min_y))
            else:
                if (min_x == start[0] and max_y == start[1]) or (min_x == end[0] and max_y == end[1]):
                    for i in range(min_x, max_x + 1):
                        self.occupied.add((i, max_y - i + min_x))
                        self.obstacles.add((i, max_y - i + min_x))
                else:
                    for i in range(min_x, max_x + 1):
                        self.occupied.add((i, min_y + i - min_x))
                        self.obstacles.add((i, min_y + i - min_x))
