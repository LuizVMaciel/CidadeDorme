while True:
    #Set da lista e inicialização do programa
    jogadores = []
    print('Bem vindo ao Cidade Dorme')
    quantidadeInicialJogadores = int(input('Quantas pessoas irão jogar? '))
    #Sistema de registro de jogadores
    if (quantidadeInicialJogadores > 0):
        jogadores.append(input('digite o seu nome: '))
        quantidadeInicialJogadores -= 1
        while(quantidadeInicialJogadores > 0):
            quantidadeJogadoresJogando = len(jogadores)
            jogadores.append(input(f'digite o nome do jogador {quantidadeJogadoresJogando + 1}: '))
            quantidadeInicialJogadores -= 1
        print('todos jogadores foram registrados!')
        break
    #Validação de que o numero de pessoas seja positivo
    else:
        print('Digite um número válido')