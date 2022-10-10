# -*- coding: utf8 -*-
from controlleurs import JeuControler
import tkinter as tk

# Boucle de jeu
if __name__ == "__main__" :
    root = tk.Tk()
    root.title("Jeu du Carré Rouge")

    jeu = JeuControler(root, None)
    
    jeu.start(root)

    root.mainloop()