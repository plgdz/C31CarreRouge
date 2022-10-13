import csv 
import time 
import tkinter as tk
from c31Geometry2 import *
from controlleurs import *
from tkinter.scrolledtext import ScrolledText 




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
    def __init__(self, root):
        self.root = root 
        self.canvas = tk.Canvas(root, background="lightgrey", width=700, height=700)
        self.carreBackground = Carre(self.canvas, Vecteur(350, 350), 500, 0, remplissage="white", bordure="black", epaisseur=0)
      
        #Afficher le titre du classement 
        titre = tk.Label(root, text="Classement")
        titre.config(font =("Lucida Console", 25), background="lightgrey")
        titre.place(anchor=tk.CENTER, relx = .5, rely = .08)
        
        #Créer un frame parent pour tenir le widget ListBox et le widget Scrollbar 
        frParent = tk.Frame(root,  bd=2, relief=tk.RIDGE)
        frParent.place(anchor=tk.CENTER, relx = .5, rely = .5)

        #Positionner le scrollbar par rapport au frame parent 
        scrollbar = tk.Scrollbar(frParent, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        #Positionner la ListBox par rapport au frame parent 
        donnees = tk.Listbox(frParent, font=("time new roman",8), justify=tk.CENTER, yscrollcommand=scrollbar.set, height=35, width=80)
        donnees.pack()

        scrollbar.config(command=donnees.yview)

         #Afficher les données du CSV dans la boîte 
        counter = 0 
        with open('fichierHighScore.csv') as fichiercsv: 
            reader = csv.reader(fichiercsv)
            for row in reader:
                counter+=1
                donnees.insert(tk.END, row)
 


        #Afficher boîte dans laquelle sont les scores 
        #scrollbar = tk.Scrollbar(root)
        #scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        #donnees = tk.Listbox(root, height = 30, width = 80, border=5)
        #donnees.place(anchor=tk.CENTER, relx = .5, rely = .5)

       
        #donnees.configure(yscrollcommand=scrollbar.set)
        #scrollbar.configure(command=donnees.yview)
        

        #Afficher le scrollbar de la boîte 
       

       


    def dessinerClassement(self, root):
        self.carreBackground.draw()
        self.canvas.pack()
        counter = 0;  

        
        # with open('fichierHighScore.csv') as fichiercsv: 
        #    reader = csv.reader(fichiercsv)
        #    for row in reader:
        #        counter +=1
        #        print(str(counter) + ".\t" + '\t'.join(row))
        #time.sleep(5.0)
  