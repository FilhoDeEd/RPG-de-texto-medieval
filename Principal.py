from limpar_pausar import *
from Player import Player
from interface import *

escolhas = interface()
mago = Player(escolhas[0],escolhas[1])

mago.calcula_vida()