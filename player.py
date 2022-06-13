class player:

    def _init_(self,nome, classe, atributos, equipamento):
        print("Nome: " + nome)
        print("Classe: " + classe)
        print("STR: ",atributos[0])
        print("DEX: ",atributos[1])
        print("CON: ",atributos[2])
        print("WIS: ",atributos[3])
        print("INT: ",atributos[4])
        print("CHA: ",atributos[5])
        print(equipamento)

    def calcula_vida(self):
        print("Vida")