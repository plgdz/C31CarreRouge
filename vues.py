from asyncio.windows_events import NULL
import csv  
import tkinter as tk
from functools import partial
from tkinter import Canvas, ttk
from tkinter.ttk import *
from c31Geometry2 import *


class VueMenu() :
    def __init__(self, root, classement):
        # initialise la difficulte a progressive
        
        # Assigne les template de menu a leurs frames
        
        self.menuClassement = classement
        self.retour(self.menuClassement)
        self.menuDiff = self.menuNiveaux(root)
        self.menu = self.menuMain(root) 

        self.menu.grid(column=0, row=0)
        self.menuDiff.grid(column=0, row=0)
        self.menuClassement.grid(column=0, row=0)
          
    # Titre commun au deux menu
    def titre(self, frame):
        titre = tk.Label(frame, text = "Jeu du carre rouge", height=10, width=20, bg='red') # Creation du titre
        titre.place(relx=0.5, rely=0.15, anchor=tk.CENTER)  # placement dans le frame

    # Bouton Quitter commun au deux menu
    def quit(self, frame, root):
        quit = tk.Button(frame, text='Quitter', command=root.quit)             # Creation du bouton
        quit.place(relx=0.5, rely=0.9, anchor=tk.CENTER)    # Placement en bas au centre du frame
        quit.config(height=2, width=8, relief = tk.GROOVE)  # Apparence du bouton

    def retour(self, frame):
        retour = tk.Button(frame, text='Retour', command=partial(self.retourMain, frame))             # Creation du bouton
        retour.place(relx=0.1, rely=0.1, anchor=tk.CENTER)    # Placement en bas au centre du frame
        retour.config(height=2, width=8, relief = tk.GROOVE)  # Apparence du bouton

    def retourMain(self, frame):
        frame.grid_forget() # Permet de masquer le frame pour revenir au menu principal

    def menuNiveaux(self, root):
        menuNiveaux = tk.Frame(root, width=700, height=700) # Definition du frame

        self.titre(menuNiveaux) # Appel de la methode titre

        # Definition des boutons de choix de niveau
        facile = tk.Button(menuNiveaux, text='Facile', height=3, width=10, relief=tk.GROOVE, command=partial(self.setDiff,root, 0))
        moyen = tk.Button(menuNiveaux, text='Moyen', height=3, width=10, relief=tk.GROOVE, command=partial(self.setDiff,root, 1))
        difficile = tk.Button(menuNiveaux, text='Difficile', height=3, width=10, relief=tk.GROOVE, command=partial(self.setDiff, root, 2))
        progressif = tk.Button(menuNiveaux, text='Progressif', height=3, width=10, relief=tk.GROOVE, command=partial(self.setDiff, root, 3))
        # Placement des boutons les uns a cotes des autres
        facile.place(relx=0.1, rely=0.4)
        moyen.place(relx=0.3, rely=0.4)
        difficile.place(relx=0.5, rely=0.4)
        progressif.place(relx=0.7, rely=0.4)
        self.retour(menuNiveaux)
        self.quit(menuNiveaux, root)  # Affichage du boutons quit

        return menuNiveaux  # Retourne le frame du menu de choix de niveau
    
    # Methode pour afficher le menu de choix de niveau un fois le "Lancer une partie" active
    def choixNiveaux(self):
        self.menuDiff.grid(column=0, row=0) # Replace le frame menu de niveau dans root
        self.menuDiff.tkraise()             # Pousse le frame menu niveau au premier plan

    def showClassement(self):
        self.menuClassement.grid(column=0, row=0)   # Replace le frame classement dans root
        self.menuClassement.tkraise()               # Pousse le frame classement au premier plan
    
    def menuMain(self, root):
        menuMain = tk.Frame(root, width=700, height=700)    # Définition du frame du menu principal

        self.titre(menuMain) # Appel de la methode titre

        partie = tk.Button(menuMain, text='Lancer une partie', command=self.choixNiveaux)   # Creation du bouton
        partie.place(relx=0.5, rely=0.4, anchor = tk.CENTER)                                # Placement sur axe x et y
        partie.config(height=3, width= 15, relief=tk.GROOVE)                                # Définition de l'apparence

        score = tk.Button(menuMain, text='Tableau des scores', command=self.showClassement)      # Creation du bouton
        score.place(relx=0.5, rely=0.55, anchor = tk.CENTER)        # Placement sur axe x et y
        score.config(height=3, width= 15, relief=tk.GROOVE)         # Définition de l'apparence

        self.quit(menuMain, root)     # Appel de l'affichage du bouton quitter

        return menuMain # Retourn le frame du menu principal

    # Methode pour definir le niveau de difficulte de la partie choisi dans le menu
    def setDiff(self, root, difficulte):
        self.jeu = VueJeu(root, difficulte)

    # Methode pour transmettre le niveau de difficulte choisi au controlleur dans le main
    def getDiff(self):
        return self.difficulte  

    def __getMenuMain__(self) :
        return self.menu

    def __getMenuDiff__(self) :
        return self.menuDiff
        
