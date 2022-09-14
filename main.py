import sys
import pygame as pg
from pygame.locals import *

pg.init()
pg.display.set_caption('Manette')
ecran = pg.display.set_mode((500, 500), 0, 32)
clock = pg.time.Clock()

pg.joystick.init()
joysticks = [pg.joystick.Joystick(i) for i in range(pg.joystick.get_count())]

for joystick in joysticks:
    print(joystick.get_name())

joueur = pg.Rect(50, 50, 50, 50)
couleur_joueur = 0
couleurs = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
mouvement = [0, 0]

while True:

    ecran.fill((0, 0, 0))

    pg.draw.rect(ecran, couleurs[couleur_joueur], joueur)
    if abs(mouvement[0]) < 0.1:
        mouvement[0] = 0
    if abs(mouvement[1]) < 0.1:
        mouvement[1] = 0
    joueur.x += mouvement[0] * 10
    joueur.y += mouvement[1] * 10

    for event in pg.event.get():
        if event.type == JOYBUTTONDOWN:
            print(event)
            if event.button == 0:
                couleur_joueur = (couleur_joueur + 1) % len(couleurs)
        if event.type == JOYBUTTONUP:
            print(event)
        if event.type == JOYAXISMOTION:
            print(event)
            if event.axis < 2:
                mouvement[event.axis] = event.value
        if event.type == JOYHATMOTION:
            print(event)
        if event.type == JOYDEVICEADDED:
            joysticks = [pg.joystick.Joystick(i) for i in range(pg.joystick.get_count())]
            for joystick in joysticks:
                print(joystick.get_name())
        if event.type == JOYDEVICEREMOVED:
            joysticks = [pg.joystick.Joystick(i) for i in range(pg.joystick.get_count())]
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pg.quit()
                sys.exit()

    pg.display.update()
    clock.tick(60)