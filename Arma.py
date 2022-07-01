from typing import Callable

class Arma:

    def __init__(self, nome: str, isMeele: bool, dano: int, defesa: int) -> None:

        self.nome = nome
        self.isMeele = isMeele
        self.peso = 2
        self.dano = dano
        self.defesa = defesa
        self.passouMochila = False