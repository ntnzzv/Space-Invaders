class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = "right"

    def change_x(self, x):
        if self.direction == "right":
            self.x += x
        elif self.direction == "left":
            self.x -= x
        if self.x >= 1180:
            self.direction = "left"
            self.change_y(70)
        elif self.x <= 20:
            self.direction = "right"
            self.change_y(70)

    def change_y(self, y):
        self.y += y if (20 <= self.y + y <= 600) else 0


