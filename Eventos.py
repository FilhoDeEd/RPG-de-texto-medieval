from Player import Player
from Inimigo import Inimigo
from Arma import Arma
from Potion import Potion
from ferramentas import escolhasUser

#Fora de combate:
def andando(player: Player) -> None:

        while True:

            mainCommand = escolhasUser(["prosseguir","mexer nos itens","consumir uma poção","ver status"])

            #Prosseguir história:
            if mainCommand == 1:
                break

            #Mexer nos itens:
            elif mainCommand == 2:
                
                if player.mao == None:
                    print("Sem item na mão\n")
                else:
                    print("Item na mão: {}\n".format(player.mao.nome))

                itemsCommand = escolhasUser(["ver os itens","retirar um item","guardar um item","dropar um item","item na mão"])

                #Ver os itens:
                if itemsCommand == 1:
                    player.mochila.mostrar()
                    player.cinto.mostrar()

                #Retirar um item:
                elif itemsCommand == 2:
                    
                    cancelar = False
                    if player.mao != None:
                        print("Você já está com um item na mão")
                        print("O que fazer com ele?")
                        maoOcupadaCommand = escolhasUser(["dropar","cancelar"])
                        if maoOcupadaCommand == 1:
                            player.mao = None
                        else:
                            cancelar = True
           
                    if not cancelar:
                        retirarItemCommand = escolhasUser(["mochila","cinto","cancelar"])
                        
                        if retirarItemCommand == 3:
                            pass
                        elif retirarItemCommand == 1:
                            player.mao = player.mochila.retirar()
                        else:
                            player.mao = player.cinto.retirar()
                
                #Guardar um item:
                elif itemsCommand == 3:
                    
                    cancelar = False
                    if player.mao == None:
                        print("Você não possui item na mão")
                        cancelar = True

                    if not cancelar:
                        guardarItemCommand = escolhasUser(["mochila","cinto","cancelar"])

                        itemGuardar = player.mao
                        if guardarItemCommand == 3:
                            itemGuardar = None
                            pass
                        elif guardarItemCommand == 1:
                            player.mao = player.mochila.guardar(itemGuardar)
                        else:
                            player.mao = player.cinto.guardar(itemGuardar)

                #Dropar um item:
                elif itemsCommand == 4:

                    droparItemCommand = escolhasUser(["mochila","cinto","cancelar"])

                    if droparItemCommand == 3:
                        pass
                    elif droparItemCommand == 1:
                        player.mochila.retirar()
                    else:
                        player.cinto.retirar()

                #Gerenciar item na mão:
                else:
                    
                    cancelar = False
                    if player.mao == None:
                        print("Você não possui item na mão")
                        cancelar = True

                    if not cancelar:
                        
                        if type(player.mao) == Potion:
                            itemMaoCommand = escolhasUser(["beber","ver descrição","dropar","cancelar"])

                            if itemMaoCommand == 4:
                                pass
                            elif itemMaoCommand == 1:
                                potion = player.mao
                                player.mao = beberPocao(player, potion)
                            elif itemMaoCommand == 2:
                                print(player.mao.descricao)
                            elif itemMaoCommand == 3:
                                player.mao = None

                        elif type(player.mao) == Arma:
                            itemMaoCommand = escolhasUser(["definir como arma principal","dropar","cancelar"])

                            if itemMaoCommand == 3:
                                pass
                            elif itemMaoCommand == 1:
                                armaPrincipal = player.mao
                                player.mao = player.armaPrincipal
                                player.armaPrincipal = armaPrincipal
                            else:
                                player.mao = None

            #Consumir uma poção:
            elif mainCommand == 3:
                
                if type(player.mochila.itemTopo) == Potion:
                    print("Mochila:")
                    print("  {}".format(player.mochila.itemTopo.nome))

                print("\nCinto:")
                for i in range(5):
                    print("  Slot {}".format(i+1))
                    for j in range(player.cinto.qtdItensSlots[i]):
                        if type(player.cinto.matrizCinto[i][j]) == Potion:
                            print("   {}".format(player.cinto.matrizCinto[i][j].nome))

                nomePotion = input("\nDigite o nome da poção: ")

                potionBeber = None

                if type(player.mochila.itemTopo) == Potion:
                    if nomePotion == player.mochila.itemTopo.nome:
                        potionBeber = player.mochila.pilhaMochila.pop()
                        player.mochila.itemTopo = player.mochila.pilhaMochila[-1]
                        player.mochila.qtdItens -= 1
                        beberPocao(player,potionBeber)

                if potionBeber == None:

                    sair = False

                    for i in range(5):

                        for j in range(len(player.cinto.matrizCinto[i])):

                            if type(player.cinto.matrizCinto[i][j]) == Potion:
                                if nomePotion == player.cinto.matrizCinto[i][j].nome:
                                    potionBeber = player.cinto.matrizCinto[i].pop(j)
                                    player.cinto.cargaAtualSlot[i] -= 1
                                    player.cinto.qtdItensSlots[i] -= 1
                                    beberPocao(player,potionBeber)
                                    sair = True

                        if sair:
                            break

                if potionBeber == None:
                    print("*Poção não encontrada*")

            #Ver status
            else:
                statusCommand = escolhasUser(["ver status","ver geral"])

                if statusCommand == 1:
                    player.status()
                else:
                    player.overview()

