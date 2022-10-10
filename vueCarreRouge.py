import tkinter as tk
import c31Geometry2 as c31

#Initialization
root = tk.Tk()
root.config(background="white")
root.geometry("450x450")
canvas = tk.Canvas(root, background='white')

#Titre
root.title("Carre Rouge")

#Affichage Carre Rouge position 225 x 225
carreRouge = c31.Carre(canvas, c31.Vecteur(225, 225), 50, remplissage= 'red')
carreRouge.draw()
canvas.grid()

root.mainloop()