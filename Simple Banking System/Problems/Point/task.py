import math


class Point:
    def __init__(self, x, y):
        self.x = abs(x)
        self.y = abs(y)

    def dist(self, p2):

        return math.sqrt(math.pow(self.x - p2.x, 2) + math.pow(self.y - p2.y, 2))