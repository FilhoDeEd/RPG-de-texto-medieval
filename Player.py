from GerenTerm import clear,pause
from Classes import classes

class Player:

    def __init__(self, nome, classe_ID):
        self.nome = nome
        self.classe = classes[classe_ID][0]
        self.atributos = classes[classe_ID][1]
        self.equipamentos = classes[classe_ID][2]

        if classe_ID == 0: self.vidaMaxima = 36
        elif classe_ID == 1 or classe_ID == 2: self.vidaMaxima = 30
        else: self.vidaMaxima = 24

        self.vidaAtual = self.vidaMaxima

    #Visão geral sobre o personagem
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

    #Para saber como vai a vida e outros status corriqueiros
    def status(self):

        #Dano
        print("Vida Atual: {}/{}".format(self.vidaAtual,self.vidaMaxima))
    
    def mochila():
        print("Mochila Mochila... Mochila Mochila... Eu sou a mochila...")
