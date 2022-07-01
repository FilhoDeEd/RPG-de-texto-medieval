from interface import interface
from Levels import levels
from GameObjects import *

#O jogo foi construido utilizando a versão 3.10.5 do Python

escolhas = interface()

#Lore

nomePlayer = escolhas[0]
classePlayer_ID = escolhas[1]
classeNome = classes[classePlayer_ID][0]
atributos = classes[classePlayer_ID][1]
equipamentos = classes[classePlayer_ID][2]

player = Player(nomePlayer, classeNome, atributos, equipamentos)
lvl = 0

while not player.morto:

    levelCode = levels[lvl](player)

    if levelCode == 1: lvl += 1

#Combate:
    #Utilizar poções guardadas no cinto
    #Atacar com arma principal
    #Usar skill de classe
# Andando:
    #Utilizar (todas as poções do cinto + poção do topo da mochila (se tiver))
    #Pode interagir livremente com mochila e cinto:
        #Se retirar um item, ele vai para a mão. Na mão ele pode
            #Dropar
            #Se Arma: pode definir como arma principal
            #Se Potion: pode Beber
            #Pode guardar no cinto (não tem restrição)
            #Pode guardar na mochila se o item não veio da mochila
        #Ver itens
            #Na mochila, só pode ver o item do topo
            #No cinto, pode ver todos
    #Se ele achar um báu:
        #Manter
            #Guardar na mochila
            #Guardar no cinto
            #Se Potion: Beber
            #Se Arma: Definir como principal
        #Dropar