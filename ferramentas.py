import os
import random as rand

#Função para limpar a tela do terminal
def clear() -> None:
    os.system('cls||clear')

#Função para pausar o programa
def pause() -> None:
    input("Pressione Enter para continuar ")

#Função que ajuda a receber dados do usuário
def escolhasUser(opcoes: list[str]) -> int:

    numOpcoes = len(opcoes)

    valoresValidos = range(numOpcoes)

    print(" ")
    for i in valoresValidos:
        print("{} para {}".format(i+1,opcoes[i]))
    
    while True:
        try:
            escolha = int(input("Selecione uma opção: "))
            if escolha-1 in valoresValidos: break
            print("Escolha uma opção válida")
        except:
            print("Escolha uma opção válida")

    print(" ")
    return escolha

#Um dado bem versátil. Você pode escolher o número de faces (por padrão é 6),
#o número de lances (por padrão é 1) e
#se esses os valores de cada lance devem ser somados ou não (por padrão não)
def dado(faces: int = 6, lances: int = 1, somar: bool = False ) -> (int | list):

    valores = []

    for i in range(lances):
        randNum = rand.randint(1,faces)
        valores.append(randNum)
    
    if somar:
        return sum(valores)
    else:
        return valores