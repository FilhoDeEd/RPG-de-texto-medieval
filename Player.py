import random as rand
from GerenTerm import clear,pause
from GameObjects import classes
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

        def retirarItem(self):
            pass         

    def __init__(self, nome: str, classe_ID: int) -> None:

        #Informações básicas:
        self.nome = nome
        self.classe = classes[classe_ID][0]
        self.atributos = classes[classe_ID][1]
        self.equipamentos = classes[classe_ID][2]

        #Vida:
        if classe_ID == 0: self.vidaMaxima = 36
        elif classe_ID == 1 or classe_ID == 2: self.vidaMaxima = 30
        else: self.vidaMaxima = 24
        self.vidaAtual = self.vidaMaxima

        #Mochila e Cinto:
        self.mochila = self.Mochila()
        self.cinto = self.Cinto()

        #Combate:
        self.alvo: Inimigo = None
        self.morto = False

    #Visão geral sobre o personagem
    def overview(self) -> None:
        
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