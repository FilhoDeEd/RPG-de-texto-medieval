from ferramentas import clear, pause
from GameObjects import classes

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

        print("Arma inicial: ")
        print("  " + classes[i][2].nome)

        print("Skill de classe: ")
        print(classes[i][3][0])

        if i==0: print("\n         ({}/6)   d>>\n".format(i+1))
        elif i==4: print("\n   <<a   ({}/6)\n".format(i+1))
        else: print("\n   <<a   ({}/6)   d>>\n".format(i+1))

        tecla = input("Digite y para escolher: ").lower()

        if tecla == 'y':
            escolhido = True

        elif tecla == 'a':
            if i > 0: i-=1

        elif tecla == 'd': 
            if i < 5: i+=1

        else:
            print("Selecione uma opção válida.")
            pause()

    clear()

    classePlayer = i

    return [nomePlayer,classePlayer]