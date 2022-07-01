from Player import Player
from Arma import Arma
from Potion import Potion
from Inimigo import Inimigo
import random as rand

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

#Criar inimigos e suas skills aqui:

esqueleto = Inimigo("Esqueleto",4,2)

#Criar armas e suas skills aqui:

pedra = Arma("Pedra", True, True, 0, 1, 0)

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

    rand.shuffle(player.mochila)

pocaoEmbaralhar = Potion("Embaralhar","Embaralhar os itens de sua mochila",[shuffle])

#fazer uma poção que retira um item aleatório da mochila
#É só usar random.choice()

#[<Nome>,<Atributos>,<Equipamentos>]
#Ordem dos atributos: Força, Destreza, Constituição, Sabedoria, Inteligência, Carisma
classes = {
    0:["Bárbaro",[14, 12, 15, 8, 10, 13],["Machado","Gibão de Pele","Totem"]],
    1:["Soldado",[15, 12, 14, 8, 13, 10],["Espada","Armadura de Talas","Escudo"]],
    2:["Patrulheiro",[12, 15, 13, 14, 10, 8],["Arco","Brunea","Mapa"]],
    3:["Ladrão",[8, 15, 12, 13, 14, 10],["Adaga","Armadura de Couro","Ferramentas"]],
    4:["Clérigo",[13, 8, 14, 15, 10, 12],["Martelo","Armadura de Placas","Símbolo Sagrado"]],
    5:["Mago",[8, 13, 14, 12, 15, 10],["Foco Arcano","Manto","Grimório"]]
}