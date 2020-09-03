class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def change_x(self, x):
        self.x += x if (20 <= self.x + x <= 1160) else 0
