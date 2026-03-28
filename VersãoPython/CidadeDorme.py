import random
from collections import Counter
while True:
    #Set da lista e inicialização do programa
    jogadores = []
    print('Bem vindo ao Cidade Dorme!')
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
        jogadoresExcetoAssassino = jogadores.copy()
        assassino = random.choice(cidadaos)
        cidadaos.remove(assassino)
        jogadoresExcetoAssassino.remove(assassino)
        detetive = random.choice(cidadaos)
        cidadaos.remove(detetive)
        anjo = random.choice(cidadaos)
        cidadaos.remove(anjo)
        print('classes atribuídas!')
        #programação das rodadas
        while((len(jogadoresExcetoAssassino) > 1) and (assassino in jogadores)):
            #programação noite (jogadores exercem suas classes)
            print('A cidade Dorme.')
            jogadoresNaPartida = len(jogadores)
            jogadorTurno = 0
            while(jogadorTurno < jogadoresNaPartida):
                if(jogadores[jogadorTurno] in cidadaos):
                    input(f'vez de {jogadores[jogadorTurno]}, digite "ok" para começar seu turno: ')
                    input('você é um cidadão, disfarce por um tempo e digite "passar" para terminar seu turno: ')
                    print('\n' * 100)
                    jogadorTurno += 1
                elif(jogadores[jogadorTurno] == detetive):
                    input(f'vez de {jogadores[jogadorTurno]}, digite "ok" para começar seu turno: ')
                    escolhaDetetive = input('quem você quer investigar? ')
                    if(escolhaDetetive in jogadores):
                        if(escolhaDetetive == assassino):
                            print(f'{escolhaDetetive} é o assassino!')
                        else:
                            print(f'{escolhaDetetive} não é o assassino')
                        input('digite "ok" para terminar seu turno: ')
                        print('\n' * 100)
                        jogadorTurno += 1
                    else:
                        print('escolha invalida')
                elif(jogadores[jogadorTurno] == anjo):
                    input(f'vez de {jogadores[jogadorTurno]}, digite "ok" para começar seu turno: ')
                    escolhaAnjo = input('quem voce quer proteger? ')
                    if(escolhaAnjo in jogadores):
                        input('digite "ok" para terminar seu turno: ')
                        print('\n' * 100)
                        jogadorTurno += 1
                    else:
                        print('escolha invalida')
                elif(jogadores[jogadorTurno] == assassino):
                    input(f'vez de {jogadores[jogadorTurno]}, digite "ok" para começar seu turno: ')
                    escolhaAssassino = input('quem você quer matar? ')
                    if(escolhaAssassino in jogadores):
                        input('digite "ok" para terminar seu turno: ')
                        print('\n' * 100)
                        jogadorTurno += 1
                    else:
                        print('escolha invalida')
            #programação dia (jogadores votam)
            print('a cidade acorda.')
            if(escolhaAnjo == escolhaAssassino):
                print('não houveram mortes essa noite')
            else:
                print(f'{escolhaAssassino} foi assassinado')
                jogadores.remove(escolhaAssassino)
                jogadoresExcetoAssassino.remove(escolhaAssassino)
            input('digite "ok" para iniciar a votação: ')
            jogadoresNaPartida = len(jogadores)
            jogadorTurnoVoto = 0
            votos = []
            while(jogadorTurnoVoto < jogadoresNaPartida):
                voto = input(f'vez de {jogadores[jogadorTurnoVoto]}, em quem você vota? ')
                if(voto in jogadores):
                    jogadorTurnoVoto += 1
                    votos.append(voto)
                else:
                    print('voto inválido')
            maisVotado = Counter(votos).most_common(2)
            #sistema de empate
            if(maisVotado[0][1] == maisVotado[1][1]):
                print(f'houve um empate, {maisVotado[0][0]} e {maisVotado[1][0]} tiveram {maisVotado[1][1]} votos')
            else:
                eliminadoVotos = maisVotado[0][0]
                quantidadeVotosEliminado = maisVotado[0][1]
                jogadores.remove(eliminadoVotos)
                if(eliminadoVotos in jogadoresExcetoAssassino):
                    jogadoresExcetoAssassino.remove(eliminadoVotos)
                    print(f'a cidade eliminou {eliminadoVotos}, com {quantidadeVotosEliminado} votos')
        if(assassino in jogadores):
            print(f'o assassino ({assassino}) venceu!')
            jogarNovamente = input('jogar novamente? ')
            if(jogarNovamente == 'sim'):
                print('reiniciando...')
            elif(jogarNovamente == 'nao'):
                break
        else:
            print('o assassino foi eliminado')
            jogarNovamente = input('jogar novamente? ')
            if(jogarNovamente == 'sim'):
                print('reiniciando...')
            elif(jogarNovamente == 'nao'):
                break
    else:
        print('Digite um número válido')