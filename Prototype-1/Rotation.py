import numpy as np
from math import sin, cos

class RotateX:
    def __init__(self):
        pass
    def generate_matrix(self, angle):
        self.matrix = np.array([
            [1, 0, 0],
            [0, cos(angle), -sin(angle)],
            [0, sin(angle), cos(angle)]
        ])
        return self.matrix


class RotateY:
    def __init__(self):
        pass
    def generate_matrix(self, angle):
        self.matrix = np.array([
            [cos(angle), 0, sin(angle)],
            [0, 1, 0],
            [-sin(angle), 0, cos(angle)]
        ])
        return self.matrix


class RotateZ:
    def __init__(self):
        pass
    def generate_matrix(self, angle):
        self.matrix = np.array([
            [cos(angle), -sin(angle), 0],
            [sin(angle), cos(angle), 0],
            [0, 0, 1]
        ])
        return self.matrix