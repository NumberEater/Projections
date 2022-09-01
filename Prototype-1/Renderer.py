import pygame as pg
import numpy as np
import random


# Handles drawing and does projection math
class Renderer:
    def __init__(self, screen, initialObjects: list, distance=20):
        if initialObjects:
            self.objects = initialObjects
            self.screen = screen
            self.projected = []
            self.distance = distance
    
    def AddObject(self, object):
        self.objects.append(object)

    def RemoveObject(self, object):
        self.objects.remove(object)
    
    def RemoveObject(self, index):
        self.objects.pop(index)
    
    def center_origin(self, screen_size, p):
        return (p[0] + screen_size[0] / 2, p[1] + screen_size[1] / 2)
    
    def project(self, z):
        z = 400 / (self.distance - z)
        projection_matrix = np.array([
            [z, 0, 0],
            [0, z, 0],
            [0, 0, 0]
        ])
        return projection_matrix
    
    def RenderFrame(self):
        for object in self.objects:
            for point in object.points:
                rotation = np.matmul(point, object.GetRotationMatrix())
                projection = np.matmul(rotation, self.project(rotation[2]))
                self.projected.append((projection[0], projection[1]))
            for edge in object.edges:
                pg.draw.line(self.screen, (255, 255, 255), self.center_origin((self.screen.get_width(), self.screen.get_height()), self.projected[edge[0]]), self.center_origin((self.screen.get_width(), self.screen.get_height()), self.projected[edge[1]]), 2)
            self.projected = []