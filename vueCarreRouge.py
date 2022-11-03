import tkinter as tk
from c31Geometry import *

class VueCarreRouge():
    def __init__(self, root) :
        self.root = root
        self.canvas = tk.Canvas(root, background='white', width= 450, height= 450)
        self.carreRouge = Carre(self.canvas, Point(225, 225), 40, fill= 'red', outline= 'red', width= 1)

    def dessiner(self) :
        self.carreRouge.draw()
        self.canvas.grid()
