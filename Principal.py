from GameObjects import *
from interface import *

escolhas = interface()

#Lore

player = Player(escolhas[0],escolhas[1])

player.vidaAtual -= 10

player.status()

pocaoCura.efeitos[0](player)

player.status()