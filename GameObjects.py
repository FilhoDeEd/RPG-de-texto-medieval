import random as rand
from Player import Player
from Arma import Arma
from Potion import Potion
from Inimigo import Inimigo
from ferramentas import dado

#Criar inimigos e suas skills aqui:

esqueleto = Inimigo("Esqueleto", 4, 2, 2)
goblin = Inimigo("Goblin", 0, 0, 0)
esqueleto_Monge = Inimigo("Esqueleto do Monge", 0, 0, 0)
lobo = Inimigo("Lobo", 0, 0, 0)
escorpião = Inimigo("Escorpião", 0, 0, 0)
outono = Inimigo("Outono", 0, 0, 0)

#Criar armas aqui:

pedra = Arma("Pedra", True, 1, 0)

machado = Arma("Pedra", True, 0, 0) #Bárbaro
espada = Arma("Espada", True, 0, 0) #Soldado
arco = Arma("Arco", False, 0, 0) #Patrulheiro
adaga = Arma("Adaga", True, 0, 0) #Ladrão - Goblin - DROP
martelo = Arma("Martelo", True, 0, 0) #Clérigo
foco_arcano = Arma("Foco Arcano", True, 0, 0) #Mago
punho = Arma("Punho", True, 0, 0) #Esqueleto do Monge
presas = Arma("Pesas", True, 0, 0) #Lobo
cauda_venenosa = Arma("Cauda Venenosa", True, 0, 0) #Escorpião - DROP
arma_natural = Arma("Arma Natural", True, 0, 0) #Outono
besta = Arma("Besta", False, 0, 0) #Achado
maca = Arma("Maça", True, 0, 0) #Achado
boomerang = Arma("Boomerang", False, 0, 0) #Achado

#Criar skills aqui:


def furia(player: Player, alvo: Inimigo):
    pass

def ataque_extra(player: Player, alvo: Inimigo):
    pass

def especializacao(player: Player, alvo: Inimigo):
    pass

def ataque_furtivo(player: Player, alvo: Inimigo):
    pass

def luz_da_punicao(player: Player, alvo: Inimigo):
    pass

def bola_de_fogo(player: Player, alvo: Inimigo):
    pass

#Criar poções e seus efeitos aqui:
def curar(player: Player) -> None:

    print("*Cura*")

    qtdCura = dado(4, 2, True)

    player.vidaAtual += qtdCura

    if player.vidaAtual > player.vidaMaxima:
        player.vidaAtual = player.vidaMaxima

pocaoCura = Potion("Poção de Cura","Cura uma quantidade aleatória de vida",[curar])

def shuffle(player: Player) -> None:
    
    print("*Embaralhar*")

    rand.shuffle(player.mochila.pilhaMochila)

pocaoEmbaralhar = Potion("Embaralhar","Embaralhar os itens de sua mochila",[shuffle])

#fazer uma poção que retira um item aleatório da mochila
#É só usar random.choice()

#----------------------------------------------------------------------------------------------

#[<Nome>,<Atributos>,<Arma inicial>,<Skill>]
#Ordem dos atributos: Força, Destreza, Constituição, Sabedoria, Inteligência, Carisma
classes = {
    0:["Bárbaro", [14, 12, 15, 8, 10, 13], machado, ["Fúria", furia]],
    1:["Soldado", [15, 12, 14, 8, 13, 10], espada, ["Ataque Extra", ataque_extra]],
    2:["Patrulheiro", [12, 15, 13, 14, 10, 8], arco, ["Especialização", especializacao]],
    3:["Ladrão", [8, 15, 12, 13, 14, 10], adaga, ["Ataque Furtivo", ataque_furtivo]],
    4:["Clérigo", [13, 8, 14, 15, 10, 12], martelo, ["Luz da Punição", luz_da_punicao]],
    5:["Mago", [8, 13, 14, 12, 15, 10], foco_arcano, ["Bola de Fogo", bola_de_fogo]]
}