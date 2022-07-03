from GameObjects import *
from Eventos import *
from ferramentas import pause

def floresta(player: Player) -> int:

    print('''Você se encontra a alguns metros da estrada principal. 
    Ao seu redor, apenas o som de um riacho distante,
    mas você está certo de estar no caminho correto''')

    abrirBau(player,[pedra,pedra,pedra,pedra,pocaoCura,pocaoEmbaralhar,pocaoCura,pedra,pedra])

    andando(player)

    comando = escolhasUser(["seguir em frente","observar um pouco"])
    
    if (comando==1):
        print('''Nada fora do comum até onde você pode ver. Porém, 
        mais alguns metros e você nota uma pequena fogueira.
        Você se arrisca um pouco, aproximando-se calmamente 
        em busca de sinais de companhia''')
    elif(comando==2):
        print('''Você se mantém na posição atual. Prestando atenção na floresta. 
        Você está certo de que sente um calafrio daqueles que te falam que algo o observa''')

    morto = combate(player, goblin)
    if morto: return 0
    
    print('''Após o leve confronto, você fica cara a cara com seu agressor já derrotado.
    São poucos os relatos de goblins perambulando essa região, então é justo que você
    esteja se perguntando se é apenas uma quebra de rotina ou algo mais.''')

    print('''Mesmo estranhando um pouco, você continua seu caminho. Coincidência ou não, 
    você ainda tem um objetivo para seguir''')

    print('''Quase uma hora de viagem depois, você começa a notar uma mudança no ambiente.
    A floresta começa a se tornar mais fechada, e as árvores mais retorcidas, e aos poucos,
    você se vê forçado a parar frente a uma parede de vinhas rígidas e duras como madeira''')

    while True:

        comando = escolhasUser(["cortar","escalar"])

        if comando==1 and player.atributos["STR"]>=13:
            print('''Apesar dessas vinhas serem verdadeiramente resistentes, 
            você é capaz de tirá-las do caminho''')
            break
        else:
            print('''Mesmo colocando toda a sua força na tarefa, você se convence,
            não há como arrancar as vinhas''')
        
        if comando==2 and player.atributos["DEX"]>=13:
            print('''Mesmo fortemente entrelaçadas, as vinhas possuem espaços
            suficientes para que você escale a parede com segurança''')
            break
        else:
            print('''Você consegue notar uma forma de escalar a parede, mas você cai 
            em todas as suas tentativas de subi-la''')

    print ('''Com certo esforço, você se vê livre em uma nova parte da floresta, quase que
    seguindo uma trilha construída há eras. Você confirma isso alguns metros a frente, 
    descendo uma pequena clareira que parece um acampamento abandonado, adentrando
    ainda mais por entre as árvores, até que você se vê no centro de um morro de pedras, sem luz
    ou calor. Acendendo uma tocha, você segue uma trilha de tijolos de pedra, afetados
    pela erosão de pequenos corregos abaixo de seus pés, até encontrar o que tem certeza 
    de ser seu objetivo: iluminada por alguns raios de Sol que atravessam fissuras do teto pedregoso, 
    uma tumba perdida.''')

    return 1

