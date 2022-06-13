from limpar_pausar import *
import player as pl
from interface import *

escolhas = interface()

mago = pl.player()
mago._init_(escolhas[0], escolhas[1], escolhas[2], escolhas[3])

mago.calcula_vida()