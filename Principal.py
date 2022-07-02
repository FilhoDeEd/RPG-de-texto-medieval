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