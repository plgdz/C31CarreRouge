import csv 
import time 
import tkinter as tk
from c31Geometry2 import *
from controlleurs import *



class VueJeu():
    def __init__(self, root) :
        self.root = root
        self.btn_classement = tk.Button(root, text='Classement')
        self.canvas = tk.Canvas(root, background="lightgrey", width=700, height=700)
        #Carré noir en arrière plan correspondant à la bordure du jeu 
        self.carreBackground = Carre(self.canvas, Vecteur(350, 350), 450, 0, remplissage="black", bordure="black", epaisseur=0)
        #Aire de jeu blanc où il est possible de déplacer le carré rouge 
        self.carreAireJeu = Carre(self.canvas, Vecteur(350, 350), 400, 0, remplissage="white", bordure="black", epaisseur=0)
        
    def dessinerAireJeu(self, root) :   
        self.carreBackground.draw()
        self.carreAireJeu.draw()
        self.btn_classement.pack()
        self.canvas.pack()


class VueClassement :     # En construction 
    def __init__(self, root):
        self.root = root 
        self.canvas = tk.Canvas(root, background="red", width=700, height=700)
        self.carreBackground = Carre(self.canvas, Vecteur(350, 350), 450, 0, remplissage="lightpink", bordure="black", epaisseur=0)

    def dessinerClassement(self, root):
        self.carreBackground.draw()
        self.canvas.pack()
        counter = 0;  
 
        #Afficher les données du CSV 
        with open('fichierHighScore.csv') as fichiercsv: 
            reader = csv.reader(fichiercsv)
            for row in reader:
                counter +=1
                print(str(counter) + ".\t" + '\t'.join(row))
        time.sleep(5.0)
  