def tumba(player: Player) -> int:
    
    print('''Você se impressiona com a vista a frente. Mesmo que tenha duvidado um pouco,
    você chegou. A trilha de pedra, coberta por anos de vegetação, te guia diretamente 
    para a construição em forma de pirâmide com uma entrada próxima ao chão. É impossível 
    não notar os esqueletos espalhados, todos com vestimentas simples, como se fossem oradores.''')

    print('''Sem se amedrontar, você empunha sua tocha e parte para desbravar a tumba. 
    A primeira vista, era um lugar desolado, frio como todo o resto, e, estranhamente, se,
    armadilhas para invasores. No final do primeiro corredor, no entanto, você tem um pressentimento:
    talvez este lugar seja um labirinto.''')


    #option(observar o chão)
    #if (option=observar)
        #print ('''você nota 1 esqueleto a esquerda, e 2 a direita''')
    
    #caminho certo = 1
    #caminho errado = 2

    #option (direita ou esquerda)
    #if(direita)
        #print('''Graças a sua tocha, você percebe que o caminho leva a dois caminhos sem saída.
        # você retorna ao ponto de partida''')
    #else
        #print('''Você aparenta ter começado corretamente''')

    

    #do while (contador certo<7)
        #puzzle do labirinto
        #+contador de direções certas
        #+contador de direções erradas

        #option(estudar o lugar ou observar)
        #if(comando==estudar && player_stats[INT]>=13)
            #print('''Parando por alguns minutos para estudar o lugar, você compreende:
            # os caminhos certos são aqueles que possuem um único esqueleto em sua direção.
            # A partir de agora, você sabe por onde ir''')
        #else
            #print('''Apesar de se concentrar o máximo que pode, nada desse lugar te parece 
            # dar uma luz no caminho certo. Sinceramente, todo o lugar parece igual para você''')
        
        #if(comando==observar && player_stats[WIS]>=13)
            #print('''Com calma e atenção, você consegue notar as escrituras remanescentes nas
            # paredes dos corredores. Elas te guiam pelo lugar''')
            #if (player_class[id]==clerigo)
                #print('''Você consegue ler alguns detalhes das paredes: essa tumba foi construída 
                # eras atrás em homenagem ao Sol e sua vitória sobre o Inverno, mas, anos depois,
                # o lugar seria deixado por todos menos os monges que se instalaram. Você agora sabe
                # quem são os donos dos esqueletos''')
        #else
            #print('''Você tem certeza que vai se perder, mas apenas isso''')
        
        #if (caminho==1)
            #contador certo+=1
            #else
                #contador errado+=1
        
        #if (contador errado==3)
            #combat
        
    print('''Depois de um longo tempo caminhando por entre estes velhos corredores,
    você finalmente chega numa sala diferente. Parece o centro da tumba, numa área
    ritualística com um pedestal em seu centro, vazio ao que parece. Você caminha 
    em sua direção, e sente um calafrio. Você olha ao redor e nota estar sendo 
    observado: um esqueleto de monge retornado a vida''')

    #combat
    
    print('''Após o estranho combate, você nota por entre os ossos do monge um brilho
    escarlate. Tirando algumas costelas do caminho, você toma para si um cristal 
    quente''')
    
    print('''Você passa alguns instantes inspecionando o artfato até decidir
    abandonar a tumba. Olhando ao redor, você segue na direção de onde acredita que 
    o esqueleto veio, e encontra uma passagem antes secreta que sai ao topo da tumba.
    Com seu prêmio em mãos, você deixa aquele pedaço de história para trás''')

    return 1

