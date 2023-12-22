import pygame
import os
import sys
import random

pygame.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
WIDTH = 1200
HEIGHT = 800
FPS = 60
sc = pygame.display.set_mode((WIDTH, HEIGHT))
from load import *

clock = pygame.time.Clock()

camera_group = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = image[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 5
        self.velocity_y = 0
        self.on_ground = True
        self.frame = 0
        self.timer_anime = 0
        self.anime = False

    def animation(self):
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.1:
                if self.frame == len(player_image) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0

    def update(self):
        self.animation()
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            self.rect.x += self.speed
            self.anime = True
            self.image = player_image[self.frame]
            if self.rect.right > 1000:
                self.rect.right = 1000
                camera_group.update(-self.speed)
        elif key[pygame.K_a]:
            self.rect.x -= self.speed
            self.image = pygame.transform.flip(player_image[self.frame], True, False)
            self.anime = True
            if self.rect.left < 200:
                self.rect.left = 200
                camera_group.update(+self.speed)
        else:
            self.anime = False

        if key[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = -15
            self.on_ground = False
        self.rect.y += self.velocity_y
        self.velocity_y += 1
        if self.velocity_y > 10:
            self.velocity_y = 10


class Earth(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step
        if pygame.sprite.spritecollide(self, player_group, False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
            elif abs(self.rect.bottom - player.rect.top) < 15:
                player.rect.top = self.rect.bottom + 5
                player.velocity_y = 0
            elif (abs(self.rect.left - player.rect.right) < 15
                  and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.right = self.rect.left
            elif (abs(self.rect.right - player.rect.right) < 15
                  and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.left = self.rect.right


class Water(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step


class Box(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step
        if pygame.sprite.spritecollide(self, player_group, False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
            elif abs(self.rect.bottom - player.rect.top) < 15:
                player.rect.top = self.rect.bottom + 5
                player.velocity_y = 0
            if (abs(self.rect.left - player.rect.right) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.right = self.rect.left
            elif (abs(self.rect.right - player.rect.left) < 15
                  and abs(self.rect.centery - player.rect.centery) < 50):

                player.rect.left = self.rect.right


class Center(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step
        if pygame.sprite.spritecollide(self, player_group, False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
            elif abs(self.rect.bottom - player.rect.top) < 15:
                player.rect.top = self.rect.bottom + 5
                player.velocity_y = 0
            if (abs(self.rect.left - player.rect.right) < 15
                  and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.right = self.rect.left
            elif (abs(self.rect.right - player.rect.left) < 15
                  and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.left = self.rect.right


class Portal(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = portal_image[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.timer_anime = 0
        self.anime = True

    def animation(self):
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.1:
                if self.frame == len(portal_image) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0

    def update(self, step):
        self.rect.x += step


class Monetka(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.timer_anime = 0
        self.aneme = False

    def update(self, step):
        self.rect.x += step


class StopEnemy(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step


def restart():
    global player_group, earth_group, water_group, box_group, center_group, portal_group, monetka_group, stopenemy_group, enemy_group, player

    player_group = pygame.sprite.Group()
    earth_group = pygame.sprite.Group()
    water_group = pygame.sprite.Group()
    box_group = pygame.sprite.Group()
    center_group = pygame.sprite.Group()
    portal_group = pygame.sprite.Group()
    monetka_group = pygame.sprite.Group()
    stopenemy_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()

    player = Player(player_image, (330, 500))
    player_group.add(player)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 1
        self.dir = 1
        self.frame = 0
        self.timer_anime = 0
        self.aneme = False

    def update(self, step):
        self.rect.x += step
        if self.dir == 1:
            self.rect.x += self.speed
        elif self.dir == -1:
            self.rect.x -= self.speed
        if pygame.sprite.spritecollide(self, stopenemy_group, False):
            self.dir *= -1


def drawMaps(nameFile):
    maps = []
    source = 'game_lvl/' + str(nameFile)
    with open(source, "r") as file:
        for i in range(0, 10):
            maps.append(file.readline().replace("\n", "").split(",")[0:-1])
            pos = [0, 0]
            for i in range(0, len(maps)):
                pos[1] = i * 80
                for j in range(0, len(maps[0])):
                    pos[0] = 80 * j
                    if maps[i][j] == "1":
                        center = Center(center_image, pos)
                        center_group.add(center)
                        camera_group.add(center)
                    elif maps[i][j] == "2":
                        box = Box(box_image, pos)
                        box_group.add(box)
                        camera_group.add(box)
                    elif maps[i][j] == "3":
                        earth = Earth(earth_image, pos)
                        earth_group.add(earth)
                        camera_group.add(earth)
                    elif maps[i][j] == "4":
                        water = Water(water_image, pos)
                        water_group.add(water)
                        camera_group.add(water)
                    elif maps[i][j] == "5":
                        stopenemy = StopEnemy(stop_image, pos)
                        stopenemy_group.add(stopenemy)
                        camera_group.add(stopenemy)
                    elif maps[i][j] == "6":
                        monetka = Monetka(item_image, pos)
                        monetka_group.add(monetka)
                        camera_group.add(monetka)
                    elif maps[i][j] == "7":
                        enemy = Enemy(enemy_1_image, pos)
                        monetka_group.add(enemy)
                        camera_group.add(enemy)
                    elif maps[i][j] == "8":
                        enemy = Enemy(enemy_2_image, pos)
                        monetka_group.add(enemy)
                        camera_group.add(enemy)
                    elif maps[i][j] == "9":
                        enemy = Enemy(enemy_3_image, pos)
                        monetka_group.add(enemy)
                        camera_group.add(enemy)
                    elif maps[i][j] == "10":
                        enemy = Enemy(enemy_4_image, pos)
                        monetka_group.add(enemy)
                        camera_group.add(enemy)
                    elif maps[i][j] == "11":
                        portal = Portal(portal_image, pos)
                        portal_group.add(portal)
                        camera_group.add(portal)


def game_lvl():
    sc.fill('black')
    player_group.draw(sc)
    player_group.update()
    earth_group.draw(sc)
    earth_group.update(0)
    water_group.draw(sc)
    water_group.update(0)
    box_group.draw(sc)
    box_group.update(0)
    center_group.update(0)
    center_group.draw(sc)
    portal_group.update(0)
    portal_group.draw(sc)
    monetka_group.update(0)
    monetka_group.draw(sc)
    stopenemy_group.update(0)
    enemy_group.update(0)
    enemy_group.draw(sc)

    pygame.display.update()


restart()
drawMaps('1.txt')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game_lvl()
    clock.tick(FPS)
