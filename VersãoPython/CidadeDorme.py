import random
from collections import Counter
import os

def LimparTela():
    if(os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')

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
        jogadoresExcetoAssassinos = jogadores.copy()
        assassinos = []
        assassino = random.choice(cidadaos)
        cidadaos.remove(assassino)
        jogadoresExcetoAssassinos.remove(assassino)
        assassinos.append(assassino)
        detetive = random.choice(cidadaos)
        cidadaos.remove(detetive)
        anjo = random.choice(cidadaos)
        cidadaos.remove(anjo)
        if(len(jogadores) > 5):
            traidor = random.choice(cidadaos)
            cidadaos.remove(traidor)
            jogadoresExcetoAssassinos.remove(traidor)
            assassinos.append(traidor)
            traidorNaPartida = True
            assassinoVivo = True
            partidaComecaComTraidor = True
        elif(len(jogadores) <= 5):
            partidaComecaComTraidor = False
            traidorNaPartida = False
        print('classes atribuídas!')
        rodada = 0
        #programação das rodadas
        while((len(jogadoresExcetoAssassinos) > len(assassinos)) and (len(assassinos) > 0)):
            rodada += 1
            #programação noite (jogadores exercem suas classes)
            print('A cidade Dorme.\n')
            jogadoresNaPartida = len(jogadores)
            jogadorTurno = 0
            escolhaAnjo = None
            while(jogadorTurno < jogadoresNaPartida):
                if(jogadores[jogadorTurno] in cidadaos):
                    input(f'vez de {jogadores[jogadorTurno]}, aperte a tecla "enter" para começar seu turno ')
                    input('você é um cidadão, disfarce por um tempo e digite "passar" para terminar seu turno: ')
                    LimparTela()
                    jogadorTurno += 1
                elif(jogadores[jogadorTurno] == detetive):
                    input(f'vez de {jogadores[jogadorTurno]}, aperte a tecla "enter" para começar seu turno ')
                    escolhaDetetive = input('quem você quer investigar? ')
                    if(escolhaDetetive in jogadores):
                        if(escolhaDetetive == assassino):
                            print(f'{escolhaDetetive} é o assassino!')
                        elif((partidaComecaComTraidor == True) and (assassinoVivo == False)):
                            if(escolhaDetetive == traidor):
                                print(f'{escolhaDetetive} é o assassino')
                        else:
                            print(f'{escolhaDetetive} não é o assassino')
                        input('aperte a tecla "enter" para finalizar seu turno ')
                        LimparTela()
                        jogadorTurno += 1
                    else:
                        print('escolha invalida')
                elif(jogadores[jogadorTurno] == anjo):
                    input(f'vez de {jogadores[jogadorTurno]}, aperte a tecla "enter" para começar seu turno ')
                    escolhaAnjo = input('quem voce quer proteger? ')
                    if(rodada == 1):
                        if(escolhaAnjo in jogadores):
                            escolhaAnteriorAnjo = escolhaAnjo
                            input('aperte a tecla "enter" para finalizar seu turno ')
                            LimparTela()
                            jogadorTurno += 1
                        else:
                            print('escolha invalida')
                    else:
                        if((escolhaAnjo in jogadores) and (escolhaAnjo != escolhaAnteriorAnjo)):
                             escolhaAnteriorAnjo = escolhaAnjo
                             input('aperte a tecla "enter" para finalizar seu turno ')
                             LimparTela()
                             jogadorTurno += 1
                        else:
                            print('escolha invalida')
                elif(jogadores[jogadorTurno] == assassino):
                    input(f'vez de {jogadores[jogadorTurno]}, aperte a tecla "enter" para começar seu turno ')
                    if((partidaComecaComTraidor == True) and (traidorNaPartida == True)):
                        print(f'traidor: {traidor}')
                    escolhaAssassino = input('quem você quer matar? ')
                    if(escolhaAssassino in jogadores):
                        input('aperte a tecla "enter" para finalizar seu turno ')
                        LimparTela()
                        jogadorTurno += 1
                    else:
                        print('escolha invalida')
                elif(partidaComecaComTraidor == True):
                    if(jogadores[jogadorTurno] == traidor):
                        if(assassinoVivo == True):
                            input(f'vez de {jogadores[jogadorTurno]}, aperte a tecla "enter" para começar seu turno ')
                            input(f'voce é o traidor e o assassino ({assassino}) ainda está vivo, disfarce por um tempo e digite "passar" para terminar seu turno: ')
                            LimparTela()
                            jogadorTurno += 1
                        elif(assassinoVivo == False):
                            input(f'vez de {jogadores[jogadorTurno]}, aperte a tecla "enter" para começar seu turno ')
                            escolhaAssassino = input('você agora é o assassino, quem você quer matar? ')
                            if(escolhaAssassino in jogadores):
                                input('aperte a tecla "enter" para finalizar seu turno ')
                                LimparTela()
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
                jogadoresExcetoAssassinos.remove(escolhaAssassino)
            if((len(jogadoresExcetoAssassinos) > len(assassinos)) and (len(assassinos) > 0)):
                input('aperte a tecla "enter" para iniciar a votação ')
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
                if(len(maisVotado) == 2 and (maisVotado[0][1] == maisVotado[1][1])):
                    print(f'houve um empate, {maisVotado[0][0]} e {maisVotado[1][0]} tiveram {maisVotado[1][1]} votos')
                else:
                    eliminadoVotos = maisVotado[0][0]
                    quantidadeVotosEliminado = maisVotado[0][1]
                    jogadores.remove(eliminadoVotos)
                    if(eliminadoVotos in jogadoresExcetoAssassinos):
                        jogadoresExcetoAssassinos.remove(eliminadoVotos)
                        print(f'a cidade eliminou {eliminadoVotos} com {quantidadeVotosEliminado} votos')
                    elif((eliminadoVotos in assassinos) and (len(assassinos) >= 1)):
                        if(eliminadoVotos == assassino):
                            assassinos.remove(eliminadoVotos)
                            print(f'o assassino {eliminadoVotos} foi eliminado com {quantidadeVotosEliminado} votos')
                            traidorNaPartida = False
                            assassinoVivo = False
                        if(partidaComecaComTraidor == True):
                            if(eliminadoVotos == traidor):
                                if(assassinoVivo == True):
                                    assassinos.remove(eliminadoVotos)
                                    print(f'a cidade eliminou {eliminadoVotos} com {quantidadeVotosEliminado} votos')
                                    traidorNaPartida = False
                                else:
                                    assassinos.remove(eliminadoVotos)
                                    print(f'o traidor {eliminadoVotos} foi eliminado com {quantidadeVotosEliminado} votos')
        if(len(assassinos) == len(jogadoresExcetoAssassinos)):
            if(partidaComecaComTraidor == True):
                print(f'o assassino ({assassino}) e o traidor ({traidor}) venceram!')
            elif(partidaComecaComTraidor == False):
                print(f'o assassino {assassino} venceu!')
            jogarNovamente = None
            while((jogarNovamente != 'sim') and (jogarNovamente != 'nao')):
                jogarNovamente = input('jogar novamente? ')
                if((jogarNovamente != 'sim') and (jogarNovamente != 'nao')):
                    print('opção invalida.')
            if(jogarNovamente == 'sim'):
                LimparTela()
            elif(jogarNovamente == 'nao'):
                break
        else:
            print('o assassino foi eliminado, a cidade vence!')
            jogarNovamente = input('jogar novamente? ')
            if(jogarNovamente == 'sim'):
                LimparTela()
            elif(jogarNovamente == 'nao'):
                break
    else:
        print('Digite um número válido.')