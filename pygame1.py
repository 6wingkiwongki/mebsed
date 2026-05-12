import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Background
Background = pygame.image.load("image.jpg")
Background = pygame.transform.scale(Background,(WIDTH, HEIGHT))

#PLAYER
Player= pygame.image.load("char.png")
Player= pygame.transform.scale(Player, (80,80))

#Enemy
Enemy = pygame.image.load("ghost.png")
Enemy = pygame.transform.scale(Enemy,(80,80))

#bullet
bullet = pygame.image.load("bulet.png")
bullet = pygame.transform.scale(bullet, (10, 50))
bullet_speed = 10

score = 0
font = pygame.font.SysFont("Arial", 30)

#Warna Background
WHITE=(0,0,0)

x=WIDTH // 2
y=HEIGHT // 2
speed= 5

clock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #gambar_ulang layar
    screen.fill(WHITE)
    screen.blit(Player, (x,y))
                
        
    #kontrol gerakan
    keys =pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x-= speed
    if keys[pygame.K_RIGHT]:
        x+= speed
    if keys[pygame.K_UP]:
        y-=speed
    if keys[pygame.K_DOWN]:
        y+=speed

    pygame.display.update()
    clock.tick(60)

    print ("Score:", score)