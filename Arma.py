from typing import Callable

class Arma:

    def __init__(self, nome: str, isMeele: bool, isConsumivel: bool,
                    dano: int, defesa: int, skills: list[Callable] = None) -> None:

        self.nome = nome
        self.isMeele = isMeele
        self.isConsumivel = isConsumivel
        self.peso = 2
        self.dano = dano
        self.defesa = defesa
        self.skills = skills