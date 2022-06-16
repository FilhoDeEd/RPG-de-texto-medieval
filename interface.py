from GerenTerm import *
from Classes import classes

def interface():

    print("Bem Vindo\n")

    nomePlayer = input("Por favor, escolha um nome: ")

    i = 0
    escolhido = False

    while not escolhido:

        clear()

        print("Saudações {}! Escolha uma classe:\n".format(nomePlayer))

        print("\t" + classes[i][0] + "\n")

        print("Atributos: ")
        print("  STR: {}  DEX: {}".format(classes[i][1][0],classes[i][1][1]))
        print("  CON: {}  WIS: {}".format(classes[i][1][2],classes[i][1][3]))
        print("  INT: {}  CHA: {}\n".format(classes[i][1][4],classes[i][1][5]))

        print("Equipamentos iniciais: ")
        print("  " + classes[i][2][0])
        print("  " + classes[i][2][1])
        print("  " + classes[i][2][2])

        if i==0: print("\n         ({}/5)   d>>\n".format(i+1))
        elif i==4: print("\n   <<a   ({}/5)\n".format(i+1))
        else: print("\n   <<a   ({}/5)   d>>\n".format(i+1))

        tecla = input("Digite y para escolher: ").lower()

        if tecla == 'y':
            escolhido = True

        elif tecla == 'a':
            if i > 0: i-=1

        elif tecla == 'd': 
            if i < 4: i+=1

        else:
            print("Selecione uma opção válida.")
            pause()

    classePlayer = i

    return [nomePlayer,classePlayer]