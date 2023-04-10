class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, speed):
        self.x += speed.x
        self.y += speed.y

    def isEqual(self, other):
        return self.x == other.x and self.y == other.y