def cidade(player: Player) -> int:

    print('''Horas de caminhada e você finalmente alcança a cidade. Seu ponto de partida e,
    principalmente, seu local de descanso. As casas de madeira estão mais destacadas do que
    o de costume, no entanto.''')

    comando=input("Falar com alguém próximo ou ir para seu lar temporário?(F/L")
    while(comando==False):
        if(comando=='F'):
            print('''Você se aproxima do sujeito mais próximo. Um senhor de idade que parece estar 
            ajudando em algo. Ele comenta:''')
            print('''Estamos nos preparando para o festival do Sol, é estranho como o tempo passa 
            rápido, não acha? Eu também me peguei surpreso com os preparativos.''')
        elif(comando=='L'):
            print('''Você escolheu deixar para descobrir depois. Você prefere avaliar o que 
            encontrou e anotar as descobertas''')
        else:
            print("Selecione uma opção válida.")

    print('''Você entra em uma estalagem de longa data. O taverneiro te cumprimenta com discrição 
    enquanto serve alguns clientes. Seu quarto está da mesma maneira de sempre, e você parte
    para fazer seus comentários sobre sua pequena aventura... até se lembrar do cristal.
    Você se recorda de um apreciador de joias local, um estudioso, acima de tudo. Ele talvez possa 
    te elucidar um pouco.''')

    print('''Caminhando por entre as ruas da cidade, você se sente mais pesado do que o comum. Ainda não 
    é tarde o bastante para anoitecer, mas está mais frio do que o de costume por ali. Olhando para o céu, 
    você diversas aves voando ao sul, como se estivessem migrando. Mais uma coincidência.''')
   
    print('''Você chega ao apreciador de joias e sua humilde loja. Uma vitrine apresenta algumas belas
    joias para possíveis, compradores, e por dentro você vê alguns outros itens de colecionador, como relógios
    caros e derivados''')

    print('''Você apresenta o cristal de fogo ao senhor, e ele fica estupefato. Após alguns segundos de apreciação,
    ele pede sua licença e vai para o quarto dos fundos. Você espera calmamente, mas ele se demora demais, e 
    sua impaciência vem a tona. Mas não era de se esperar a vista que encontrara: enquanto se aproxima, sentindo
    um frio inexplicável, você vê uma estátua de gelo no lugar do senhor que lhe atendera.''')

    comando = escolhasUser(["inspecionar a estátua","chamar por ajuda"])
   
    if(comando==1):
        print('''Observando cuidadosamente a estátua de gelo, você se atreve a dizer que o próprio senhor
        # tornou-se uno com o gelo que o envolve. Isso está fora da sua alçada, e você não consegue pensar em
        # nada para ajudá-lo. Você também encontra um mapa levando a uma cabana fora da cidade, não tão longe 
        # da tumba que havia encontrado mais cedo.''')  
    elif(comando==2):
        print('''Antes de sair da joalheria, você encontra um mapa para uma cabana próxima,
        # jogado numa mesa próxima ao senhor congelado. Você corre para fora da joalheria, 
        # clamando pelos guardas mais próximos. As próximas horas são totalmente voltadas para 
        # o acontecimento.''')   

    print('''Você sabe que os guardas vão acobertar a situação até que o festival tenha terminado. Depois de 
    explicar tudo o que você sabia, eles deixam você voltar para a taverna. Nenhum de vocês tem ideia de como
    aquilo aconteceu, mas já não está em suas mãos... ou talvez esteja, considerando o cristal que você
    escondeu de seus relatos.''')

    print('''Você retorna para a taverna com a mente matutando novas ideias. Nenhuma criatura que fosse capaz
    de tal coisa vem a mente. Feitiçaria é muito barulhenta e as coisas aconteceram sem que você percebesse
    até ser tarde demais. Ainda se indagando sobre o novo mistério, você nem nota cair no sono.''')

    print('''Você acorda diversas vezes durante a noite. Várias vezes você olha pela janela para ver a lua brilhando
    plenamente. Até que não havia mais lua. Você acorda uma última vez, completamente descansado mas ainda na 
    escuridão da noite. Não há ninguém nas ruas, mas as luzes estão acessas. Você ainda não sabia disso,
    mas nos próximos dias todos perceberiam: o Sol não estava mais nascendo.''')

    return 1

def casaBruxa(player: Player) -> int:

    print('''Dias pós dia, o Sol continuou não aparecendo. Os dias ficavam mais gelados a cada hora. A única coisa
    que não perdia calor era o cristal que você guarda consigo. Sua única pista era a cabana na floresta, então
    é para lá que você vai.''')

    print('''Você anda apenas com uma tocha em mãos. A Lua ainda não estava presente para iluminar o caminho.
    As folhas são as únicas coisas que fazem som além das suas pegadas enquanto os ventos te forçam a se lembrar
    das condições dos novos tempos.''')

    print('''Quando você sentia estar completamente sozinho, você escuta arbustos se agitando por perto. 
    Você olha para a direção dos sons, e uma fera de pelos brancos aparece, avançando em sua direção.''')

    #combat
        
    print('''Você abandona o animal caído e continua seu caminho até encontrar a cabana mostrada em seu mapa. 
    É uma casa humilde de madeira. Você sente o cheiro de algo sendo preparado do lado de dentro. Você bate
    a porta, e uma mulher com por volta dos seus 30 anos o atende.''')

    print('''Você explica a situação para mulher, que se apresentou como Aurélia, e ela admite ter das 
    mesmas preocupações. Você deixa de comentar sobre o cristal por não saber se pode confiar nela. 
    Sua conversa então chega ao ponto principal: ela tem uma ideia de por onde começar a resolver o problema
    da falta de Sol, e te convida para se juntar a ela. Você concorda por não ter outra escolha, mas promete
    a si mesmo tomar cuidado.''')

    print('''Aurelia então prepara algumas coisas, e quando você se dá conta, ela te coloca um colar dourado com
    forma de Sol. Você fecha seus olhos por instantes, e se vÊ numa paisagem que nunca antes havia visto: um
    deserto congelante.''')

    return 1

