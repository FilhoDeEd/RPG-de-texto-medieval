from Player import Player
from Arma import Arma
from Potion import Potion
from Inimigo import Inimigo
import random as rand

#Criar inimigos e suas skills aqui:


#Criar armas e suas skills aqui:


#Criar poções e seus efeitos aqui:
def curar_1(player: Player) -> None:

    print("*Cura*")
    player.vidaAtual += 2

    if player.vidaAtual > player.vidaMaxima:
        player.vidaAtual = player.vidaMaxima

pocaoCura = Potion("Poção de Cura", [curar_1])

    #Ideia: Fazer uma poção que "embarralhe" os itens da mochila do player;
    #É só usar o método random.shuffle(), que consegue embarralhar uma lista;
    #Já que o cara só pode acessar itens no topo, isso pode ser muito útil
    #dependendo da sorte do cara
    #Na mesma linha, dá pra fazer uma poção que retira um item aleatório da mochila
    #É só usar random.choice()

#Um dado bem versátil. Você pode escolher o número de faces (por padrão é 6),
#o número de lances (por padrão é 1) e
#se esses os valores de cada lance devem ser somados ou não (por padrão não)
def dado(faces: int = 6, lances: int = 1, somar: bool = False ) -> (int | list):

    valores = []

    for i in range(lances):
        randNum = rand.randint(1,faces)
        valores.append(randNum)
    
    if somar:
        return sum(valores)
    else: return valores