import tkinter as tk
from functools import partial

class VueMenu:
    def affichageTitre():
        titre = tk.Label(root, text = "Jeu du carre rouge", height=10, width=20) # Creation du titre
        titre.config(background=('red'))
        titre.place(relx=0.5, rely=0.15, anchor=tk.CENTER) #Placement du titre au centre 
        return titre

    def lancerJeu():
        partie = tk.Button(root, text='Lancer une partie') #Creation du bouton
        partie.place(relx=0.5, rely=0.4, anchor = tk.CENTER)
        partie.config(height=3, width= 15, relief=tk.GROOVE)

    def choixNiveaux():
        facile = tk.Button(root, text='Facile', height=3, width=10, relief=tk.GROOVE)
        moyen = tk.Button(root, text='Moyen', height=3, width=10, relief=tk.GROOVE)
        difficile = tk.Button(root, text='Difficile', height=3, width=10, relief=tk.GROOVE)
        progressif = tk.Button(root, text='Progressif', height=3, width=10, relief=tk.GROOVE)

        facile.place(relx=0.1, rely=0.4)
        moyen.place(relx=0.3, rely=0.4)
        difficile.place(relx=0.5, rely=0.4)
        progressif.place(relx=0.7, rely=0.4)

    def lancerScores():
        score = tk.Button(root, text='Tableau des scores')
        score.place(relx=0.5, rely=0.55, anchor = tk.CENTER)
        score.config(height=3, width= 15, relief=tk.GROOVE)

    def quit():
        quit = tk.Button(root, text='Quitter')
        quit.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
        quit.config(height=2, width=8, relief = tk.GROOVE)

# Main temporaire pour test affichage
if __name__ == "__main__" :
        root = tk.Tk()
        root.title("Jeu du carre rouge")
        root.geometry('700x700')
        VueMenu.affichageTitre()
        VueMenu.choixNiveaux()
        root.mainloop()