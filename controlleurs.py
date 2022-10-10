
# -*- coding: utf8 -*-
from vues import VueJeu


class JeuControler :
    def __init__(self, root, vues) :
        self.vues = VueJeu(root)

    def start(self, root) :
        self.vues.dessiner(root)    