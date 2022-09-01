from RenderableObject import *
import numpy as np

# Pyramid with 5 verticies and 8 edges
class Pyramid(RenderableObject):
    def __init__(self, size):
        super().__init__(size)
        self.points = np.array([
            [-self.width, self.height, -self.length],
            [self.width, self.height, -self.length],
            [self.width, self.height, self.length],
            [-self.width, self.height, self.length],
            [0, -self.height, 0]
        ])
        self.edges = np.array([
            [0, 1], [1, 2], [2, 3], [3, 0],
            [0, 4], [1, 4], [2, 4], [3, 4]
        ])