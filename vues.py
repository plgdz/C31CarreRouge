from asyncio.windows_events import NULL
import csv  
import tkinter as tk
from functools import partial
from tkinter import Canvas, ttk
from tkinter.ttk import *
from c31Geometry2 import *
import threading

total = 0
        
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
        with open('fichierHighScore.csv', 'a+') as fichiercsv: 
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

class VueCarreRouge():
    def __init__(self, root) :
        self.root = root
        self.canvas = tk.Canvas(root, background='white', width= 450, height= 450)
        self.carreRouge = Carre(self.canvas, Vecteur(225, 225), 40, fill= 'red', outline= 'red', width= 1)

    def dessiner(self) :
        self.carreRouge.draw()
        self.canvas.grid()

class VueRectangles :
    def __init__(self, root, difficulte, canvas, carreRougeClicked) :
        #Initialisation des données 
        self.root = root
        self.canvas = canvas
        self.vitesse = 0 
        self.difficulte = difficulte # Difficultée choisie par l'utilisateur
        self.carreRougeClicked = carreRougeClicked # Valeur qui dicte quand les rectangles peuvent commencer à bouger

        #Choix difficultee
        if(self.difficulte == 0):
            self.vitesse = 0.2
        elif(self.difficulte == 1):
            self.vitesse = 0.4
        elif(self.difficulte == 2):
            self.vitesse = 0.6
        elif(self.difficulte == 3):
            self.vitesse = 0.2

        #Creation des rectangles, de la vitesse et de la direction initiale
        self.rectangleBleuSupDroit = Rectangle(self.canvas, Vecteur(425, 210), 60, 50, remplissage= 'blue', bordure= 'black', epaisseur= 1) 
        self.x1 = -self.vitesse
        self.y1 = self.vitesse

        self.rectangleBleuGauche = Rectangle(self.canvas, Vecteur(225, 225), 60, 60,  remplissage= 'blue', bordure= 'black', epaisseur= 1)
        self.x2 = self.vitesse + 0.01
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
        
        # Afficher les rectangles
        self.dessiner()

        # Vérification de si le carré a été cliqué avant de commencer les mouvements
        if(self.carreRougeClicked):
            self.moveRectangles()
            self.loop()
            self.loopStart()

            
    # DÉPLACEMENT DES RECTANGLES 

    def _moveRectangleBleuSupDroit(self) :
        position = self.rectangleBleuSupDroit.get_barycentre() 

        # Si la position sur l'axe X arrive à l'extrémitée de l'aire du jeu, alors changement de direction. 
        if(position.x - 31 < 125 or position.x + 31 > 575) :
            self.x1 *= -1

        # Si la position sur l'axe Y arrive à l'extrémitée de l'aire du jeu, alors changement de direction.
        elif(position.y + 26 > 575 or position.y - 26 < 125) :
            self.y1 *= -1

        # Translation du rectangle selon la direction de celui-ci
        self.rectangleBleuSupDroit.translate(Vecteur(self.x1, self.y1)) 
        
        # Afficher le rectangle dans sa nouvelle position
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

    # DÉMARRER LE MOUVEMENT DES RECTANGLES

    def moveRectangles(self) :
        self._moveRectangleBleuGauche()
        self._moveRectangleBleuInfDroit()
        self._moveRectangleBleuInfGauche()
        self._moveRectangleBleuSupDroit()

    # INTERVALLE DE TEMPS POUR AUGMENTER LA VITESSE PROGRESSIVEMENT

    def set_interval(self,func, sec):
        def func_wrapper():
            self.set_interval(func, sec)
            func()
        t = threading.Timer(sec, func_wrapper)
        t.start()
        return t

    # AUGMENTE LA VITESSE DE CHAQUE RECTANGLE EXPONENTIELLEMENT
    
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
        #affichage de la zone tu timer
        self.labelTimer()
        #Carré noir en arrière plan correspondant à la bordure du jeu 
        self.carreBackground = Carre(self.canvas, Vecteur(350, 350), 450, 0, remplissage="black", bordure="black", epaisseur=0)
        #Aire de jeu blanc où il est possible de déplacer le carré rouge 
        self.carreAireJeu = Carre(self.canvas, Vecteur(350, 350), 400, 0, remplissage="white", bordure="black", epaisseur=0)
        self.buttonLaunch = tk.Button(self.canvas, text="Start / Stop", width=12, height=1, background="Green", foreground="white", borderwidth=2, command=self.startAndStop)
        self.buttonLaunch.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
        
        self.dessiner()      
        
    def startAndStop(self) :
        if self.carreRougeClicked == False:
            self.carreRougeClicked = True
            self.buttonLaunch.config(background="red")
            self.rect = VueRectangles(self.canvas, self.difficulte, self.canvas, self.carreRougeClicked)
            self.timer()
        else :
            global total
            total = self.total
            self.canvas.grid_forget()

    def dessiner(self) :   
        self.carreBackground.draw()
        self.carreAireJeu.draw()
        self.canvas.grid(column=0, row=0)

    def setDifficulte(self, difficulte):
        self.difficulte = difficulte

    def timer(self) :
        self.min = self.sec = self.ms = self.total = 0

        if self.carreRougeClicked : # simule le déclenchement au click sur le carre rouge
            self.update()
        
    def update(self): 
        self.ms += 10
        self.total += 10
        if self.ms == 1000:
            self.sec += 1
            self.ms = 0
        if self.sec == 60:
            self.min += 1
            self.sec = 0

        # Tranforme les compteurs en string en ajustant le format pour éviter les decalages aux changement de dizaines/centaines
        minutes = f'{self.min}' if self.min > 9 else f'0{self.min}' 
        secondes = f'{self.sec}' if self.sec > 9 else f'0{self.sec}'
        milliSec = f'{self.ms}' if self.ms > 99 else f'0{self.ms}'    
        
        self.label.config(text=f'{minutes}' + ':' + f'{secondes}' + ':' + f'{milliSec}')
        self.label.after(10, self.update)   # Recursivité pour mise a jour du timer

    def labelTimer(self) :
        self.label = tk.Label(self.canvas, text = '00:00:00', height=2, width=10, bg='white', font=("Lucida Console", 19)) # Creation de l'affichage
        self.label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)  # placement dans le frame

        
