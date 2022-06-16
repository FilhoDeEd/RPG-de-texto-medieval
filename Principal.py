from GerenTerm import *
from Player import Player
from interface import *

escolhas = interface()

player = Player(escolhas[0],escolhas[1])
player.calcula_vida()
player.overview()