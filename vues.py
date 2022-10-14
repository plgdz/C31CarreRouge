import csv  
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from c31Geometry2 import *

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


class VueClassement :     # En construction  ----------------------------
    def __init__(self, root, fncSupprimerScore):
        self.root = root 
        self.canvas = tk.Canvas(root, background="lightgrey", width=700, height=700)
        
        #Afficher le titre du classement 
        titre = tk.Label(root, text="Classement")
        titre.config(font =("Lucida Console", 35), background="lightgrey", foreground="red")
        titre.place(anchor=tk.CENTER, relx = .5, rely = .2)
        
        #Ajouter un frame parent pour contenir Treeview et Scrollbar
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
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        #Afficher les données du CSV dans le widget Treeview
        with open('fichierHighScore.csv') as fichiercsv: 
            i = 0 
            reader = csv.reader(fichiercsv)
            for row in reader:
                i += 1
                nom = row[0]
                secondes = row[1]
                date = row[2]
                tree.insert('', 'end', values=(i, nom, secondes, date))


        #Afficher le boutton supprimer 
        supprimerButton = tk.Button(root, text="Supprimer", width=15, background="red", foreground="white", borderwidth=5, command=fncSupprimerScore)
        supprimerButton.place(anchor=tk.CENTER, relx = .5, rely = 0.8)
        

        #Ajouter un event listener pour le click de la souris + envoyer l'information à supprimer le score


    def dessinerClassement(self, root):
        self.canvas.grid()


        
        ''' 
        #Afficher le titre du classement 
        titre = tk.Label(root, text="Classement")
        titre.config(font =("Lucida Console", 25), background="turquoise", foreground="deeppink")
        titre.place(anchor=tk.CENTER, relx = .5, rely = .1)
        
        #Créer un frame parent pour tenir le widget ListBox et le widget Scrollbar 
        frParent = tk.Frame(root,  bd=5, relief=tk.SUNKEN)
        frParent.place(anchor=tk.CENTER, relx = .5, rely = .5)

        #Positionner le scrollbar par rapport au frame parent 
        scrollbar = tk.Scrollbar(frParent, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
      
        #Positionner la ListBox par rapport au frame parent et intégrer le scrollbar
        donnees = tk.Listbox(frParent, font='Courier 11', justify=tk.CENTER, yscrollcommand=scrollbar.set, height=25, width=58)
        donnees.pack(padx=5, pady=5)
        scrollbar.config(command=donnees.yview)
        

        #Afficher les données du CSV dans la boîte (ListBox)
        titresColonnes = ["    Nom", "Nombre de secondes", "Date"]
        rangees_format ="{:<12} {sp} {:<12} {sp} {:<12}" 
        counter = 0 
        donnees.insert(0, rangees_format.format(*titresColonnes, sp=" "*2))
        with open('fichierHighScore.csv') as fichiercsv: 
            reader = csv.reader(fichiercsv)
            for row in reader:
                counter+=1
                donnees.insert(tk.END, rangees_format.format(*row, sp=" "*2))
        
        #Afficher le boutton supprimer 
        deleteButton = tk.Button(root, text="Supprimer", width=15).place(anchor=tk.CENTER, relx = .5, rely = 0.9)
        '''
