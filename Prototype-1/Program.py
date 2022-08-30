import pygame as pg
import numpy as np
from math import sin, cos
from Box import *
import random
from os import system

pg.init()
screen = pg.display.set_mode((800, 800))
pg.display.set_caption("Projection")
clock = pg.time.Clock()

def center_origin(surf, p):
    return (p[0] + surf.get_width() / 2, p[1] + surf.get_height() / 2)

distance = 3
def project(rotated_z):
    z = 400 / (distance - rotated_z)
    projection_matrix = np.array([
        [z, 0, 0],
        [0, z, 0],
        [0, 0, 0]
    ])
    return projection_matrix

running = True
rotation_angle = 0.0
projected = []

scaleX = 400
scaleY = 400

box = Box()

doRotation = True

while running:
    clock.tick(60)
    screen.fill((0, 0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 5:
                distance += 0.2
            elif event.button == 4:
                if distance >= 0.2:
                    distance -= 0.2
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                doRotation = not doRotation

    if doRotation:
        box.PushAngleX(rotation_angle)
        rotation_angle += 0.01

    for point in box.points:
        rotation = np.matmul(point, box.GetRotationMatrix())
        projection = np.matmul(rotation, project(rotation[2]))
        #print(projection[0], projection[1])
        projected.append((projection[0], projection[1]))
        pg.draw.circle(screen, (255, 255, 255), center_origin(screen, (projection[0], projection[1])), 15 - distance)
    for edge in box.edges:
        pg.draw.line(screen, (255, 255, 255), center_origin(screen, projected[edge[0]]), center_origin(screen, projected[edge[1]]), 2)
    projected = []

    pg.display.update()
    
    

pg.quit()
