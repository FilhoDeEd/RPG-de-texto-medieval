from GerenTerm import clear,pause
from Classes import *

class Player:

    def __init__(self, nome, classe_ID):
        self.nome = nome
        self.classe = classes[classe_ID][0]
        self.atributos = classes[classe_ID][1]
        self.equipamentos = classes[classe_ID][2]

    def calcula_vida(self):
        print("Vida")

    def overview(self):
        
        clear()

        print("Nome: {}\n".format(self.nome))

        print("Classe: {}\n".format(self.classe))

        print("Atributos: ")
        print("  STR: {}  DEX: {}".format(self.atributos[0],self.atributos[1]))
        print("  CON: {}  WIS: {}".format(self.atributos[2],self.atributos[3]))
        print("  INT: {}  CHA: {}\n".format(self.atributos[4],self.atributos[5]))

        print("Equipamentos iniciais: ")
        print("  " + self.equipamentos[0])
        print("  " + self.equipamentos[1])
        print("  " + self.equipamentos[2]+"\n")

        pause()
        clear()
