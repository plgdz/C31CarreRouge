import tkinter as tk
from c31Geometry2 import *


class VueJeu():
    def __init__(self, root) :
        self.root = root
        self.canvas = tk.Canvas(root, background="lightgrey", width=700, height=700)
        #Carré noir en arrière plan correspondant à la bordure du jeu 
        self.carreBackground = Carre(self.canvas, Vecteur(350, 350), 450, 0, remplissage="black", bordure="black", epaisseur=0)
        #Aire de jeu blanc où il est possible de déplacer le carré rouge 
        self.carreAireJeu = Carre(self.canvas, Vecteur(350, 350), 400, 0, remplissage="white", bordure="black", epaisseur=0)
        
    def dessiner(self, root) :   
        self.carreBackground.draw()
        self.carreAireJeu.draw()
        self.canvas.pack()
