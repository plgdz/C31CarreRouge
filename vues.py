import csv  
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from c31Geometry2 import *


class VueRegisterSession(): 
    def __init__(self, root) :
        self.root = root
        self.canvas = tk.Canvas(root, background="lightgrey", width=700, height=700)
        enregistrer = tk.Label(root, text="Enregistrer la session?")
        enregistrer.config(font =("Lucida Console", 20), background="lightgrey", foreground="red")
        enregistrer.place(anchor=tk.CENTER, relx = .5, rely = .4)

        #tree.bind('<ButtonRelease-1>', partial(self.envoyerChoix, tree)) 
        self.buttonOui = tk.Button(root, text="Oui", width=12, height=2, background="Green", foreground="white", borderwidth=5)
        self.buttonNon = tk.Button(root, text="Non", width=12, height=2, background="Red", foreground="white", borderwidth=5)

    def dessinerRegisterSession(self, root) :
        self.canvas.pack()
        self.buttonOui.place(anchor=tk.CENTER, relx = .4, rely = 0.55)
        self.buttonNon.place(anchor=tk.CENTER, relx = .6, rely = 0.55)




class VueJeu():
    def __init__(self, root) :
        self.root = root
        self.canvas = tk.Canvas(root, background="lightgrey", width=700, height=700)
        
        #Carré noir en arrière plan correspondant à la bordure du jeu 
        self.carreBackground = Carre(self.canvas, Vecteur(350, 350), 450, 0, remplissage="black", bordure="black", epaisseur=0)
        
        #Aire de jeu blanc où il est possible de déplacer le carré rouge 
        self.carreAireJeu = Carre(self.canvas, Vecteur(350, 350), 400, 0, remplissage="white", bordure="black", epaisseur=0)
        

    def dessinerAireJeu(self, root) :   
        self.carreBackground.draw()
        self.carreAireJeu.draw()
        self.canvas.pack()


class VueClassement :   
    index = None   # Variable globale 

    def __init__(self, root, fncSupprimerScore):
        self.root = root 
        self.canvas = tk.Canvas(root, background="lightgrey", width=700, height=700)
        
        #Afficher le titre du classement 
        titre = tk.Label(root, text="Tableau des scores")
        titre.config(font =("Lucida Console", 35), background="lightgrey", foreground="red")
        titre.place(anchor=tk.CENTER, relx = .5, rely = .2)
        
        #Ajouter un frame parent pour contenir les widgets Treeview et Scrollbar
        frParent = tk.Frame(root,  bd=5, relief=tk.SUNKEN)
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
        self.deleteButton = tk.Button(root, text="Supprimer", width=15, background="red", foreground="white", borderwidth=5, command = lambda:[fncSupprimerScore(index), self.afficherDonnees(tree)])


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


    def dessinerClassement(self, root):
        self.canvas.grid()
        self.deleteButton.place(anchor=tk.CENTER, relx = .5, rely = 0.8)