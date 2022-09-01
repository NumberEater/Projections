import pygame as pg
from Shapes.Box import *
from os import system
from Renderer import *
from Shapes.Pyramid import *

class ExampleProgram:
    def RunExample(self):
        # Pygame stuff
        pg.init()
        screen = pg.display.set_mode((640, 480), vsync=1)
        pg.display.set_caption("Projection")
        clock = pg.time.Clock()
        running = True
        box1 = Box(Vector3(1.0, 1.0, 1.0))
        pyramid = Pyramid(Vector3(1, 1, 1))

        renderer = Renderer(screen, [pyramid], distance=5)

        while running:
            screen.fill((70, 80, 100))  # Clears the screen
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.MOUSEMOTION:
                    pyramid.PushAngleY(-(pg.mouse.get_pos()[0] / (screen.get_width() / 360)))  # Move the pyramid with the mouse
                    
            renderer.RenderFrame()  # Tell renderer to render stuff
            pg.display.update()  # Update the screen

        pg.quit()

program = ExampleProgram()
program.RunExample()