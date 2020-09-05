import pygame
import math
import random
from Enemy import Enemy
from Bullet import Bullet
from Player import Player

# enums
SCREEN_WIDTH = 1240
SCREEN_HEIGHT = 720
# initializing game and globals
pygame.init()
pygame.key.set_repeat(1, 10)
clock = pygame.time.Clock()
score = 0
gameWon = False
bossLevel = False
enemyBullets = []
playerBullets = []
# creating screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
# Assets loading
playerIMG = pygame.image.load('assets/player.png')
enemyIMG = pygame.image.load('assets/enemy.png')
ammoIMG = pygame.image.load('assets/ammo.png')
background = pygame.image.load('assets/background.jpg')
icon = pygame.image.load('assets/windowicon.png')

# Setting game title,fonts and icon
pygame.display.set_caption("Space-Invaders")
pygame.display.set_icon(icon)
font = pygame.font.Font("freesansbold.ttf", 32)
title_font = pygame.font.SysFont("freesansbold.ttf", 70)


def show_score():
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))
    health = font.render("Health: " + str(player.health), True, (255, 255, 255))
    screen.blit(health, (10, 60))


def set_entity_position(image, x, y):
    screen.blit(image, (x, y))


def collision(x1, x2, y1, y2):
    return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)) < 50


def spawn_enemies():
    for i in range(10):
        enemies.append(Enemy(100 + i * 100, 100))
    for i in range(10):
        enemies.append(Enemy(100 + i * 100, 300))


def spawn_boss():
    enemies.append(Enemy(600, 200))


# entities initialization
player = Player()
bullet = Bullet(player.x, player.y)
enemies = []
spawn_enemies()

# the main game loop
while running:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    clock.tick(60)
    player.set_cooldown()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                if player.health == 0:
                    player = Player()
            if event.key == pygame.K_LEFT:
                player.change_x(-4)
            if event.key == pygame.K_RIGHT:
                player.change_x(4)
            if event.key == pygame.K_SPACE:
                if player.is_ready_to_fire():
                    playerBullets.append(Bullet(player.x, player.y))
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.change_x(0)
    if player.health > 0:
        # bullet and collision handling
        for bullet in playerBullets:
            bullet.set_travel_distance(10)
            if bullet.y <= 0:
                playerBullets.remove(bullet)

            for enemy in enemies:
                collided = collision(enemy.x, bullet.x, enemy.y, bullet.y)
                if collided:
                    enemies.remove(enemy)
                    playerBullets.remove(bullet)
                    score += 1
                    gameWon = True if bossLevel else False
            set_entity_position(ammoIMG, bullet.x, bullet.y)

        # set enemy position and update
        for enemy in enemies:
            if random.randrange(0, 320) == 1:
                enemyBullets.append(Bullet(enemy.x, enemy.y))
            enemy.change_x(2)
            set_entity_position(enemyIMG, enemy.x, enemy.y)

        for bullet in enemyBullets:
            bullet.set_travel_distance(-4)
            set_entity_position(ammoIMG, bullet.x, bullet.y)
            collided = collision(bullet.x, player.x, bullet.y, player.y)
            if collided and player.health > 0:
                player.health -= 1
                enemyBullets.remove(bullet)

        set_entity_position(playerIMG, player.x, player.y)
    show_score()

    # check if boss should be spawned
    if len(enemies) == 0 and not gameWon:
        bossLevel = True
        enemyIMG = pygame.image.load('assets/boss.png')
        spawn_boss()

    if gameWon:
        title_label = title_font.render("You Won !!!", 1, (
            255 * random.randint(0, 1), 255 * random.randint(0, 1), 255 * random.randint(0, 1)))
        screen.blit(title_label, (SCREEN_WIDTH / 2 - title_label.get_width() / 2, 350))

    if player.health == 0:
        title_label = title_font.render("You Lost ! Press TAB to keep playing", 1, (255, 255, 255))
        screen.blit(title_label, (SCREEN_WIDTH / 2 - title_label.get_width() / 2, 350))

    pygame.display.update()
