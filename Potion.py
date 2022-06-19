from typing import Callable

class Potion:

    def __init__(self, nome: str, peso: int, efeitos: list[Callable]) -> None:
        self.nome = nome
        self.peso = peso
        self.efeitos = efeitos
        