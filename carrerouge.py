# -*- coding: utf8 -*-
from controlleurs import ClassementControler, JeuControler
import tkinter as tk
import random
from vues import VueClassement

# Boucle de jeu
if __name__ == "__main__" :
    root = tk.Tk()
    root.title("Jeu du Carré Rouge")  
    root.geometry("700x700")  
    #frameJeu = tk.Frame(root)
    #frameJeu.pack() 
    #frameClassement = tk.Frame(root)
    #frameClassement.pack()

    classement = ClassementControler(root, None)
    classement.start(root)

    #jeu = JeuControler(root, None)
    #jeu.start(root)
    
    #Générer valeurs aléatoires pour tests sur classement 
    #secondes = random.uniform(0, 400)  
    #nom = "Brian"
   
    root.mainloop()