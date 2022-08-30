import numpy as np
from math import sin, cos

class Box:
    def __init__(self):
        self.rotationX = np.array([
            [1, 0, 0],
            [0, cos(0), -sin(0)],
            [0, sin(0), cos(0)]
        ])
        self.rotationY = np.array([
            [cos(0), 0, sin(0)],
            [0, 1, 0],
            [-sin(0), 0, cos(0)]
        ])
        self.rotationZ = np.array([
            [cos(0), -sin(0), 0],
            [sin(0), cos(0), 0],
            [0, 0, 1]
        ])
        self.size = 1
        self.points = np.array([
            [-self.size, self.size, -self.size],
            [self.size, self.size, -self.size],
            [self.size, -self.size, -self.size],
            [-self.size, -self.size, -self.size],
            [-self.size, self.size, self.size],
            [self.size, self.size, self.size],
            [self.size, -self.size, self.size],
            [-self.size, -self.size, self.size]
        ])
        self.edges = np.array([
            [0, 1], [1, 2], [2, 3], [3, 0],
            [4, 5], [5, 6], [6, 7], [7, 4],
            [0, 4], [1, 5], [2, 6], [3, 7]
        ])
    def PushAngleX(self, angle):
        self.rotationX = np.array([
            [1, 0, 0],
            [0, cos(angle), -sin(angle)],
            [0, sin(angle), cos(angle)]
        ])
    
    def PushAngleY(self, angle):
        self.rotationY = np.array([
            [cos(angle), 0, sin(angle)],
            [0, 1, 0],
            [-sin(angle), 0, cos(angle)]
        ])
    
    def PushAngleZ(self, angle):
        self.rotationZ = np.array([
            [cos(angle), -sin(angle), 0],
            [sin(angle), cos(angle), 0],
            [0, 0, 1]
        ])
    
    def GetRotationMatrix(self):
        matrix = np.matmul(self.rotationX, self.rotationY)
        matrix = np.matmul(matrix, self.rotationZ)
        return matrix
    