class VueClassement :   
    index = None   # Variable globale 

    def __init__(self, root, fncSupprimerScore):
        self.root = root 
        self.canvas = tk.Frame(root, background="lightgrey", width=700, height=700)
        
        #Afficher le titre du classement 
        titre = tk.Label(self.canvas, text="Tableau des scores")
        titre.config(font =("Lucida Console", 35), background="lightgrey", foreground="red")
        titre.place(anchor=tk.CENTER, relx = .5, rely = .2)
        
        #Ajouter un frame parent pour contenir les widgets Treeview et Scrollbar
        frParent = tk.Frame(self.canvas,  bd=5, relief=tk.SUNKEN)
        frParent.place(anchor=tk.CENTER, relx = .5, rely = .5)

        #Ajouter un widget Treeview 
        colonnes = ('rang', 'nom', 'secondes', 'date')
        tree = ttk.Treeview(frParent, columns=colonnes, show='headings')
        
        #Configurer le style du widget Treeview 
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('Treeview.Heading', background="red", foreground="white")
        s.configure('Treeview', background="black", fieldbackground="black", foreground="white", font =("Lucida Console", 10))

        #Configurer la disposition et le texte des colonnes de Treeview 
        tree.heading('rang', text='Rang')
        tree.column("rang",minwidth=0,width=120, anchor="center")
        
        tree.heading('nom', text='Nom')
        tree.column("nom",minwidth=0,width=120, anchor="center")
        
        tree.heading('secondes', text='Secondes')
        tree.column("secondes",minwidth=0,width=120, anchor="center")

        tree.heading('date', text='Date')
        tree.column("date",minwidth=0,width=120, anchor="center")
        
        #Afficher le widget Treeview 
        tree.grid(row=0, column=0, sticky=tk.NSEW)

        #Ajouter un scrollbar sur la droite du Treeview 
        scrollbar = ttk.Scrollbar(frParent, orient=tk.VERTICAL, command=tree.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')
        tree.configure(yscroll=scrollbar.set)
        
        self.afficherDonnees(tree)
    
        #Configurer un boutton supprimer 
        tree.bind('<ButtonRelease-1>', partial(self.getRow, tree)) 
        self.deleteButton = tk.Button(self.canvas, text="Supprimer", width=15, background="red", foreground="white", borderwidth=5, command = lambda:[fncSupprimerScore(index), self.afficherDonnees(tree)])
        self.deleteButton.place(anchor=tk.CENTER, relx = .5, rely = 0.8)


    def afficherDonnees(self, tree): 
        #Afficher les données du CSV dans le widget Treeview
        tree.delete(*tree.get_children()) #Si données déjà présentes dans TreeView, les supprimer pour un refresh 
        with open('fichierHighScore.csv') as fichiercsv: 
            i = 0 
            reader = csv.reader(fichiercsv)
            for row in reader:
                i += 1
                nom = row[0]
                secondes = row[1]
                date = row[2]
                tree.insert('', 'end', values=(i, nom, secondes, date))


    def getRow(event, tree, self):  
        global index
        index = (tree.index(tree.selection())) 

class VueRectangles :
    def __init__(self, root, difficulte, canvas, carreRougeClicked) :
        #Creation du canvas 
        self.root = root
        self.canvas = canvas
        self.vitesse = 0
        self.difficulte = difficulte
        self.carreRougeClicked = carreRougeClicked

        #Choix difficultee
        if(self.difficulte == 0):
            self.vitesse = 1
        elif(self.difficulte == 1):
            self.vitesse = 3
        elif(self.difficulte == 2):
            self.vitesse = 5
        elif(self.difficulte == 3):
            self.vitesse = 1

        #Creation des rectangles, de la vitesse et de la direction initiale
        self.rectangleBleuSupDroit = Rectangle(self.canvas, Vecteur(425, 210), 60, 50, remplissage= 'blue', bordure= 'black', epaisseur= 1) 
        self.x1 = -self.vitesse
        self.y1 = self.vitesse

        self.rectangleBleuGauche = Rectangle(self.canvas, Vecteur(225, 225), 60, 60,  remplissage= 'blue', bordure= 'black', epaisseur= 1)
        self.x2 = self.vitesse + 0.25
        self.y2 = self.vitesse
        
        self.rectangleBleuInfDroit = Rectangle(self.canvas, Vecteur(480, 465), 100, 20, remplissage= 'blue', bordure= 'black', epaisseur= 1)
        self.x3 = -self.vitesse
        self.y3 = -self.vitesse

        self.rectangleBleuInfGauche = Rectangle(self.canvas, Vecteur(210, 475), 30, 60, remplissage= 'blue', bordure= 'black', epaisseur= 1) 
        self.x4 = self.vitesse
        self.y4 = -self.vitesse

        # Augmentation de la vitesse a chaque 5 seconde en mode progressif
        if(self.difficulte == 3):
            self.set_interval(self.addSpeed, 5)

        self.dessiner()

        if(self.carreRougeClicked):
            self.moveRectangles()
            self.loop()
            self.loopStart()

            
    # DÉPLACEMENT DES RECTANGLES 

    def _moveRectangleBleuSupDroit(self) :
        position = self.rectangleBleuSupDroit.get_barycentre() 

        if(position.x - 31 < 125 or position.x + 31 > 575) :
            self.x1 *= -1

        elif(position.y + 26 > 575 or position.y - 26 < 125) :
            self.y1 *= -1

        self.rectangleBleuSupDroit.translate(Vecteur(self.x1, self.y1)) 
        self.rectangleBleuSupDroit.draw()


    def _moveRectangleBleuGauche(self) :
        position = self.rectangleBleuGauche.get_barycentre()

        if(position.x + 31 > 575 or position.x - 31 < 125) :
            self.x2 *= -1

        elif(position.y + 31 > 575 or position.y - 31 < 125) :
            self.y2 *= -1

        self.rectangleBleuGauche.translate(Vecteur(self.x2, self.y2))
        self.rectangleBleuGauche.draw()


    def _moveRectangleBleuInfDroit(self) :
        position = self.rectangleBleuInfDroit.get_barycentre()

        if(position.y + 11 > 575 or position.y - 11 < 125) :
            self.y3 *= -1

        elif(position.x - 51 < 125 or position.x + 51 > 575) :
            self.x3 *= -1

        self.rectangleBleuInfDroit.translate(Vecteur(self.x3, self.y3))
        self.rectangleBleuInfDroit.draw()


    def _moveRectangleBleuInfGauche(self) :
        position = self.rectangleBleuInfGauche.get_barycentre()

        if(position.x + 16 > 575 or position.x - 16 < 125) :
            self.x4 *= -1

        elif(position.y + 31 > 575 or position.y - 31 < 125) :
            self.y4 *= -1

        self.rectangleBleuInfGauche.translate(Vecteur(self.x4,self.y4))            
        self.rectangleBleuInfGauche.draw()

    # DÉFINITION DES LOOP

    def loop(self) :
        self.loop1 = LoopEvent(self.canvas, partial(self._moveRectangleBleuGauche), timesleep= 1)
        self.loop2 = LoopEvent(self.canvas, partial(self._moveRectangleBleuInfDroit), timesleep= 1) 
        self.loop3 = LoopEvent(self.canvas, partial(self._moveRectangleBleuInfGauche), timesleep= 1) 
        self.loop4 = LoopEvent(self.canvas, partial(self._moveRectangleBleuSupDroit), timesleep= 1) 

    # PARTIR LES LOOP

    def loopStart(self):
        self.loop1.startImmediately()
        self.loop2.startImmediately()
        self.loop3.startImmediately()
        self.loop4.startImmediately()

    # DESSINER TOUT LES RECTANGLES ET AFFICHER LE CANEVAS AU DÉBUT

    def dessiner(self) : 
        self.rectangleBleuGauche.draw()
        self.rectangleBleuSupDroit.draw()
        self.rectangleBleuInfGauche.draw()
        self.rectangleBleuInfDroit.draw()
        self.canvas.grid()

    # MOUVEMENT DES RECTANGLES

    def moveRectangles(self) :
        self._moveRectangleBleuGauche()
        self._moveRectangleBleuInfDroit()
        self._moveRectangleBleuInfGauche()
        self._moveRectangleBleuSupDroit()

    # PROGRESSIF

    def set_interval(self,func, sec):
        def func_wrapper():
            self.set_interval(func, sec)
            func()
        t = threading.Timer(sec, func_wrapper)
        t.start()
        return t

    def addSpeed(self):
        self.x1 *= 1.25
        self.y1 *= 1.25
        self.x2 *= 1.25
        self.y2 *= 1.25
        self.x3 *= 1.25
        self.y3 *= 1.25
        self.x4 *= 1.25
        self.y4 *= 1.25

class VueJeu :
    def __init__(self, root, difficulte) :
        self.root = root
        self.difficulte = difficulte
        self.carreRougeClicked = False
        self.canvas = tk.Canvas(root, background="lightgrey", width=700, height=700)
        #Carré noir en arrière plan correspondant à la bordure du jeu 
        self.carreBackground = Carre(self.canvas, Vecteur(350, 350), 450, 0, remplissage="black", bordure="black", epaisseur=0)
        #Aire de jeu blanc où il est possible de déplacer le carré rouge 
        self.carreAireJeu = Carre(self.canvas, Vecteur(350, 350), 400, 0, remplissage="white", bordure="black", epaisseur=0)

        self.dessiner()

        while(self.carreRougeClicked == False):
            self.carreRougeClicked = True # Donnee retournee du controlleur du carre
            self.rect = VueRectangles(root, self.difficulte, self.canvas, self.carreRougeClicked)

        self.dessiner()
        
    def dessiner(self) :   
        self.carreBackground.draw()
        self.carreAireJeu.draw()
        self.canvas.grid(column=0, row=0)

    def setDifficulte(self, difficulte):
        self.difficulte = difficulte