#Iniciar combate contra um inimigo:
def combate(player: Player, alvo: Inimigo) -> bool:
    
    print("\n*Um {} apareceu*".format(alvo.nome))

    player.inCombate = True
    turnoPlayer = True
    acaoSkill = True

    while True:

        if turnoPlayer:

            acaoPotion = True

            while turnoPlayer:

                print("*Seu turno*")

                opcoes = ["atacar","utilizar uma poção","utilizar skill"]
                if not acaoPotion:
                    opcoes.remove("utilizar uma poção")
                if not acaoSkill:
                    opcoes.remove("utilizar skill")

                combateCommand = escolhasUser(opcoes)

                if not acaoPotion and acaoSkill and combateCommand == 2:
                    combateCommand = 3

                if combateCommand == 1:

                    danoPlayer = player.atacar()
                    defesaInimigo = alvo.defender()
                    resultado = danoPlayer - defesaInimigo
                    if resultado < 0:
                        resultado = 0

                    alvo.vidaAtual -= resultado
                    if alvo.vidaAtual <= 0:
                        alvo.vidaAtual = 0
                        alvo.morto = True

                    print("*Você infingiu {} de dano*".format(resultado))

                    if alvo.morto:
                        print("Você derrotou {}".format(alvo.nome))
                    else:    
                        print("Vida do {}: {}/{}".format(alvo.nome, alvo.vidaAtual, alvo.vidaMaxima))

                    player.danoExtra = 0
                    player.lancesExtraDano = 0
                    turnoPlayer = False
                
                elif combateCommand == 2:

                    print("\nCinto:")
                    for i in range(5):
                        print("  Slot {}".format(i+1))
                        for j in range(player.cinto.qtdItensSlots[i]):
                            if type(player.cinto.matrizCinto[i][j]) == Potion:
                                print("   {}".format(player.cinto.matrizCinto[i][j].nome))

                    nomePotion = input("\nDigite o nome da poção: ")

                    potionBeber = None
                    sair = False

                    for i in range(5):

                            for j in range(len(player.cinto.matrizCinto[i])):

                                if type(player.cinto.matrizCinto[i][j]) == Potion:
                                    if nomePotion == player.cinto.matrizCinto[i][j].nome:
                                        potionBeber = player.cinto.matrizCinto[i].pop(j)
                                        player.cinto.cargaAtualSlot[i] -= 1
                                        player.cinto.qtdItensSlots[i] -= 1
                                        beberPocao(player,potionBeber)
                                        acaoPotion = False
                                        sair = True

                            if sair:
                                break

                    if potionBeber == None:
                        print("*Poção não encontrada*")

                elif combateCommand == 3:
                    player.skill(player,alvo)
                    acaoSkill = False

        else:
            
            danoAlvo = alvo.atacar()
            defesaPlayer = player.defender()
            resultado = danoAlvo - defesaPlayer
            if resultado < 0:
                resultado = 0

            player.vidaAtual -= resultado

            if player.vidaAtual <= 0:
                player.vidaAtual = 0
                player.morto = True

            print("*Você recebeu {} de dano*".format(resultado))

            if player.morto:
                print("Você morreu")
            else:
                print("Sua vida: {}/{}".format(player.vidaAtual, player.vidaMaxima))

            player.lancesExtraDefesa = 0
            player.defesaExtra = 0
            turnoPlayer = True

        if player.morto or alvo.morto:
            player.inCombate = False
            return player.morto

#Quando o player precisar receber recompensas:
def abrirBau(player: Player, itens: list[(Arma | Potion)]) -> None:

    print("\n*Você achou um báu*")

    for item in itens:

        print("*Você recebeu {}*".format(item.nome))

        opcoes = ["guardar na mochila","guardar no cinto","dropar"]
        if type(item) == Potion:
            opcoes.append("beber")

        novoItemCommand = escolhasUser(opcoes)

        if novoItemCommand == 1:
            player.mochila.guardar(item)

        elif novoItemCommand == 2:
            cheio = player.cinto.guardar(item)

            if cheio != None:

                opcoes2 = ["guardar na mochila","dropar"]
                if type(item) == Potion:
                    opcoes2.append("beber")

                cintoCheioCommand = escolhasUser(opcoes2)

                if cintoCheioCommand == 1:
                    player.mochila.guardar(item)
                elif cintoCheioCommand == 2:
                    item = None
                elif cintoCheioCommand == 3:
                    beberPocao(player,item)

        elif novoItemCommand == 3:
            item = None

        elif novoItemCommand == 4:
            beberPocao(player,item)
    
    print(" ")

#Utilizar uma poção:
def beberPocao(player: Player, potion: Potion) -> None:

    for efeito in potion.efeitos:
        efeito(player)
        
    return None