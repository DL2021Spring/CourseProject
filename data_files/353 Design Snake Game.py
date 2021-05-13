
from collections import deque

__author__ = 'Daniel'


class SnakeGame(object):
    def __init__(self, width, height, food):
        
        self.w = width
        self.h = height
        self.food = deque(food)
        self.body = deque([(0, 0)])
        self.dirs = {
            'U': (-1, 0),
            'L': (0, -1),
            'R': (0, 1),
            'D': (1, 0),
        }
        self.eat = 0

    def move(self, direction):
        
        x, y = self.body[0]
        dx, dy = self.dirs[direction]
        x += dx
        y += dy
        fx, fy = self.food[0] if self.food else (-1, -1)
        if x == fx and y == fy:
            self.food.popleft()
            self.eat += 1
        else:
            self.body.pop()
            if (x, y) in self.body or not (0 <= x < self.h and 0 <= y < self.w):
                
                return -1

        self.body.appendleft((x, y))
        return self.eat






if __name__ == "__main__":
    game = SnakeGame(3, 2, [[1, 2], [0, 1]])
    for char, expect in zip('RDRULU', [0, 0, 1, 1, 2, -1]):
        assert game.move(char) == expect
