import random as rand
from Player import Player
from Arma import Arma
from Potion import Potion
from Inimigo import Inimigo
from ferramentas import dado

#Criar inimigos e suas skills aqui:

esqueleto = Inimigo("Esqueleto", 4, 2, 2)

Goblin = Inimigo("Goblin", 0, 0, 0)
Esqueleto_Monge = Inimigo("Esqueleto do Monge", 0, 0, 0)
Lobo = Inimigo("Lobo", 0, 0, 0)
Escorpião = Inimigo("Escorpião", 0, 0, 0)
Outono = Inimigo("Outono", 0, 0, 0)


#Criar armas aqui:

pedra = Arma("Pedra", True, 1, 0)

Machado = Arma("Pedra", True, 0, 0) #Bárbaro
Espada = Arma("Espada", True, 0, 0) #Soldado
Arco = Arma("Arco", False, 0, 0) #Patrulheiro
Adaga = Arma("Adaga", True, 0, 0) #Ladrão - Goblin - DROP
Martelo = Arma("Martelo", True, 0, 0) #Clérigo
Foco_Arcano = Arma("Foco Arcano", True, 0, 0) #Mago
Punho = Arma("Punho", True, 0, 0) #Esqueleto do Monge
Presas = Arma("Pesas", True, 0, 0) #Lobo
Cauda_Venenosa = Arma("Cauda Venenosa", True, 0, 0) #Escorpião - DROP
Arma_Natural = Arma("Arma Natural", True, 0, 0) #Outono
Besta = Arma("Besta", False, 0, 0) #Achado
Maça = Arma("Maça", True, 0, 0) #Achado
Boomerang = Arma("Boomerang", False, 0, 0) #Achado

#Criar skills aqui:
Furia = Skill("Furia", ) #Bárbaro
Ataque_Extra = Skill("Ataque Extra", ) #Soldado
Especialização = Skill("Especialização", ) #Patrulheiro
Ataque_Furtivo = Skill("Ataque Furtivo", ) #Ladrão
Luz_da_Punição = Skill("Luz da Punição", ) #Clérigo
Bola_de_Fogo = Skill("Bola de Fogo", ) #Mago

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