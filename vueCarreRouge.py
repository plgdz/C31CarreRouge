import tkinter as tk
from c31Geometry2 import *

class VueCarreRouge():
    def __init__(self, root) :
        self.root = root
        self.canvas = tk.Canvas(root, background='white')
        self.carreRouge = Carre(self.canvas, Vecteur(225, 225), 50, remplissage= 'red', bordure= 'black', epaisseur= 1)

    def dessiner(self) :
        self.carreRouge.draw()
