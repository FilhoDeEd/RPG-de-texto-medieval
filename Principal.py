from GerenTerm import clear,pause
from interface import interface
from Levels import levels
from GameObjects import *

#O jogo foi construido utilizando a versão 3.10.5 do Python

escolhas = interface()

#Lore

player = Player(escolhas[0],escolhas[1])
gameOver = False
lvl = 0

while not gameOver:
    levelCode = levels[lvl](player, levelsGameObjects[lvl][1], levelsGameObjects[lvl][2])

print(dado(6,10,True))