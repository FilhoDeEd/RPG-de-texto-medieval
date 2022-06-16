from limpar_pausar import *
from Classes import classes

def interface():

    print("Bem Vindo")

    nomePlayer = input("Escolha um nome: ")

    i = 0

    while True:

        print(i)

        i = int(input("Digite: "))

        if i == 4: break

        print("<<a   ({}/5)   d>>".format(i))

    print("Fim do loop")
    pause()

interface()