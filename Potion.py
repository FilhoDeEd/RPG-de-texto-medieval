from typing import Callable

class Potion:

    def __init__(self, nome: str, descricao:str, efeitos: list[Callable]) -> None:

        self.nome = nome
        self.descricao = descricao
        self.peso = 1
        self.efeitos = efeitos