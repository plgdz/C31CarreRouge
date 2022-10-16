import tkinter as tk
from functools import partial

class VueMenu():
    def __init__(self, root):
        # initialise la difficulte a progressive
        self.difficulte = 3
        # Assigne les template de menu a leurs frames
        self.menuDiff = self.menuNiveaux(root)
        self.menu = self.menuMain(root)
        # superpose les deux frames 
        self.menuDiff.grid(column=0, row=0)
        self.menu.grid(column=0, row=0)             

    # Methode pour afficher le menu de choix de niveau un fois le "Lancer une partie" active
    def choixNiveaux(self):
        self.menuDiff.tkraise()

    # Titre commun au deux menu
    def titre(self, frame):
        titre = tk.Label(frame, text = "Jeu du carre rouge", height=10, width=20, bg='red') # Creation du titre
        titre.place(relx=0.5, rely=0.15, anchor=tk.CENTER)                                  # placement dans le frame
        
    # Bouton Quitter commun au deux menu
    def quit(self, frame):
        quit = tk.Button(frame, text='Quitter')             # Creation du bouton
        quit.place(relx=0.5, rely=0.9, anchor=tk.CENTER)    # Placement en bas au centre du frame
        quit.config(height=2, width=8, relief = tk.GROOVE)  # Apparence du bouton
        
    def menuMain(self, root):
        menuMain = tk.Frame(root, width=700, height=700)    # Définition du frame du menu principal

        self.titre(menuMain) # Appel de la methode titre

        partie = tk.Button(menuMain, text='Lancer une partie', command=self.choixNiveaux)   # Creation du bouton
        partie.place(relx=0.5, rely=0.4, anchor = tk.CENTER)                                # Placement sur axe x et y
        partie.config(height=3, width= 15, relief=tk.GROOVE)                                # Définition de l'apparence

        score = tk.Button(menuMain, text='Tableau des scores')      # Creation du bouton
        score.place(relx=0.5, rely=0.55, anchor = tk.CENTER)        # Placement sur axe x et y
        score.config(height=3, width= 15, relief=tk.GROOVE)         # Définition de l'apparence

        self.quit(menuMain)     # Appel de l'affichage du bouton quitter

        return menuMain # Retourn le frame du menu principal

    # Methode pour definir le niveau de difficulte de la partie choisi dans le menu
    def setDiff(self, difficulte):
        self.difficulte = difficulte
        print(self.difficulte)

    # Methode pour transmettre le niveau de difficulte choisi au controlleur dans le main
    def getDiff(self):
        return self.difficulte  

    def menuNiveaux(self, root):
        menuNiveaux = tk.Frame(root, width=700, height=700) # Definition du frame

        self.titre(menuNiveaux) # Appel de la methode titre

        # Definition des boutons de choix de niveau
        facile = tk.Button(menuNiveaux, text='Facile', height=3, width=10, relief=tk.GROOVE, command=partial(self.setDiff, 0))
        moyen = tk.Button(menuNiveaux, text='Moyen', height=3, width=10, relief=tk.GROOVE, command=partial(self.setDiff, 1))
        difficile = tk.Button(menuNiveaux, text='Difficile', height=3, width=10, relief=tk.GROOVE, command=partial(self.setDiff, 2))
        progressif = tk.Button(menuNiveaux, text='Progressif', height=3, width=10, relief=tk.GROOVE, command=partial(self.setDiff, 3))
        # Placement des boutons les uns a cotes des autres
        facile.place(relx=0.1, rely=0.4)
        moyen.place(relx=0.3, rely=0.4)
        difficile.place(relx=0.5, rely=0.4)
        progressif.place(relx=0.7, rely=0.4)

        self.quit(menuNiveaux)  # Affichage du boutons quit

        return menuNiveaux  # Retourne le frame du menu de choix de niveau