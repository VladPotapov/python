import pygame
pygame.init()
def inter(x1, y1, x2, y2, db1, db2):
    if x1 > x2-db1 and x1 < x2+db2 and y1 > y2-db1 and y1 < y2+db2:
        return 1
    else:
        return 0

window = pygame.display.set_mode((650, 406))

screen = pygame.Surface((650, 406))
img_screen = pygame.image.load('screen.jpg')

player = pygame.Surface((40, 40))
x_player = 325
y_player = 360
img_player = pygame.image.load('shooter.png')
player.set_colorkey((0, 0, 0))

zet = pygame.Surface((40, 40))
x_zet = 0
y_zet = 0
img_zet = pygame.image.load('target.png')
zet.set_colorkey((0, 0, 0))

arrow = pygame.Surface((8, 40))
x_arrow = 1000
y_arrow = 1000
img_arrow = pygame.image.load('arrow.png')
arrow.set_colorkey((0, 0, 0))

count = 0

speed = 1

pygame.font.init()
myfont = pygame.font.SysFont('arial', 15)
pygame.font.Font('C:/Windows/Fonts/ARIALN.TTF', 15)

strike = False

right = True

done = False

while done == False:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = True
        #движение вправо
        if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
            x_player += 5
            if x_player >= 615:
                x_player = 615
        #движение влево
        if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
            x_player -= 5
            if x_player <= 0:
                x_player = 0
        if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
            if strike == False:
                strike = True
                x_arrow = x_player
                y_arrow = y_player - 40

    if strike:
        y_arrow -= speed

        if y_arrow < 0:
            strike = False
            x_arrow = 1000
            y_arrow = 1000

    if inter(x_arrow, y_arrow, x_zet, y_zet, 20, 40):
        count += 1
        speed += 0.1
        strike = False
        x_arrow = 1000
        y_arrow = 1000


    if right:
        x_zet += speed
        if x_zet > 615:
            x_zet -= speed
            right = False
    else:
        x_zet -= speed
        if x_zet < 0:
            x_zet += speed
            right = True

    string = myfont.render('Очков: '+str(count), 0, (255, 0, 0))

    screen.fill((0, 255, 0))
    screen.blit(img_screen, (0, 0))
    arrow.blit(img_arrow, (0, 0))
    player.blit(img_player, (0, 0))
    zet.blit(img_zet, (0, 0))
    screen.blit(string, (0, 50))
    screen.blit(arrow, (x_arrow, y_arrow))
    screen.blit(zet, (x_zet, y_zet))
    screen.blit(player, (x_player, y_player))
    window.blit(screen, (0, 0))
    pygame.display.update()

pygame.quit()