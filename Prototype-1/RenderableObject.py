import numpy as np
from math import sin, cos, atan2
from Vector3 import *

# Renderable object is the parent class of all objects/shapes on the screen
# The default is a box with a Vector3 for size
# Making a different shape just requires a redefinition of the points and edges

class RenderableObject:
    def __init__(self, size: Vector3):

        # Define rotation matrices for xyz axis
        # TODO: This could be a Vector3
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
        
        # TODO: Rewrite this to be a tuple
        self.width = size.x
        self.height = size.y
        self.length = size.z
        # Defines the points in the shape
        self.points = np.array([
            [-self.width, self.height, -self.length],
            [self.width, self.height, -self.length],
            [self.width, -self.height, -self.length],
            [-self.width, -self.height, -self.length],
            [-self.width, self.height, self.length],
            [self.width, self.height, self.length],
            [self.width, -self.height, self.length],
            [-self.width, -self.height, self.length]
        ])
        # Defines the index of connecting verticies
        self.edges = np.array([
            [0, 1], [1, 2], [2, 3], [3, 0],
            [4, 5], [5, 6], [6, 7], [7, 4],
            [0, 4], [1, 5], [2, 6], [3, 7]
        ])

    # Set rotation on x axis in degrees
    def PushAngleX(self, angle):
        angle = np.deg2rad(angle)
        self.rotationX = np.array([
            [1, 0, 0],
            [0, cos(angle), -sin(angle)],
            [0, sin(angle), cos(angle)]
        ])
    
    # Set rotation on y axis in degrees
    def PushAngleY(self, angle):
        angle = np.deg2rad(angle)
        self.rotationY = np.array([
            [cos(angle), 0, sin(angle)],
            [0, 1, 0],
            [-sin(angle), 0, cos(angle)]
        ])
    
    # Set rotation on z axis in degrees
    def PushAngleZ(self, angle):
        angle = np.deg2rad(angle)
        self.rotationZ = np.array([
            [cos(angle), -sin(angle), 0],
            [sin(angle), cos(angle), 0],
            [0, 0, 1]
        ])
    
    # Calculate combined rotation matrix
    def GetRotationMatrix(self):
        matrix = np.matmul(self.rotationX, self.rotationY)
        matrix = np.matmul(matrix, self.rotationZ)
        return matrix
