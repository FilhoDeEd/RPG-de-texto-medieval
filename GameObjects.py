from Player import Player
from Arma import Arma
from Potion import Potion
from Inimigo import Inimigo
import random as rand

#Criar inimigos e suas skills aqui:

esqueleto = Inimigo("Esqueleto",4,2)

#Criar armas e suas skills aqui:

pedra = Arma("Pedra", True, True, 0, 1, 0)

#Criar poções e seus efeitos aqui:
def curar_1(player: Player) -> None:

    print("*Cura*")

    qtdCura = dado(4, 2, True)

    player.vidaAtual += qtdCura

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

#[<Nome do Level>:<Inimigos>,<Itens para recompensa>]
levelsGameObjects = {
    0:["floresta",[esqueleto],[pedra,pocaoCura]],
    1:["tumba",[esqueleto],[pedra,pocaoCura]],
    2:["cidade",[esqueleto],[pedra,pocaoCura]],
    3:["casaBruxa",[esqueleto],[pedra,pocaoCura]],
    4:["deserto",[esqueleto],[pedra,pocaoCura]],
    5:["ultimaCidade",[esqueleto],[pedra,pocaoCura]]
}

def dado(faces: int = 6, lances: int = 1, somar: bool = False ) -> (int | list):

    valores = []

    for i in range(lances):
        randNum = rand.randint(1,faces)
        valores.append(randNum)
    
    if somar:
        return sum(valores)
    else: return valores