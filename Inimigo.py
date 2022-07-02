from typing import Callable

class Inimigo:

    def __init__(self, nome: str, vida: int, dano: int, skills: list[Callable] = []):

        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.skills = skills
        self.medo = 0.0

    def ataque(self):
        pass

    def defesa(self):
        pass