import pygame
from script import load_image
earth_image = pygame.image.load('image/blocks/earth.png').convert_alpha()
center_image = pygame.image.load('image/blocks/center.png').convert_alpha()
water_image = pygame.image.load('image/blocks/water.png').convert_alpha()
box_image = pygame.image.load('image/blocks/box.png').convert_alpha()
stop_image = pygame.image.load('image/blocks/stop.png')

player_image = load_image('image/player')
item_image = load_image('image/item')
portal_image = load_image('image/portal')
enemy_1_image = load_image('image/enemy/1')
enemy_2_image = load_image('image/enemy/2')
enemy_3_image = load_image('image/enemy/3')
enemy_4_image = load_image('image/enemy/4')
fireball_image = load_image('image/Fireball')
