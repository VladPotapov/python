#добавить звуки 
# ммм после 10 очков 
# ооо после 20 
# после 30 очков включать звук ай ой во время поподания 
# после 50 очков скорость утки должна меняться 
# ускоряться и замедляться 
# после 70 очков утка должна летать волной 
# при 100 очках появляется количество жизней 
# которые сокращаются когда утка гадит на стрелка
# анимировать утку чтоб махала клыльями 
# и разворачивалась


import pygame, time
pygame.init()

pygame.mixer.music.load("seraja.mp3")
pygame.mixer.music.play()


def inter(x1, y1, x2, y2, db1, db2):
    if x1 > x2-db1 and x1 < x2+db2 and y1 > y2-db1 and y1 < y2+db2:
        return 1
    else:
        return 0

window = pygame.display.set_mode((650, 406))

#фон
screen = pygame.Surface((650, 406))
img_screen = pygame.image.load('screen.jpg')

#лук
player = pygame.Surface((40, 40))
x_player = 325
y_player = 360
img_player = pygame.image.load('shooter.png')
player.set_colorkey((0, 0, 0))

#утка
zet = pygame.Surface((40, 40))
x_zet = 0
y_zet = 0
img_zet = pygame.image.load('target.png')
zet.set_colorkey((0, 0, 0))

#стрела
arrow = pygame.Surface((8, 40))
x_arrow = 1000
y_arrow = 1000
img_arrow = pygame.image.load('arrow.png')
arrow.set_colorkey((0, 0, 0))

count = 0
#speed = 1
speed_arrow, speed_zet = 2, 3

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
        y_arrow -= speed_arrow

        if y_arrow < 0:
            strike = False
            x_arrow = 1000
            y_arrow = 1000

    if inter(x_arrow, y_arrow, x_zet, y_zet, 20, 40):
        count += 1
        #speed += 0.1
        speed_arrow += 0.2
        speed_zet += 0.5
        strike = False
        x_arrow = 1000
        y_arrow = 1000


    if right:
        #x_zet += speed
        x_zet += speed_zet
        if x_zet > 610:
            x_zet -= speed_zet
            right = False
    else:
        x_zet -= speed_zet
        if x_zet < 0:
            x_zet += speed_zet
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