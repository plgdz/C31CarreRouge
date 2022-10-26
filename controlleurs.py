
# -*- coding: utf8 -*-
import csv
import os  
from datetime import datetime
from vues import *
import tkinter as tk
from pathlib import Path
from tempfile import NamedTemporaryFile


class JeuControler :
    def __init__(self, root, vues) :
        self.vues = VueJeu(root)

    def start(self, root) :
        self.vues.dessinerAireJeu(root)    


class RegisterSessionControler:
    def __init__(self, root, vues) :
        self.vues = VueRegisterSession(root)

    def start(self, root) :
        self.vues.dessinerRegisterSession(root)



class ClassementControler:
    def __init__(self, root, vues) :
        self.vues = VueClassement(root, self.supprimerScore)
        

    def start(self, root) :
        self.vues.dessinerClassement(root)    


    def ecrireScore(self, nom, secondes):   
        secondes = "%.2f" % secondes    #Convertir le nb de secondes (float) en 2 décimales après la virgule  
        date = datetime.today().strftime('%Y-%m-%d')        # Enregistrer la date du jour 
        with open('fichierHighScore.csv', 'a', newline="") as csv_file:  #Ouvrir le fichier en "append" pour ajouter donnée
            writer = csv.writer(csv_file, delimiter=',')              
            writer.writerows(zip([nom], [secondes], [date]))             #Écrire le nom, nb de secondes et date dans le CSV


    def ajouterAuClassement(self, nom, secondes): 
        ClassementControler.ecrireScore(self, nom, secondes) 

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
