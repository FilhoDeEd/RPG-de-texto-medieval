from Classes import *

class Player:

    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.atributos = classes[classe][1]
        self.equipamentos = classes[classe][2]

    def calcula_vida(self):
        print("Vida")