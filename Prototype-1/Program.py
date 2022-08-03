import pygame as pg
import numpy as np
from math import sin, cos
from Rotation import *

pg.init()
screen = pg.display.set_mode((800, 800))
pg.display.set_caption("Projection")
clock = pg.time.Clock()

def center_origin(surf, p):
    return (p[0] + surf.get_width() / 2, p[1] + surf.get_height() / 2)

points = np.array([
    [-0.5, 0.5, -0.5],
    [0.5, 0.5, -0.5],
    [0.5, -0.5, -0.5],
    [-0.5, -0.5, -0.5],
    [-0.5, 0.5, 0.5],
    [0.5, 0.5, 0.5],
    [0.5, -0.5, 0.5],
    [-0.5, -0.5, 0.5]
])

distance = 2
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
edges = [
[0, 1], [1, 2], [2, 3], [3, 0],
[4, 5], [5, 6], [6, 7], [7, 4],
[0, 4], [1, 5], [2, 6], [3, 7]
]

scaleX = 400
scaleY = 400

rotationX = RotateX()
rotationY = RotateY()
rotationZ = RotateZ()
rotationX.generate_matrix(0)
rotationZ.generate_matrix(0)
rotationY.generate_matrix(0)

while running:
    clock.tick(60)
    pg.draw.rect(screen, (0, 0, 0), pg.Rect(0, 0, 800, 800))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 5:
                distance += 0.5
            elif event.button == 4:
                if distance >= 0.5:
                    distance -= 0.5
        elif event.type == pg.MOUSEMOTION:
            mouse_position = pg.mouse.get_pos()
            rotationY.generate_matrix(-mouse_position[0] / 200)
            rotationX.generate_matrix(mouse_position[1] / 200)
    for point in points:
        rotation = np.matmul(point, rotationX.matrix)
        rotation = np.matmul(rotation, rotationZ.matrix)
        rotation = np.matmul(rotation, rotationY.matrix)
        
        projection = np.matmul(rotation, project(rotation[2]))
        projected.append((projection[0], projection[1]))
    for edge in edges:
        pg.draw.line(screen, (255, 255, 255), center_origin(screen, projected[edge[0]]), center_origin(screen, projected[edge[1]]), 3)
    projected = []

    pg.display.update()
    rotation_angle += 0.01

pg.quit()
