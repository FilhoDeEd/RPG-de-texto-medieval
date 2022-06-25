from typing import Callable
from Dictios import raridades

class Arma:

    def __init__(self, nome: str, isMeele: bool, raridade_ID: int,
                    dano: int, defesa: int, skills: list[Callable]) -> None:
        self.nome = nome
        self.isMeele = isMeele
        self.peso = 2
        self.raridade_ID = raridade_ID
        self.dano = dano
        self.defesa = defesa
        self.skills = skills
        