from GameObjects import *
from GerenTerm import pause

def floresta(player: Player) -> int:

    print('''Você se encontra a alguns metros da estrada principal. 
    Ao seu redor, apenas o som de um riacho distante,
    mas você está certo de estar no caminho correto''')

    pause()

    #option (seguir em frente ou não)

    #if (comando==y):
        #print('''Nada fora do comum até onde você pode ver. Porém, 
        #mais alguns metros e você nota uma pequena fogueira.
        #Você se arrisca um pouco, aproximando-se calmamente 
        #em busca de sinais de companhia''')
    #else:
       # print('''Você se mantém na posição atual. Prestando atenção na floresta. 
       # Você está certo de que sente um calafrio daqueles que te falam que algo o observa''')


    #combat

    #if (player_hp==0)
        #print('Fim de jogo')
    #else 
       # print('''Após o leve confronto, você fica cara a cara com seu agressor já derrotado.
        #São poucos os relatos de goblins perambulando essa região, então é justo que você
       # esteja se perguntando se é apenas uma quebra de rotina ou algo mais.''')

    print('''Mesmo estranhando um pouco, você continua seu caminho. 
    Coincidência ou não, você ainda tem um objetivo para seguir''')
    print('''Quase uma hora de viagem depois, você começa a notar uma mudança no ambiente.
    A floresta começa a se tornar mais fechada, e as árvores mais retorcidas, e aos poucos,
    você se vê forçado a parar frente a uma parede de vinhas rígidas e duras como madeira''')

    while True:

        while True:
            comando = input("'E' para escalar ou 'C' para cortar")
            if comando == 'E' or 'C': break
            print("Escolha uma opção válida")

        if(comando=='C' and player.atributos["STR"]>=13):
            print('''Apesar dessas vinhas serem verdadeiramente resistentes, 
            você é capaz de tirá-las do caminho''')
            break
        else:
            print('''Mesmo colocando toda a sua força na tarefa, você se convence,
            não há como arrancar as vinhas''')
        
        if(comando=='E' and player.atributos["DEX"]>=13):
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
        #if(player hp == 0)
            #print("fim de jogo")
            #else
                #print('''Após o estranho combate, você nota por entre os ossos do monge um brilho
                # escarlate. Tirando algumas costelas do caminho, você toma para si um cristal 
                # quente''')
    
    print('''Você passa alguns instantes inspecionando o artfato até decidir
    abandonar a tumba. Olhando ao redor, você segue na direção de onde acredita que 
    o esqueleto veio, e encontra uma passagem antes secreta que sai ao topo da tumba.
    Com seu prêmio em mãos, você deixa aquele pedaço de história para trás''')

    #option(cidade ou estrada)

    return 1

def cidade(player: Player) -> int:

    print('''Horas de caminhada e você finalmente alcança a cidade. Seu ponto de partida e,
    principalmente, seu local de descanso. As casas de madeira estão mais destacadas do que
    o de costume, no entanto.''')

    #option(falar com npc ou ir para casa)

    #if(falar com npc)
        #print('''Você se aproxima do sujeito mais próximo. Um senhor de idade que parece estar 
        #ajudando em algo. Ele comenta:''')
        #print('''Estamos nos preparando para o festival do Sol, é estranho como o tempo passa 
        #rápido, não acha? Eu também me peguei surpreso com os preparativos.''')
    #else
        #print('''Você escolheu deixar para descobrir depois. Você prefere avaliar o que 
        #encontrou e anotar as descobertas''')

    print('''Você entra em uma estalagem de longa data. O taverneiro te cumprimenta com discrição 
    enquanto serve alguns clientes. Seu quarto está da mesma maneira de sempre, e você parte
    para fazer seus comentários sobre sua pequena aventura... até se lembrar do cristal.
    Você se recorda de um apreciador de joias local, um estudioso, acima de tudo. Ele talvez possa 
    te elucidar um pouco.''')

    #option(ir agora ou mais tarde)
    #if(ir agora)
        #print('''Quanto mais cedo você cuidar disso, mais rápido ira sanar sua curiosidade''')
        #else
            #print('''O apreciador de joias não ira desaparecer se você não for imediatamente''')

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

    #option(inspecionar a estátua ou chamar por ajuda)

    #if(inspecionar)
        #print('''Observando cuidadosamente a estátua de gelo, você se atreve a dizer que o próprio senhor
        # tornou-se uno com o gelo que o envolve. Isso está fora da sua alçada, e você não consegue pensar em
        # nada para ajudá-lo. Você também encontra um mapa levando a uma cabana fora da cidade, não tão longe 
        # da tumba que havia encontrado mais cedo.''')  
    #else
        #print('''Antes de sair da joalheria, você encontra um mapa para uma cabana próxima,
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
        #if(player hp == 0)
            #print("fim de jogo")
        #else
            #print('''O animal te parece um lobo das neves, um dos maiores que você poderia ver. Mas o que ele 
            # faz ali é a maior dúvida. No inverno, claramente haveria neve, mas seu lar não é uma terra gelada
            # para servir de habitat para uma espécie como aquela.''')

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

    return -1

def deserto(player: Player) -> None:

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

    #option (apenas continuar ou observar)
        #if(observar)
            #print('''''')
        #else
        #break

    print('''Vocês três continuam sua viagem até encontrarem algumas ruínas. Algumas são semelhantes aos da tumba, mas 
    outros te são desconhecidos. No centro de tudo, uma pequena tenda ''')

    pass

def deserto(player: Player) -> int:
    
    return 1

def ultimaCidade(player: Player) -> int:
    
    return 1

levels = [floresta, tumba, cidade, casaBruxa, deserto, ultimaCidade]