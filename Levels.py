from GameObjects import *
  
    
def floresta(player: Player, inimigos: list[Inimigo], itens: list[Arma | Potion]) -> None:

    print('''Você se encontra a alguns metros da estrada principal. 
    Ao seu redor, apenas o som de um riacho distante,
    mas você está certo de estar no caminho correto''')

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

    #option (cortar ou escalar)

    #if(comando==cortar && player_stats[STR]>=13):
       # print('''Apesar dessas vinhas serem verdadeiramente resistentes, 
        #você é capaz de tirá-las do caminho''')
    #else
        #print('''Mesmo colocando toda a sua força na tarefa, você se convence,
       # não há como arrancar as vinhas''')
    
    #if(comando==pular && player_stats[DEX]>=13):
        #print('''Mesmo fortemente entrelaçadas, as vinhas possuem espaços
       #suficientes para que você escale a parede com segurança''')
    #else
        #print('''Você consegue notar uma forma de escalar a parede, mas você cai 
       # em todas as suas tentativas de subi-la''')


    print ('''Com certo esforço, você se vê livre em uma nova parte da floresta, quase que
    seguindo uma trilha construída há eras. Você confirma isso alguns metros a frente, 
    descendo uma pequena clareira que parece um acampamento abandonado, adentrando
    ainda mais por entre as árvores, até que você se vê no centro de um morro de pedras, sem luz
    ou calor. Acendendo uma tocha, você segue uma trilha de tijolos de pedra, afetados
    pela erosão de pequenos corregos abaixo de seus pés, até encontrar o que tem certeza 
    de ser seu objetivo: iluminada por alguns raios de Sol que atravessam fissuras do teto pedregoso, 
    uma tumba perdida.''')
    pass


def tumba(player: Player, inimigos: list[Inimigo], itens: list[Arma | Potion]) -> None:
    
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

    pass

def cidade(player: Player, inimigos: list[Inimigo], itens: list[Arma | Potion]) -> None:

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

    print('''Caminhando por entre as ruas da cidade, você se mais pesado do que o comum. Ainda não é tarde
    o bastante para anoitecer, mas está mais frio do que o de costume por ali. Olhando para o céu, você 
    diversas aves voando ao sul, como se estivessem migrando.''')

    


    pass

def estrada(player: Player, inimigos: list[Inimigo], itens: list[Arma | Potion]) -> None:

    pass

def casaBruxa(player: Player, inimigos: list[Inimigo], itens: list[Arma | Potion]) -> None:
    pass

def deserto(player: Player, inimigos: list[Inimigo], itens: list[Arma | Potion]) -> None:
    pass

def ultimaCidade(player: Player, inimigos: list[Inimigo], itens: list[Arma | Potion]) -> None:
    pass

levels = [floresta, tumba, cidade, estrada, casaBruxa, deserto, ultimaCidade]

