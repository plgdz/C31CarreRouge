import tkinter as tk
from functools import partial

class VueMenu:
    def affichageTitre():
        titre = tk.Label(root, text = "Jeu du carre rouge") # Creation du titre
        titre.config(background=('blue'))
        titre.place(relx=0.5, rely=0.15, anchor=tk.CENTER) #Placement du titre au centre 
        return titre

    def styleBouton():
        style = tk.st

    def lancerJeu():
        partie = tk.Button(root, text='Lancer une partie') #Creation du bouton
        partie.place(relx=0.5, rely=0.4, anchor = tk.CENTER)
        partie.config(height=3, width= 15,
                        relief=tk.GROOVE)

    def lancerScores():
        score = tk.Button(root, text='Tableau des scores')
        score.place(relx=0.5, rely=0.55, anchor = tk.CENTER)
        score.config(height=3, width= 15,
                        relief=tk.GROOVE)

    def quit():
        quit = tk.Button(root, text='Quitter')
        quit.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
        quit.config(height=2, width=8, relief = tk.GROOVE)

# Main temporaire pour test affichage
if __name__ == "__main__" :
        root = tk.Tk()
        root.title("Jeu du carre rouge")
        root.geometry('400x400')
        VueMenu.affichageTitre()
        VueMenu.lancerJeu()
        VueMenu.lancerScores()
        VueMenu.quit()
        root.mainloop()


