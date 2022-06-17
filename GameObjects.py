from Player import Player
from Arma import Arma
from Potion import Potion
from Inimigo import Inimigo

#Criar inimigos e suas skills aqui:


#Criar armas e suas skills aqui:


#Criar poções e seus efeitos aqui:
def curar_1(player: Player):

    print("*Cura*")
    player.vidaAtual += 2

    if player.vidaAtual > player.vidaMaxima:
        player.vidaAtual = player.vidaMaxima

pocaoCura = Potion("Poção de Cura", 1, [curar_1])