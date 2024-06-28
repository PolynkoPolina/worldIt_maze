import pygame
import os

pygame.init()

clock = pygame.time.Clock()

exit = pygame.Rect(350,350,100,50)
m =  pygame.Rect(750,0,50,50)
gg = pygame.Rect(0,0,45,45)     
gg2 = pygame.Rect(750,750,45,45)
b = pygame.Rect(250,450,50,20)
b2 = pygame.Rect(700,250,50,20)
w_g = pygame.Rect(750,300,50,50)
w_g2 = pygame.Rect(600,300,50,50)
dp = pygame.display.set_mode((800, 800))

finish = 0
go_right1 = False
go_left1 = False
go_up1 = False
go_down1 = False

go_right2 = False
go_left2 = False
go_up2 = False
go_down2 = False

d_p = os.path.dirname(__file__)
img_p = os.path.abspath(d_p + "/textures")
#grass = 0
#wall = 1
#wall_g = 2
#wall_g2 = 3
#mouse = 4
#cat1 = 5
#cat2 = 6
#button1 = 7
#button2 = 8
wall = pygame.image.load(img_p + "/stone.png")
wall_g = pygame.image.load(img_p + "/stone_grass.png")
wall_g2 = pygame.image.load(img_p + "/stone_grass.png")
grass = pygame.image.load(img_p + "/grass.png")
cat1 = pygame.image.load(img_p + "/cat1.png")
mouse = pygame.image.load(img_p + "/mouse.png")
cat2 = pygame.image.load(img_p + "/cat2.png")
button1 = pygame.image.load(img_p + "/button1.png")
button2 = pygame.image.load(img_p+ "/button2.png")

textures = [
    [0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,1,1,0,0,0,0,0,0,0,0,1,0,0,1,0],
    [0,1,0,0,1,1,1,1,1,1,0,1,1,0,1,0],
    [0,1,0,1,1,1,0,0,0,1,0,1,0,0,1,0],
    [0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0],
    [0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,8],
    [0,1,1,1,0,0,1,1,1,1,0,1,2,1,0,3],
    [0,1,0,0,1,0,1,1,1,1,0,0,0,1,1,0],
    [0,1,1,0,1,0,1,1,1,1,1,1,1,1,0,0],
    [1,1,1,0,1,7,1,1,0,0,0,0,0,1,0,0],
    [1,0,0,0,1,1,1,1,0,1,0,1,0,1,1,0],
    [1,1,1,1,0,0,0,1,0,1,0,1,0,0,0,0],
    [1,0,0,0,0,1,0,0,0,1,0,1,1,1,1,0],
    [1,0,1,1,1,0,1,1,1,1,1,0,0,0,1,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0]
]
#-------------------------------------------------------

shrift2 = pygame.font.SysFont("Oswald Medium", 40)
shrift = pygame.font.SysFont("Oswald Medium", 50)
ex = shrift.render("Вихід", True, (186, 207, 95))
win = shrift.render("Перемога буде 15 травня", True, (186, 207, 95))

#ХАха это я Вика, я это написала ещё в 13.05.24
#Лабиринт имба
#----------------------------------------
x = 0 
y = 0 
rects = []
rects_t = []
bad = []

for texture in textures:
    for i in texture:
        s = pygame.Rect(x,y,50,50)
        rects.append(s)
        rects_t.append(i)
        if i == 1 or i == 2 or i == 3:
            bad.append(s)
        x += 50
    x = 0
    y += 50

rects_len = len(rects) #размер списка с текстурами

game = True 

cat_1_touch = False
cat_2_touch = False

while game:
    

    dp.fill((0,0,0))


#-----------------------------------------------------------------------------
    for i in range(rects_len):
        if rects_t[i] == 0 or rects_t[i] == 2 or rects_t[i] == 3 or rects_t[i]== 4 or rects_t[i] == 7 or rects_t[i] == 8:
            dp.blit(grass, rects[i])
        if rects_t[i] == 1:
            dp.blit(wall, rects[i])
#--------------------------------------------------------
    pygame.draw.rect(dp,(17, 33, 17),exit)
    dp.blit(ex,exit)
    dp.blit(button1,b)
    dp.blit(button2,b2)
    dp.blit(mouse,m)
    dp.blit(wall_g,w_g)
    dp.blit(wall_g2,w_g2)
    dp.blit(cat1,gg)
    dp.blit(cat2,gg2)
#---------------------------------------------------------------
    for i in pygame.event.get():
        if i.type == pygame.MOUSEBUTTONDOWN:
            if exit.collidepoint(i.pos):
                game = False
        if i.type == pygame.QUIT:
            game = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_w:
                 go_up1 = True
            if i.key == pygame.K_s:
                go_down1 = True
            if i.key == pygame.K_a:
                 go_left1 = True
            if i.key == pygame.K_d:
                 go_right1 = True
            if i.key == pygame.K_UP:
                 go_up2 = True
            if i.key == pygame.K_DOWN:
                 go_down2 = True
            if i.key == pygame.K_LEFT:
                 go_left2 = True
            if i.key == pygame.K_RIGHT:
                 go_right2 = True
                
            
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_w:
                 go_up1 = False
            if i.key == pygame.K_s:
                go_down1 = False
            if i.key == pygame.K_a:
                 go_left1 = False
            if i.key == pygame.K_d:
                 go_right1 = False
            if i.key == pygame.K_UP:
                 go_up2 = False
            if i.key == pygame.K_DOWN:
                 go_down2 = False
            if i.key == pygame.K_LEFT:
                 go_left2 = False
            if i.key == pygame.K_RIGHT:
                 go_right2 = False
#-----------------------------------------------------------------------
    if go_right1 == True:
        gg.x += 2
    if go_left1 == True:
        gg.x -= 2
    if go_up1 == True:
        gg.y -= 2
    if go_down1 == True:
        gg.y += 2
    
    if go_right2 == True:
        gg2.x += 2
    if go_left2 == True:
        gg2.x -= 2
    if go_up2 == True:
        gg2.y -= 2
    if go_down2 == True:
        gg2.y += 2
#---------------------------------------------------------
    if cat_1_touch == True and cat_2_touch == True:
        dp.fill((17, 33, 17))
        dp.blit(win, (200,350))
    for d in bad:
       if gg.colliderect(d) or gg2.colliderect(d):
            gg.x = 0
            gg.y = 0
            gg2.x = 750
            gg2.y = 750
    if gg.colliderect(b):
        w_g.x = 10000
        w_g.y = 10000
    if gg2.colliderect(b2):
        w_g2.x = 10000
        w_g2.y = 10000
    if gg.colliderect(m):
        cat_1_touch = True
    if gg2.colliderect(m):
        cat_2_touch = True
#------------------------------------------------
    pygame.display.flip() #обязательно в цикле
    clock.tick(60)