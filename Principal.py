from interface import interface
from Levels import levels
from GameObjects import *
from ferramentas import clear

#O jogo foi construido utilizando a versão 3.10.5 do Python

#Responsáveis por este projeto:
    #Allan Bastos da Silva
    #André Lisboa Augusto
    #Edson Rodrigues da Cruz Filho

escolhas = interface()

nomePlayer = escolhas[0]
classePlayer_ID = escolhas[1]
classeNome = classes[classePlayer_ID][0]
atributos = classes[classePlayer_ID][1]
armaPrincipal = classes[classePlayer_ID][2]
skill = classes[classePlayer_ID][3]

player = Player(nomePlayer, classeNome, atributos, armaPrincipal, skill)
gameOver = False
lvl = 0

while not gameOver:

    levelCode = levels[lvl](player)

    if levelCode == 1:
        lvl += 1
    elif levelCode == 0:
        clear()
        print("Game Over")
        gameOver = True
    elif levelCode == 2:
        break