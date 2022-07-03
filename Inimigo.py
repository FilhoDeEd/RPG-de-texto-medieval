from typing import Callable
from Arma import Arma
from Potion import Potion
from ferramentas import dado

class Inimigo:

    def __init__(self, nome: str, vidaMaxima: int, arma: Arma, drops: list[(Arma | Potion)] = [], skills: list[Callable] = []):

        #Informações básicas:
        self.nome = nome
        
        #Vida:
        self.vidaMaxima = vidaMaxima
        self.vidaAtual = vidaMaxima

        #Combate:
        self.skills = skills
        self.arma = arma
        self.morto = False
        if len(drops) == 0:
            self.temDrops = False 
            self.drops = []
        else:
            self.temDrops = True
            self.drops = drops

    def atacar(self) -> int:
        
        return self.arma.dano + dado(4)

    def defender(self) -> int:
        
        return self.arma.defesa + dado(4)