def deserto(player: Player) -> int:

    print('''Aurelia se diverte com seu susto enquanto te passa algumas roupas compridas para te proteger do frio.
    Ela pede perdão pela mudança repentina de cenário, mas afirma estar com certa pressa para encontrar uma pessoa.
    Ela também te pede para lidar com um encontro inesperado, apontando para o horizonte. Você demora alguns segundos
    para notar, mas seus olhos se acostumam e você vê um escorpião gigante indo até vocês.''')

    #combat

    print('''Lutar num deserto já é uma coisa que poucos gostariam de fazer, mas você prefere mais o calor
    da batalha do que congelar ali mesmo. 
    Aurelia agradece pelos seus esforços e garante que ira te guiar por caminhos mais seguros dali para frente.
    Você está um pouco mais desconfiado, mas tem certeza que poderá lidar com algum problema futuro se ela for a
    causa.''')

    print('''Vocês dois caminham pelo que parecem dias. Você até já aprendeu a olhar o tempo pelo movimento da lua.
    Aurelia comenta que é uma praticante de magia há vários anos, mas que a falta do Sol vem prejudicando seus 
    dons. Trazer vocês e voltar para casa são as duas últimas coisas que ela tem certeza de ser capaz.''')

    print('''Tempos depois, vocês param em um pequeno oasis quase que congelado. O topo das árvores já está ficando 
    coberto por gelo, e a água parece estar a minutos de congelar por completo. Do outro lado do pequeno lago, você 
    nota uma figura e um camelo caídos. Aurelia é a primeira a ir até lá. Vocês resgatam uma andarilha que se perdeu
    no deserto, e que perdeu seu camelo para o cansaço.''')

    print('''A moça se apresenta como Tamara. Já estava viajando no deserto há mais de dez dias, procurando por
    qualquer novo traço de civilização que pudesse encontrar, e trazer novos contatos ao seu povo. Tudo se complicou
    com o frio dos últimos dias, e agora ela havia perdido seu camelo.''')

    print('''Aurelia não parecia tentada a deixar a jovem moça para trás, e a convidou para acompanhar vocês. 
    Tamara, a primeira vista, não desejava atrapalhar seus assuntos, mas preferiu não continuar sozinha.''')

    print('''Vocês três continuam sua viagem até encontrarem algumas ruínas com diversos desenhos e rostos. Algumas 
    são semelhantes aos da tumba, mas outros te são desconhecidos. No centro de tudo, uma pequena tenda iluminada por 
    uma fogueira, e uma nova figura sentada, olhando para algumas ruínas mais conservadas.''')

    print('''O homem se levanta como se soubesse que vocês haviam chegado. É um senhor em volta de seus 40 anos, 
    vestido como quem está acostumado a viver no calor do deserto. Aurelia pede para que você e Tamara a esperem, e 
    vai ao encontro do sujeito.''')

    print('''Tamara se senta num pedaço de construção caído ao chão, olhando atentamente para os dois afastados.
    De pouco a pouco, você começa a se sentir incomodado com a presença dela, sentindo ímpeto em se afastar.
    Você olha uma última vez em direção a Aurélia, e nota um olha desesperançoso. Ela olha em direção a vocês, e
    esse olhar muda para uma surpresa desagradável.''')
    
    print('''Você ouve uma voz forte do lugar de onde Tamara estava, e fica paralisado no lugar onde está: 
    "Isso é ridículo". A dona de tal voz era de uma jovem mulher branca como a neve em um vestido azul gelo. 
    Seu andar fazia seu corpo tremer. Por longos momentos, você não conseguiu tomar quaisquer atitudes.''')

    print('''Aurelia se colocou frente a frente da nova figura, mas tinha em seu olhar poucas expectativas de fazer
    qualquer coisa. "Mova-se, Primavera", disse a mulher albina, "meus assuntos envolvem Sandman, e apenas ele".''')

    print('''"Com que direito você tenta me dar ordens, Cerulea?", indaga Aurelia, mas o senhor nomeado Sandmand lhe
    deu um leve toque no ombro para encarar ele mesmo a mulher albina. "Faça o que acha que deve fazer, criança."''')

    print('''Foi num piscar de olhos, mas você viu o resultado do que aconteceu com o apreciador de joias uma 
    segunda vez. No lugar daquele senhor, uma estátua de gelo se formou. Você prepara sua arma para se defender, e 
    tem certeza de que Aurelia, ao menos, lutaria ao seu lado.''')

    print('''"Eu lhe dei a chance que preciava para não tentar mexer com o que não devia, mortal. O velho das joias
    devia ter sido aviso o suficiente. Mas estou com um pouco de clemência sobrando para o dia de hoje. Dê-me o cristal
    de fogo que carrega, e não precisará compartilhar do mesmo destino que os outros."''')

    print('''Você volta da paralisia temporária do frio, se perguntando como havia chegado numa situação como essa, e 
    se entreolha com Aurelia, e ela te devolve um olhar confuso. Você volta a olhar para Cerulea e nota: o rosto 
    dela estava em vários dos desenhos das ruínas. Ela foi chamada de Primavera, e a mulher albina era fria como gelo,
    estaria você diante das personificações das estações?''')

    opção = input("Entregar o cristal?(S/N")

    if(opção=='S'):
        print('''Você teme por sua vida agora que a paranoia toma conta dos seus pensamentos. As simples ideias do que
        essa mulher possa ser é o suficiente para fazer suas pernas vacilarem. Você retira o cristal de fogo de sua 
        mochila, e o apresenta a Cerulea. ''')
        
        pause

        print('''Aurelia demonstra que irá fazer algo, mas metade de seu corpo é revestido por gelo em questão de
        segundos. Isso confirma que você nunca teve uma chance.''')



        print('''Cerulea toma o cristal de você, e o olha como um achado raro, até parecendo se esquecer de você por 
        alguns instantes. Você preferia que ela realmente tivesse te esquecido. O frio ao seu redor aumenta de maneira
        assustadora. Seu corpo começa a congelar dos pés até a cabeça.''')



        print('''"Você merece ao menos entender o que é isso", diz Cerulea sem te olhar nos olhos, "eu bem disse que seu
        destino não seria o mesmo dos outros, mas nunca disse que seria misericordioso, ou que seria até mesmo poupado". 
        Ela passa ao seu lado, começando a ir embora das ruínas. "Um traidor não merece minha clemência, mas ser feito
        como um exemplo para ser esquecido? Isso eu lhe concedo, mortal".''')

        print('''O gelo lentamente toma conta. Você sente seu interior gelando por inteiro, e fecha seus olhos para seu fim.
        Aos poucos, você para de pensar.''')


        print('''Final ruim''')
                
    else:
        print('''Mesmo sabendo que suas chances são quase nulas, você se nega a entregar o cristal a ela, o que claramente
        a irrita.''')

        print('''"Então, que você se junte ao apreciador de joias, mortal". Assim que essas palavras terminam, você vê Aurelia sendo
        tomada por gelo, e sente seu corpo gelando rapidamente enquanto Cerulea desaparece de sua visão.''')



        print('''Algo começa a esquentar você. Aos poucos, você recobra a consciência. Seu corpo molhado com o gelo derretido cai em neve.
        Você olha ao redor e tudo está congelado. Não há sinal de Aurelia, mas a estátua de Sandman continua aonde você se recorda.''')

        print('''Você cambalheia em direção a ele, e procura qualquer coisa que te seja um sinal de esperança para escapar daquela 
        situação, mas dificilmente alguém ou algo apareceria para prestar socorro. Você então volta sua atenção para o calor em suas costas.''')

        print('''Você retira o cristal de fogo, brilhando como brasa mas não queimando ao toque. Seu primeiro instinto é tentar descongelar 
        Sandman, e assim você o tenta.''')

        print('''Sua noção de tempo está defasada. A tarefa parece demorar horas para ter algum progresso. Mas você consegue descongelar o 
        senhor insconsciente.''')

        print('''Você garante que ele esteja aquecido, ao mesmo tempo que se pergunta se ele era como Cerulea e, provavelmente, Aurelia. Se for
        o caso, nem tudo estará perdido, ou assim sua expectativa espera. E falando sobre esperar, você se dá o luxo de observar mais atentamente
        os arredores.''')

        print('''O deserto era completamente de neve agora. A tenda havia desaparecido por completo. Algo assim não deveria acontecer tão rápido, 
        e você dúvida que Cerulea se deu o trabalho de deixar o ambiente daquela forma. Isso te faz se perguntar quanto tempo esteve na forma de 
        estátua."Mais de vinte dias", diz um recém desperto Sandman, "em minha ausência, Cerulea congelou as próprias estrelas no lugar, nem mesmo
        a Luz pode abandonar seu lugar de quando fomos congelados. Sim, criança, ela congelou o próprio tempo."''')

        print('''"Eu sou aquele chamado de Senhor das Areias do Tempo, e sei o que está se perguntando agora, então irei direto ao assunto, minha 
        criança: Eonhad, o Verão e seu Sol, os abandonou, decepcionado por sua mortalidade falha. Mas você pode ajudar a trazê-lo de volta. Ajude
        a última cidade a perdurar, e ele se arrependerá por sua ausência. Entendo o que está pensando, mas antes tarde do que nunca, é o que vocês
        dizem. Uma última coisa para guardar na memória: a pessoa certa no lugar errado por fazer toda a diferença do mundo. A humanidade agradece
        seus esforços,''' +player.nome+'''."''')
   
    return 1

