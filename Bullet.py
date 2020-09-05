
class Bullet:
    def __init__(self,x,y):
        self.x = x + 16
        self.y = y - 10
        self.ready = True

    def set_ready(self, boolean):
        self.ready = boolean

    def set_travel_distance(self, bullet_travel):
        self.y -= bullet_travel

