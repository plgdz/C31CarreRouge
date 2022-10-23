import tkinter as tk
from controlleurs import *

if __name__ == "__main__" :
    root = tk.Tk()
    root.title("Jeu du Carré Rouge")  
    root.geometry("700x700")  

    menu = MenuControler(root)
    
    root.mainloop()