from typing import Callable

class Inimigo:

    def __init__(self, nome: str, vida: int, dano: int, skills: list[Callable] = None):
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.skills = skills