class VuePartiePerdue: 

    def __init__(self, root, secondes) :
        self.root = root
        self.canvas = tk.Canvas(root, background="lightgrey", width=700, height=700)

        #Configurer le titre de la fenêtre 
        self.titre = tk.Label(root, text="Perdu")
        self.titre.config(font =("Lucida Console", 40), background="lightgrey", foreground="red")

        #Configurer affichage score du joueur  
        secondes = 5
        self.score = tk.Label(root, text="Votre score: " + str(secondes) + " secondes") 
        self.score.config(font =("Lucida Console", 15), background="lightgrey", foreground="red")

        #Configurer bouton recommencer partie 
        self.buttonRecommencer = tk.Button(root, text="Recommencer la partie", width=20, height=1, background="Black", foreground="white", borderwidth=5)
        self.buttonQuitter = tk.Button(root, text="Quitter la session", width=20, height=1, background="Black", foreground="white", borderwidth=5)


    def dessinerPartiePerdue(self, root) :
        self.canvas.pack()
        self.titre.place(anchor=tk.CENTER, relx = .5, rely = .3)
        self.score.place(anchor=tk.CENTER, relx = .48, rely = .5)
        self.buttonRecommencer.place(anchor=tk.CENTER, relx = .5, rely = 0.7)
        self.buttonQuitter.place(anchor=tk.CENTER, relx = .5, rely = 0.8)

class VueEnregistrerSession : 
    inputNom= None   # Variable globale 

    def __init__(self, root, fncEcrireScore, menuMain) :
        self.root = root
        self.canvas = tk.Canvas(root, background="lightgrey", width=700, height=700)
        self.menu = menuMain
        #Configurer le titre de la fenêtre 
        self.titre = tk.Label(self.canvas, text="Enregistrer la session?")
        self.titre.config(font =("Lucida Console", 22), background="lightgrey", foreground="red")

        #Configurer les boutons oui et non 
        self.buttonOui = tk.Button(self.canvas, text="Oui", width=12, height=1, background="Green", foreground="white", borderwidth=5,  command = lambda:[self.afficherInputNom(fncEcrireScore)])
        self.buttonNon = tk.Button(self.canvas, text="Non", width=12, height=1, background="Red", foreground="white", borderwidth=5, command=self.destroy)

        self.titre.place(anchor=tk.CENTER, relx = .5, rely = .3)
        self.buttonOui.place(anchor=tk.CENTER, relx = .4, rely = 0.5)
        self.buttonNon.place(anchor=tk.CENTER, relx = .6, rely = 0.5)

        self.canvas.grid(column=0, row=0)

    def destroy(self) :
        self.canvas.grid_forget()
        self.menu.grid(column=0, row=0)

    def afficherInputNom(self, fncEcrireScore):
        #Si le joueur appuie sur "oui", afficher option pour input du nom
        self.prenom = tk.Label(self.canvas, text="Entrez votre prénom : ")
        self.prenom.config(font =("Lucida Console", 15), background="lightgrey", foreground="red")

        self.textBox=tk.Text(self.canvas, height=1, width=20)
        self.textBox.bind('<KeyPress-Return>', partial(lambda x:[self.retrieveInput(self.textBox), fncEcrireScore(self, inputNom, total / 1000), self.destroy()])) 

        self.prenom.place(anchor=tk.CENTER, relx = .4, rely = .8)
        self.textBox.place(anchor=tk.CENTER, relx = .7, rely = .8)
        
    def retrieveInput(event, textBox):
        #Obtenir la valeur de l'entrée du nom du joueur 
        global secondes   
        global inputNom
        inputNom=textBox.get("1.0","end-1c")
      
