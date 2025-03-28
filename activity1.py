import pygame
import math
import random



Screen_Width = 800
Screen_Height = 500
Player_Start_X = 370
Player_Start_Y = 380
Enemy_Start_Y_Min = 50
Enemy_Start_Y_Max = 150
Enemy_Speed_X = 4
Enemy_Speed_Y = 40
Bullet_Speed = 10
Collision_Distance = 27

pygame.init()
screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
background = pygame.image.load('background.png')

playerImg = pygame.image.load("player.png")
Player_X = Player_Start_X
Player_Y = Player_Start_Y
Player_X_Change = 0

Enemy_Img = []
Enemy_X = []
Enemy_Y = []
Enemy_X_Change = []
Enemy_Y_Change = []
Num_Enemies = 6

for i in range(Num_Enemies):
    Enemy_Img.append(pygame.image.load("enemy.png"))
    Enemy_X.append(random.randint(0, Screen_Width - 64))
    Enemy_Y.append(random.randint(Enemy_Start_Y_Min ,Enemy_Start_Y_Max))
    Enemy_Y_Change.append(Enemy_Speed_Y)
    Enemy_X_Change.append(Enemy_Speed_X)

Bullet_Img = pygame.image.load("bullet.png")
Bullet_X = 0
Bullet_Y = Player_Start_Y
Bullet_X_Change = 0
Bullet_Y_Change = Bullet_Speed
Bullet_State = "Ready"

Score_Value = 0
Font = pygame.font.Font('freesansbold.ttf', 32)
Text_Y = 10
Text_X = 10

Over_Font = pygame.font.Font('freesansbold.ttf')

def Show_Score(x, y):
    Score = Font.render("Score : " + str(Score_Value), True, (255,255,255))
    screen.blit(Score,(x, y))

def Game_Over_Text():
    Over_Text = Over_Font.render("Game Over", True, (255,255,255))
    screen.blit(Over_Text, (200,250))

def Player(x, y):
    screen.blit(playerImg, (x,y))

def Enemy(x, y, i):
    screen.blit(Enemy_Img[i], (x, y))

def Fire_Bullet(x, y):
    global Bullet_State
    Bullet_State = "Fire"
    screen.blit(Bullet_Img,(x + 16,y + 10))

def isCollistion(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt((enemyx - bulletx)** 2 + (enemyy - bullety) ** 2)
    return distance < Collision_Distance

running = True

while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            Player_X_Change = -5
        if event.key == pygame.K_RIGHT:
            Player_X_Change = 5
        if event.key == pygame.K_SPACE and Bullet_State == "Ready":
            Bullet_X = Player_X
            Fire_Bullet(Bullet_X, Bullet_Y)
    if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
        Player_X_Change = 0

Player_X += Player_X_Change
Player_X = max(0 , min(Player_X, Screen_Width - 64))

for i in range(Num_Enemies):
    if Enemy_Y[i] > 340:
        for j in range(Num_Enemies):
            Enemy_Y[j] = 2000
        Game_Over_Text()
        break

    Enemy_X[i] += Enemy_X_Change[i]
    if Enemy_X[i] <= 0 or Enemy[i] >= Screen_Width - 64:
        Enemy_X_Change[[i]] *= -1
        Enemy_Y[i] += Enemy_Y_Change[i]

    if isCollistion(Enemy_X[i], Enemy_Y[i], Bullet_X, Bullet_Y):
        Bullet_Y = Player_Start_Y
        Bullet_State = "Ready"
        Score_Value += 1
        Enemy_X[i] = random.randint(0, Screen_Width - 64)
        Enemy_Y[i] = random.randint(Enemy_Start_Y_Min, Enemy_Start_Y_Max)

    Enemy(Enemy_X[i], Enemy_Y[i], i)

if Bullet_Y <= 0:
    Bullet_Y = Player_Start_Y
    Bullet_State = "Ready"
elif Bullet_State == "Fire":
    Fire_Bullet(Bullet_X, Bullet_Y)
    Bullet_Y -= Bullet_Y_Change

Player(Player_X, Player_Y)
Show_Score(Text_X, Text_Y)
pygame.display.update()