import pygame
import math
from Enemy import Enemy
from Bullet import Bullet
from Player import Player

clock = pygame.time.Clock()
# enums
SCREEN_WIDTH = 1240
SCREEN_HEIGHT = 720
# initializing game
pygame.init()
pygame.key.set_repeat(1, 10)
# creating screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
# Assets loading
playerIMG = pygame.image.load('assets/player.png')
enemyIMG = pygame.image.load('assets/enemy.png')
ammoIMG = pygame.image.load('assets/ammo.png')
background = pygame.image.load('assets/background.jpg')
icon = pygame.image.load('assets/windowicon.png')

# Setting title and icon
pygame.display.set_caption("Space-Invaders")
pygame.display.set_icon(icon)
font = pygame.font.Font("freesansbold.ttf", 32)
score = 0


def show_score():
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))


def set_entity_position(image, x, y):
    screen.blit(image, (x, y))


def collision(x1, x2, y1, y2):
    return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)) < 50


def spawn_enemies():
    for i in range(10):
        enemies.append(Enemy(100 + i * 100, 100))


def spawn_boss():
    enemies.append(Enemy(600, 200))


# entities initialization
player = Player(480, 500)
bullet = Bullet(player.x, player.y)
enemies = []
spawn_enemies()

# the main game loop
while running:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.change_x(-4)
            if event.key == pygame.K_RIGHT:
                player.change_x(4)
            if event.key == pygame.K_SPACE:
                bullet.set_ready(False)
                bullet.x = player.x + 16
                bullet.y = player.y + 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.change_x(0)
#   # bullet and collision handling
    if not bullet.ready:
        bullet.set_travel_distance(10)
        for enemy in enemies:
            collided = collision(enemy.x, bullet.x, enemy.y, bullet.y)
            if collided:
                bullet.set_ready(True)
                enemies.remove(enemy)
                score += 1
        set_entity_position(ammoIMG, bullet.x, bullet.y)
    # set enemy position and update
    for enemy in enemies:
        enemy.change_x(2)
        set_entity_position(enemyIMG, enemy.x, enemy.y)

    set_entity_position(playerIMG, player.x, player.y)
    show_score()

    # check if boss should be spawned
    if len(enemies) == 0:
        enemyIMG = pygame.image.load('assets/boss.png')
        spawn_boss()
    pygame.display.update()
