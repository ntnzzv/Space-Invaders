class Player:
    gunCooldown = 30

    def __init__(self):
        self.x = 500
        self.y = 650
        self.health = 3

    def change_x(self, x):
        self.x += x if (20 <= self.x + x <= 1160) else 0

    def set_cooldown(self):
        if self.gunCooldown >= 30:
            self.gunCooldown = 0
        elif self.gunCooldown >= 1:
            self.gunCooldown += 1

    def is_ready_to_fire(self):

        if self.gunCooldown == 0:
            self.gunCooldown += 1
            return True
        return False
