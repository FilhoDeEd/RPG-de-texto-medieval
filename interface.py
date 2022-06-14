from limpar_pausar import *
from Classes import classes

def interface():

    print("Bem vindo")

    nome = input("Escolha seu nome: ")
    classe = None

    while classe==None:

        clear()

        print("Escolha seu nome: " + nome)
        
        print("\nEscolha uma das classes abaixo: ")
        for i in ["Bárbaro","Soldado","Patrulheiro","Ladrão","Clérigo"]:
            print("\n" + classes[i][0] + ":")

            print("\tAtributos: ")
            print("\t\t" + "STR: " + str(classes[i][1][0]) + "\t" + "DEX: " + str(classes[i][1][1]))
            print("\t\t" + "CON: " + str(classes[i][1][2]) + "\t" + "WIS: " + str(classes[i][1][3]))
            print("\t\t" + "INT: " + str(classes[i][1][4]) + "\t" + "CHA: " + str(classes[i][1][5]))

            print("\tEquipamentos iniciais: ")
            print("\t\t" + classes[i][2][0] + "\t" + classes[i][2][0] + "\t" + classes[i][2][0])
        print("\n")

        classe = classes.get(input("Esolha: "), None)
        if classe==None:
            print("Escolha uma classe existente.")
            pause()

    escolhas = []
    escolhas.append(nome)
    escolhas.append(classe[0])

    return escolhas