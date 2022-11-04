from asyncio.windows_events import NULL
import csv
import os  
from datetime import datetime
from vues import VueClassement, VueJeu, VueEnregistrerSession
import tkinter as tk
from pathlib import Path
from tempfile import NamedTemporaryFile
from functools import partial


# class JeuControler :
#     def __init__(self, root, difficulte) :
#         self.vues = VueJeu(root, difficulte)   

class MenuControler :
    def __init__(self, root):  
        # Assigne les template de menu a leurs frames
        self.reg = VueEnregistrerSession(root, ClassementControler.ajouterAuClassement, self.menuMain(root))   
        self.menuClassement = ClassementControler(root).__getMenuClassement__()
        self.retour(self.menuClassement)
        self.menuDiff = self.menuNiveaux(root)
        self.menu = self.menuMain(root) 

        self.menu.grid(column=0, row=0)
                        
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
        self.menu.grid(column=0, row=0)

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
        self.menu.grid_forget()
        self.menuDiff.grid(column=0, row=0) # Replace le frame menu de niveau dans root
        self.menuDiff.tkraise()             # Pousse le frame menu niveau au premier plan

    def showClassement(self):
        self.menu.grid_forget()
        self.menuClassement.grid(column=0, row=0)   # Replace le frame classement dans root
        self.menuClassement.tkraise()              # Pousse le frame classement au premier plan

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
        self.menuDiff.grid_forget()
        self.reg.canvas.grid(column=0, row=0)
        self.jeu = VueJeu(root, difficulte)
        
             
    # Methode pour transmettre le niveau de difficulte choisi au controlleur dans le main
    def getDiff(self):
        return self.difficulte  

    def __getMenuMain__(self) :
        return self.menu

    def __getMenuDiff__(self) :
        return self.menuDiff
        
class RegisterSessionControler:
    def __init__(self, root) :
        self.vues = VueEnregistrerSession(root, ClassementControler.ajouterAuClassement)

    def getRegisterSession(self) :
        return self.vues.canvas

class ClassementControler:
    def __init__(self, root) :
        self.vues = VueClassement(root, self.supprimerScore)

    def __getMenuClassement__(self):
        return self.vues.canvas   
   
    def ajouterAuClassement(self, nom, secondes): 
        secondes = "%.2f" % secondes    #Convertir le nb de secondes (float) en 2 décimales après la virgule  
        date = datetime.today().strftime('%Y-%m-%d')        # Enregistrer la date du jour 
        with open('fichierHighScore.csv', 'a', newline="") as csv_file:  #Ouvrir le fichier en "append" pour ajouter donnée
            writer = csv.writer(csv_file, delimiter=',')              
            writer.writerows(zip([nom], [secondes], [date]))             #Écrire le nom, nb de secondes et date dans le CSV

        # Ouvrir le fichier CSV et le trier par le nombre de secondes des joueurs en ordre décroissant 
        data = csv.reader(open('fichierHighScore.csv'),delimiter=',')
        data = sorted(data, key=lambda x: float(x[1]), reverse= True) 
        
        #Écraser le contenu du CSV courant avec un contenu trié 
        sorted_csv_file = open('fichierHighScore.csv', 'w+', newline='') 
        write = csv.writer(sorted_csv_file)           
        for eachline in data:
                write.writerow(eachline)   


    def supprimerScore(self, index):
        ligneASupprimer = (index + 1) 
        ligne = 0
        filepath = Path('fichierHighScore.csv')
        with open(filepath, 'r', newline='') as csv_file, \
            NamedTemporaryFile('w', newline='', dir=filepath.parent, delete=False) as tmp_file:
            
            csv_reader = csv.reader(csv_file)
            csv_writer = csv.writer(tmp_file)

            # Copier les lignes du CSV sans copier la rangée que l'utilisateur veut supprimer 
            for row in csv_reader:
                ligne += 1 
                if ligne == ligneASupprimer:  
                    continue  
                csv_writer.writerow(row)

        # Remplacer le fichier csv existant par le nouveau avec la ligne supprimée  
        os.replace(tmp_file.name, filepath)

class ControlleurCarreRouge :

    def __init__(self):
        self.vues = VueCarreRouge(
            self.root, self.canvas, self.carreRouge
        )
    def left(self,e):
        x = -10
        y = 0
        self.vues.canvas.move(self.carreRouge, x, y)

    def right(self,e):
        x = 10
        y = 0
        self.vues.canvas.move(self.carreRouge, x, y)

    def up(self,e):
        x = 0
        y = -10
        self.vues.canvas.move(self.carreRouge, x, y)

    def down(self,e):
        x = 0
        y = 10
        self.vues.canvas.move(self.carreRouge, x, y)
