import pygame

# initialize game
pygame.init()
pygame.key.set_repeat(1, 10)
# creating screen
screen = pygame.display.set_mode((800, 600))
running = True

# background
background = pygame.image.load('Images/background.jpg')
# Setting title and icon
pygame.display.set_caption("Space-Invaders")
icon = pygame.image.load('Images/windowicon.png')
pygame.display.set_icon(icon)


# Player
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bullet_state = "ready"
        self.bullet_position = [self.x + 16, self.y - 30]

    def change_x(self, x):
        self.x += x if (20 <= self.x + x <= 720) else 0

    def fire_bullet(self, y):
        set_entity_position(ammoIMG, self.x + 16, self.bullet_position[1] - y)
        self.bullet_state = "travelling" if self.bullet_position[1] < 100 else "ready"

# Enemy
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
        if self.x >= 720:
            self.direction = "left"
            self.change_y(20)
        elif self.x <= 20:
            self.direction = "right"
            self.change_y(20)

    def change_y(self, y):
        self.y += y if (20 <= self.y + y <= 400) else 0


playerIMG = pygame.image.load('Images/player.png')
player = Player(480, 500)
enemyIMG = pygame.image.load('Images/astronaut.png')
enemy = Enemy(370, 100)
ammoIMG = pygame.image.load('Images/ammo.png')


def set_entity_position(image, x, y):
    screen.blit(image, (x, y))


# the main game loop
while running:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.change_x(-4)
            if event.key == pygame.K_RIGHT:
                player.change_x(4)
            if event.key == pygame.K_SPACE:
                player.fire_bullet(30)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.change_x(0)
    if(player.bullet_state == "traveling"):
        player.fire_bullet(player.bullet_position + 30)
    set_entity_position(playerIMG, player.x, player.y)
    enemy.change_x(0.7)
    set_entity_position(enemyIMG, enemy.x, enemy.y)
    pygame.display.update()
    pygame.time.wait(5)
