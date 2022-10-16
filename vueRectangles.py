import tkinter as tk
from c31Geometry2 import *

class VueRectangles(tk.Frame):
    def __init__(self, root, difficulte) :
        
        #CREATION DU CANVAS 
        
        self.root = root
        self.canvas = tk.Canvas(root, background='white', width= 450, height= 450)
        self.vitesse = 0
        self.difficulte = difficulte

        #CHOIX DIFFICULTE
        
        if(self.difficulte == "facile"):
            self.vitesse = 1
        elif(self.difficulte == "moyen"):
            self.vitesse = 3
        elif(self.difficulte == "difficile"):
            self.vitesse = 5
        elif(self.difficulte == "progressif"):
            self.vitesse = 1

        #CREATION DES RECTANGLES
        
        self.rectangleBleuSupDroit = Rectangle(self.canvas, Vecteur(300, 85), 60, 50, remplissage= 'blue', bordure= 'black', epaisseur= 1) 
        self.x1 = -self.vitesse
        self.y1 = self.vitesse

        self.rectangleBleuGauche = Rectangle(self.canvas, Vecteur(100, 100), 60, 60,  remplissage= 'blue', bordure= 'black', epaisseur= 1)
        self.x2 = self.vitesse
        self.y2 = self.vitesse
        
        self.rectangleBleuInfDroit = Rectangle(self.canvas, Vecteur(355, 340), 100, 20, remplissage= 'blue', bordure= 'black', epaisseur= 1)
        self.x3 = -self.vitesse
        self.y3 = -self.vitesse

        self.rectangleBleuInfGauche = Rectangle(self.canvas, Vecteur(85, 350), 30, 60, remplissage= 'blue', bordure= 'black', epaisseur= 1) 
        self.x4 = self.vitesse
        self.y4 = -self.vitesse
        
    # DÉPLACEMENT DES RECTANGLES 

    def _moveRectangleBleuSupDroit(self) :
        position = self.rectangleBleuSupDroit.get_barycentre() 

        if(self.difficulte == "progressif"):
            if(position.x - 29 < 0 or position.x + 29 > 450) :
                self.x1 *= -1.1

            elif(position.y + 24 > 450 or position.y - 24 < 0) :
                self.y1 *= -1.1

        else:
            if(position.x - 29 < 0 or position.x + 29 > 450) :
                self.x1 *= -1

            elif(position.y + 24 > 450 or position.y - 24 < 0) :
                self.y1 *= -1

        self.rectangleBleuSupDroit.translate(Vecteur(self.x1, self.y1)) 
        self.rectangleBleuSupDroit.draw()


    def _moveRectangleBleuGauche(self) :
        position = self.rectangleBleuGauche.get_barycentre()

        if(self.difficulte == "progressif"):
            if(position.x + 29 > 450 or position.x - 29 < 0) :
                self.x2 *= -1.1

            elif(position.y + 25 > 450 or position.y - 25 < 0) :
                self.y2 *= -1.1

        else:
            if(position.x + 29 > 450 or position.x - 29 < 0) :
                self.x2 *= -1

            elif(position.y + 25 > 450 or position.y - 25 < 0) :
                self.y2 *= -1

        self.rectangleBleuGauche.translate(Vecteur(self.x2, self.y2))
        self.rectangleBleuGauche.draw()


    def _moveRectangleBleuInfDroit(self) :
        position = self.rectangleBleuInfDroit.get_barycentre()

        if(self.difficulte == "progressif"):
            if(position.y + 9 > 450 or position.y - 9 < 0) :
                self.y3 *= -1.1

            elif(position.x - 49 < 0 or position.x + 49 > 450) :
                self.x3 *= -1.1
        
        else:
            if(position.y + 9 > 450 or position.y - 9 < 0) :
                self.y3 *= -1

            elif(position.x - 49 < 0 or position.x + 49 > 450) :
                self.x3 *= -1

        self.rectangleBleuInfDroit.translate(Vecteur(self.x3, self.y3))
        self.rectangleBleuInfDroit.draw()


    def _moveRectangleBleuInfGauche(self) :
        position = self.rectangleBleuInfGauche.get_barycentre()

        if(self.difficulte == "progressif"):
            if(position.x + 14 > 450 or position.x - 14 < 0) :
                self.x4 *= -1.1

            elif(position.y + 29 > 450 or position.y - 29 < 0) :
                self.y4 *= -1.1
        
        else:
            if(position.x + 14 > 450 or position.x - 14 < 0) :
                self.x4 *= -1

            elif(position.y + 29 > 450 or position.y - 29 < 0) :
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
