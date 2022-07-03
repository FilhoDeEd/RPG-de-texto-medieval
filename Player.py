import random as rand
from ferramentas import escolhasUser, dado
from Potion import Potion
from Arma import Arma
from Inimigo import Inimigo

class Player:

    class Mochila:

        def __init__(self) -> None:

            #Lista que representa a mochila:
            self.pilhaMochila: list[Arma | Potion] = []
            self.itemTopo: (Arma | Potion) = None
            self.qtdItens = 0

        def guardar(self, item: (Arma | Potion)) -> (Arma | Potion | None):
            
            if item.passouMochila:
                print("*Esse item está amaldiçoado e não pode voltar a mochila*")
                return item

            self.pilhaMochila.append(item)
            self.itemTopo = item
            self.qtdItens += 1
            return None

        def retirar(self) -> (Arma | Potion | None):
            
            if self.qtdItens == 0:
                print("*Mochila vázia*")
                return None

            print("Item: {}".format(self.itemTopo.nome))
            tecla = escolhasUser(["confirmar","cancelar"])

            if tecla == 2:
                return None

            item = self.pilhaMochila.pop()
            self.qtdItens -= 1
            item.passouMochila = True
            self.itemTopo = self.pilhaMochila[-1]

            return item
        
        def mostrar(self) -> None:

            print("Mochila:")
            print("  {}".format(self.itemTopo.nome))

    class Cinto:

        def __init__(self) -> None:

            self.matrizCinto: list[list[Arma | Potion]] = [[],[],[],[],[]]
            self.capacidadeMaxSlot = 2
            self.cargaAtualSlot = [0,0,0,0,0]
            self.qtdItensSlots = [0,0,0,0,0]
        
        def guardar(self, item: (Arma | Potion)) -> (Arma | Potion | None):

            slotsLivres = []

            for i in range(5):
                if item.peso + self.cargaAtualSlot[i] <= 2:
                    slotsLivres.append(i)
            
            if len(slotsLivres) == 0:
                print("*Cinto cheio*")
                return item
            
            randSlot = rand.choice(slotsLivres)

            self.matrizCinto[randSlot].append(item)
            self.cargaAtualSlot[randSlot] += item.peso
            self.qtdItensSlots[randSlot] += 1
            return None
 
        def retirar(self) -> (Arma | Potion | None):

            self.mostrar()
                    
            nomeItemRetirar = input("Digite o nome do item: ")

            for i in range(5):
                for j in range(self.qtdItensSlots[i]):
                    if nomeItemRetirar == self.matrizCinto[i][j].nome:
                        item = self.matrizCinto[i].pop(j)
                        self.cargaAtualSlot[i] -= item.peso
                        self.qtdItensSlots[i] -= 1
                        return item

            print("*Item não encontrado*")
            return None

        def mostrar(self) -> None:
            
            print("Cinto:")
            for i in range(5):
                print("  Slot {}".format(i+1))
                for j in range(self.qtdItensSlots[i]):
                    print("   {}".format(self.matrizCinto[i][j].nome))     

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
        self.morto = False

    #Visão geral sobre o personagem:
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

    #Para saber como vai a vida e outros status corriqueiros:
    def status(self) -> None:

        if self.armaPrincipal != None:
            print("Arma Principal: {}".format(self.armaPrincipal.nome))
        else:
            print("Sem arma principal")
        print("Vida Atual: {}/{}".format(self.vidaAtual,self.vidaMaxima))
    
    #Calcular ataque:
    def atacar(self) -> int:
        
        return self.armaPrincipal.dano + dado(6)
    
    #Calcular defesa:
    def defender(self) -> int:
        
        return self.armaPrincipal.defesa + dado(6)