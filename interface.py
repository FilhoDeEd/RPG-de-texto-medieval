from limpar_pausar import *

#[<Atributos>,<Equipamentos>]
#Ordem dos atributos: Força, destresa, constituição, sabedoria, inteligencia, carisma
classes = {
    "Bárbaro":["Bárbaro",[14, 12, 15, 13, 10, 8],["Machado","Gibão de Pele","Totem"]],
    "Soldado":["Soldado",[15, 13, 14, 8, 12, 10],["Espada","Armadura de Talas","Escudo"]],
    "Patrulheiro":["Patrulheiro",[12, 15, 13, 14, 10, 8],["Arco","Brunea","Mapa"]],
    "Ladrão":["Ladrão",[8, 15, 12, 13, 14, 10],["Adaga","Armadura de Couro","Ferramentas"]],
    "Clérigo":["Clérigo",[13, 8, 14, 15, 10, 12],["Martelo","Armadura de Placas","Símbolo Sagrado"]]
}

def interface():

    print("Bem vindo")

    nome = input("Escolha seu nome: ")
    classe = 0

    while classe==0:
        clear()

        for i in ["Bárbaro","Soldado","Patrulheiro","Ladrão","Clérigo"]:
            print(classes[i])
        
        print("\n")

        classe = classes.get(input("Esolha sua classe: "), 0)
        if classe==0:
            print("Escolha inválida")
            pause()

    escolhas = []

    escolhas.append(nome)
    escolhas.append(classe[0])
    escolhas.append(classe[1])
    escolhas.append(classe[2])

    return escolhas