from typing import Callable
from Arma import Arma
from ferramentas import dado

class Inimigo:

    def __init__(self, nome: str, vidaMaxima: int, arma: Arma, skills: list[Callable] = []):

        #Informações básicas:
        self.nome = nome
        
        #Vida:
        self.vidaMaxima = vidaMaxima
        self.vidaAtual = vidaMaxima

        #Combate:
        self.skills = skills
        self.arma = arma
        self.medo = 0.0
        self.morto = False

    def atacar(self) -> int:
        
        return self.dano + dado(4)

    def defender(self) -> int:
        
        return self.defesa + dado(4)