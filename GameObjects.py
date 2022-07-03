import random as rand
from Player import Player
from Arma import Arma
from Potion import Potion
from Inimigo import Inimigo
from ferramentas import dado

#Criar armas aqui:

    #Lixo:
pedra = Arma("Pedra", True, 1, 0)
osso = Arma("Osso", True, 1, 1)
couro = Arma("Couro",True, 0, 1)
    #Armas iniciais:
machado = Arma("Machado", True, 8, 3) #Bárbaro
espada = Arma("Espada", True, 6, 2) #Soldado
arco = Arma("Arco", False, 6, 1) #Patrulheiro
adaga = Arma("Adaga", True, 4, 1) #Ladrão - Goblin - DROP
martelo = Arma("Martelo", True, 7, 2) #Clérigo
foco_arcano = Arma("Foco Arcano", False, 9, 0) #Mago
    #Outras armas
punho = Arma("Punho", True, 2, 2) #Esqueleto do Monge
presas = Arma("Presas", True, 5, 2) #Lobo
arco_velho = Arma("Arco Velho", False, 5, 0) #Esqueleto
cauda_venenosa = Arma("Cauda Venenosa", True, 7, 2) #Escorpião - DROP
arma_natural = Arma("Arma Natural", True, 10, 3) #Outono
besta = Arma("Besta", False, 7, 2) #Achado
maca = Arma("Maça", True, 8, 2) #Achado
boomerang = Arma("Boomerang", False, 3, 1) #Achado
escudo = Arma("Escudo", True, 2, 6) #Achado

#Criar poções e seus efeitos aqui:
def curar(player: Player) -> None:

    print("*Cura*")

    qtdCura = dado(4, 2, True)

    player.vidaAtual += qtdCura

    if player.vidaAtual > player.vidaMaxima:
        player.vidaAtual = player.vidaMaxima

pocaoCura = Potion("Poção de Cura","Cura uma quantidade aleatória de vida",[curar])

def forca(player: Player) -> None:
    
    print("*Força*")

    if player.inCombate:
        player.danoExtra += 3
    else:
        player.danoExtra = 3

pocaoForca = Potion("Poção de Força","Aumenta o seu dano em 3 até o seu próximo ataque",[forca])

def resistencia(player: Player) -> None:
    
    print("*Resistência*")

    if player.inCombate:
        player.defesaExtra += 2
    else:
        player.defesaExtra = 2

pocaoResistencia = Potion("Poção de Resistência","Aumenta a sua defesa em 2 até sua próxima defesa",[resistencia])

def shuffle(player: Player) -> None:
    
    print("*Embaralhar*")

    rand.shuffle(player.mochila.pilhaMochila)

pocaoEmbaralhar = Potion("Embaralhar","Embaralhar os itens de sua mochila",[shuffle])

def cachaca(player: Player) -> None:

    print("*Cachaça*")

    player.danoExtra -= 2

corote = Potion("Cachaça","Literalmente cachaça",[cachaca])

#Criar inimigos e suas skills aqui:

esqueleto = Inimigo("Esqueleto", 8, arco_velho, [arco_velho, osso])
goblin = Inimigo("Goblin", 26, adaga, [adaga, pocaoCura])
esqueleto_monge = Inimigo("Esqueleto do Monge", 32, punho)
lobo = Inimigo("Grande Lobo Branco", 50, presas, [couro, pocaoForca])
escorpiao = Inimigo("Escorpião", 30, cauda_venenosa, [cauda_venenosa, pocaoEmbaralhar])
outono = Inimigo("Outono", 60, arma_natural)

#----------------------------------------------------------------------------------------------

#Criar skills aqui:

def furia(player: Player, alvo: Inimigo):
    
    print("*Fúria*")

    player.defesaExtra += 5

def ataque_extra(player: Player, alvo: Inimigo):
    
    print("*Ataque Extra*")

    player.danoExtra += player.armaPrincipal.dano

def especializacao(player: Player, alvo: Inimigo):
    
    print("*Especialização*")

    alvo.vidaAtual -= 6

def ataque_furtivo(player: Player, alvo: Inimigo):
    
    print("*Ataque Furtivo*")

    player.lancesExtraDano += 2

def luz_da_punicao(player: Player, alvo: Inimigo):
    
    print("*Luz da Punição*")

    curar(player)

    alvo.vidaAtual -= 3

def bola_de_fogo(player: Player, alvo: Inimigo):
    
    print("*Bola de Fogo*")

    alvo.vidaAtual -= 15

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