def ultimaCidade(player: Player) -> int:

    print('''As areais cobertas por neve se erguem e te cobrem. Você se sente sendo levado com o próprio vento''')

    print('''Você sente pousar. As areias somem aos poucos, e te é revelado a presença de algumas figuras conhecidas: Aurelia, cara-a-cara
    com uma nova pessoa, e Cerulea, tomando a frente de um gigante exército de animais de neve.''')

    print('''"Então, no final de contas, o cristal pode te salvar", diz Cerulea quase com um olhar entediado. Aurelia se aproxima sem tirar os 
    olhos do homem que a encara de volta.''')

    print('''"Não temos tempo para explicações, eu preciso de tempo para me recuperar antes que os animais percam a paciência e avancem por si só".
    Terminando suas palavras, Aurelia coloca umas das mãos no seu ombro, e você se sente revitalizado enquanto ela toma a retagurda. "Por favor, 
    apenas segure Outono, ele pensa que está lutando para me salvar, mas há outras formas para isso."''')

    print('''"Não o conheço, mortal, mas peço para que desista da resistência", diz-lhe o sujeito, mas você não recua. "Eu, ao menos, tentei."''')

    #combat

    print('''Foi a coisa mais inesperada que você teve que fazer. Batalhar com Outono sem o suporte inicial de Aurelia seria impossível, mas mesmo
    que você ainda esteja de pé, reconhece que ele está na vantagem.''')

    print('''"Eu realmente sinto muito", fala Outono com pesar.''')

    print('''"Bela demonstração de vontade, mortal, mas é apenas isso o que você pode fazer", diz Cerulea, mesmo a distância sua voz é clara como 
    cristal."Todos que sobreviverem saberão que lutou com honra, ao invés de se acovardar, mesmo que no final tenha sido derrotado."''')

    print('''Você olha para ela, seus olhos nem ao menos se cruzam. Mesmo que ela diga tais palavras, Cerulea não se importa com sua presença. Você 
    diria até que ela está sendo misericordiosa, até certo ponto. Mas você a deixa sabendo de que você só precisava de tempo.''')

    print('''Dessa vez, ela te olhou nos olhos. Mas antes que dissesse qualquer coisa, Aurelia te puxa para perto, e você sente mais da energia
    que te colocou em condições de combate. "Proteja os olhos", diz ela sem mais explicações. Você o faz.''')

    print('''Pelo canto dos olhos, você vê o impossível: as estrelas e a própria lua começam a se mover, ao ponto de até mesmo cortarem os céus
    como cometas. O brilho cresce até ser quase cegante, mas o mais impressinante é o que veio a seguir.''')

    print('''Um brilho no horizonte, dourado como ouro, começa a subir, aquecendo você pelas costas. Depois de muitos dias, o farol de sua vida 
    começa a retornar. Mais uma vez, a luz do dia começava a nascer. A posição do Sol, recém-nascido, declarava as dez horas da manhã como se fosse
    a primeira vez desde o começo dos tempos. Seus olhos se acostumam com a claridade aos poucos, e uma mão pousa em seu ombro.''')

    print('''"Me perdoe por deixa-los passarem por tudo isso, eu retornei para tomar responsabilidade pelo meu erro", diz-lhe um sujeito de cabelos 
    dourados, deixando o seu lado e passando por Outono com um olhar amigável, mas entristecido.''')

    print('''"Por que agora, Eonhad?", indagou Cerulea, "O mundo está quase acabando, muitos se perderam, e somente agora você decide tomar uma atitude?"
    "Eu demorei demais, eu sei. Mas ficar parado não seria melhor", responde Verão. "Vou carregar comigo o peso das vidas que você congelou, mas o 
    farei sem pensar duas vezes, ao invés de deixar está última cidade ser congelada."''')

    print('''Você observa Eonhad levantar uma das mãos, e sente Aurelia cobrindo seus olhos. Mesmo não vendo, você sente o calor do Sol, mais forte e 
    focado, aquecendo seus arredores até que a neve sob seus pés derreta. Você abre seus olhos novamente, e vê que praticamente todo o exército de 
    Cerulea havia sido derretido, deixando a sozinha na linha de frente. É impressionante a falta de expressão que ela tem, mas é ainda mais 
    surpreendente como ela não tira os olhos de Verão. ''')

    print('''"A partir deste dia, eu declaro que esta guerra acabou.", diz Eonhad, em alto e bom som, "Uma vez mais, os mortais estão sob minha proteção."''')

    print('''"Eles te afastaram uma vez por conta da escuridão de sua existência, por não apreciarem o dom da vida que você e Privamera garantiam. 
    Matando e roubando seus iguais, quebrando o trabalho da própria Mãe Natureza por sua ganância e sua.... filosofia dos mortais como o centro de 
    tudo. Como você garante que isso não ocorrerá de novo?"''')

    print('''"Eu não posso, mas se a vida fosse algo a ser controlado, não seria entregue a eles, de um jeito ou de outro. Você pode não concordar com isso,
    mas essa é a forma que as coisas serão."''')

    print('''"Então, isso é apenas um atraso do inevitável. Eu irei recuar, por hora. Mas tenha isso em mente, Eonhad, o dia chegará em que você
    não será suficiente para impedir minhas conquistas, e você próprio não estará fora do alcance delas". E simplesmente assim, Cerulea desaparece com 
    uma leve brisa gelada, deixando apenas o calor do Sol restar naquele lugar.''')

    print('''As palavras de Sandman se provaram verdadeiras, mas Cerulea estava certa, muitos foram perdidos. Vocês sabem apenas da condição da cidade que
    estão protegendo. Só o tempo dirá se outros povos também resistiram. Sobreviver não se baseia na vitória, e você tem certeza de não se esquecerdisso. 
    Pelo menos, pela primeira vez, os próprios senhores do mundo estão do seu lado.''')

    print('''O cristal de fogo ficou sob os cuidados de Aurelia. Outono, agora que Aurelia, que você descobre ser sua esposa, está a salvo, se manteve ao 
    lado dela e de Eonhad. Por vezes, Sandman atende as suas dúvidas enquanto você passou a viver para ajudar a reconstruir o mundo, mesmo que eles não 
    saibam que fora você uma das pessoas que ajudou a salvar o mundo. Ser a pessoa certa no lugar errado fez a diferença no mundo, mas não te fez ser
    conhecido por ele.''')

    print('''Todos os dias, sempre que você sente frio, você pensa nas palavras de Cerulea. Não há como saber se vocês se reencontrarão nessa vida. Mas você
    a teme mesmo assim. Isso te dá forças para continuar, ironicamente, pelo menos tentar o máximo possível para ajudar a atrasar o dia da promessa dela.''')

    print('''Fim de jogo. Final Verdadeiro.''')

    return 1

levels = [floresta, tumba, cidade, casaBruxa, deserto, ultimaCidade]