import random as rand
from GerenTerm import pause
from Potion import Potion
from Arma import Arma
from Inimigo import Inimigo

class Player:

    class Mochila:

        def __init__(self) -> None:

            #Lista que representa a mochila:
            self.pilhaMochila: list[Arma | Potion] = []
            self.qtdItens = 0

        def guardar(self, item: (Arma | Potion)) -> None:
        
            self.pilhaMochila.append(item)
            self.qtdItens += 1

        def retirarItem(self) -> (Arma | Potion | None):
            
            if self.qtdItens == 0:
                print("*Mochila vázia*")
                return

            print("Item:" + self.pilhaMochila[-1].nome)
            pause()

            Item = self.pilhaMochila.pop()
            self.qtdItens -= 1

            return Item

    class Cinto:

        def __init__(self) -> None:

            self.cinto: list[list[Arma | Potion]] = [[],[],[],[],[]]
            self.capacidadeMaxSlot = 2
            self.cargaAtualSlot = [0,0,0,0,0]
            self.qtdItensSlots = [0,0,0,0,0]
        
        def guardar(self, item: (Arma | Potion)) -> None:

            slotsLivres = []

            for i in range(5):
                if item.peso + self.cargaAtualSlot[i] <= 2:
                    slotsLivres.append(i)
            
            if slotsLivres.__len__ == 0:
                self@Player.cintoCheio(item)
                return
            
            randSlot = rand.choice(slotsLivres)

            self.cinto[randSlot].append(item)
            self.cargaAtualSlot[randSlot] += item.peso
            self.qtdItensSlots[randSlot] += 1

        #Se retirar poção, 
        def retirarItem(self):
            pass         

    def __init__(self, nome: str, classe: str, atributos: list[int], equipamentos: list[str]) -> None:

        #Informações básicas:
        self.nome = nome
        self.classe = classe
        self.atributos = {
            "STR":atributos[0],
            "DEX":atributos[1],
            "CON":atributos[2],
            "WIS":atributos[3],
            "INT":atributos[4],
            "CHA":atributos[5]
        }
        self.equipamentos = equipamentos

        #Vida:
        if classe == "Bárbaro": self.vidaMaxima = 36
        elif classe == "Soldado" or classe == "Patrulheiro": self.vidaMaxima = 30
        else: self.vidaMaxima = 24
        self.vidaAtual = self.vidaMaxima

        #Mochila, Cinto, Mão:
        self.mochila = self.Mochila()
        self.cinto = self.Cinto()
        self.armaPrincipal: Arma = None
        self.mao: (Arma | Potion) = None

        #Combate:
        self.alvo: Inimigo = None
        self.morto = False

    #Visão geral sobre o personagem
    def overview(self) -> None:

        print("Nome: {}\n".format(self.nome))

        print("Classe: {}\n".format(self.classe))

        print("Atributos: ")
        print("  STR: {}  DEX: {}".format(self.atributos["STR"],self.atributos["DEX"]))
        print("  CON: {}  WIS: {}".format(self.atributos["CON"],self.atributos["WIS"]))
        print("  INT: {}  CHA: {}\n".format(self.atributos["INT"],self.atributos["CHA"]))

        print("Equipamentos iniciais: ")
        print("  " + self.equipamentos[0])
        print("  " + self.equipamentos[1])
        print("  " + self.equipamentos[2]+"\n")

    #Para saber como vai a vida e outros status corriqueiros
    def status(self) -> None:

        #Dano
        print("Vida Atual: {}/{}".format(self.vidaAtual,self.vidaMaxima))

    #Utilizar um consumível
    def consumir(self, item: (Arma | Potion)) -> None:

        if type(item) == Potion:
            for efeito in item.efeitos:
                efeito(self@Player)
            return
        
        if type(item) == Arma:
            pass
    
    #Iniciar combate contra um inimigo
    def combate(self, alvo: Inimigo) -> None:
        
        self.alvo = alvo

    #É pra largar o item, colocar na mochila ou, caso consumível, usar já?
    def cintoCheio(self, item: (Arma | Potion)):

        print("*Cinto Cheio*")

        escolhasValidas = [1,2]
        valido = False

        print("O que fazer com o item?")
        print("Largar (1)")
        print("Guardar na mochila (2)")
        if item.isConsumivel:
            print("Consumir agora (3)")
            escolhasValidas.append(3)
        
        while not valido:

            escolha = int(input(": "))

            if escolha not in escolhasValidas:
                valido = False
                print("Não há essa opção")
            else: valido = True
            
        if escolha == 1:
           return

        if escolha == 2:
            self.mochila.guardar(item)
        
        if escolha == 3:
            self.consumir(item)