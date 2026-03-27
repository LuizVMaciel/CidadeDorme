import random
while True:
    #Set da lista e inicialização do programa
    jogadores = []
    print('Bem vindo ao Cidade Dorme')
    quantidadeInicialJogadores = int(input('Quantas pessoas irão jogar? '))
    #Validação de que o numero de jogadores seja positivo e maior que dois
    if (quantidadeInicialJogadores > 2):
        #Sistema de registro de jogadores
        jogadores.append(input('digite o seu nome: '))
        quantidadeInicialJogadores -= 1
        while(quantidadeInicialJogadores > 0):
            quantidadeJogadoresJogando = len(jogadores)
            jogadores.append(input(f'digite o nome do jogador {quantidadeJogadoresJogando + 1}: '))
            quantidadeInicialJogadores -= 1
        print('todos jogadores foram registrados!')
        #atribuição de classes/cargos para os jogadores 
        cidadaos = jogadores.copy()
        assassino = random.choice(cidadaos)
        cidadaos.remove(assassino)
        detetive = random.choice(cidadaos)
        cidadaos.remove(detetive)
        anjo = random.choice(cidadaos)
        cidadaos.remove(anjo)
        break
    else:
        print('Digite um número válido')