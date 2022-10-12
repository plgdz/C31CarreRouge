# -*- coding: utf8 -*-
from controlleurs import ClassementControler, JeuControler
import tkinter as tk
import random

from vues import VueClassement

# Boucle de jeu
if __name__ == "__main__" :
    root = tk.Tk()
    root.title("Jeu du Carré Rouge")

    
    frameJeu = tk.Frame(root)
    frameJeu.pack() 

    frameClassement = tk.Frame(root)
    frameClassement.pack()

    jeu = JeuControler(root, None)
    jeu.start(root)
    

    #Générer valeurs aléatoires pour tests sur classement 
    secondes = random.uniform(0, 400)  
    nom = "Brian"
   
    root.mainloop()