from random import choice
from time import sleep
print('Vamos brincar de jokenpo!')
n=0
while n!=1 or n!=2:
    n = int(input("""Você prefere md3 ou md5?
[1]md3
[2]md5
Digite aqui sua opção:"""))
    cganha = 0
    jganha = 0
    if n == 1:
        print('Você selecionou uma melhor de 3! Logo serão 3 partidas, quem tiver a melhor pontuação vence!')
        sleep(1)
        for c in range(1, 4):
            jogador=0
            while jogador !=1 and jogador!=2 and jogador!=3:
                print('Vamos para {}° de 3!'.format(c))
                jogador = int(input("""\033[1:37m[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
Selecione qual opção você irá escolher:"""))
                opcoes = ['pedra', 'papel', 'tesoura']
                computador = choice(opcoes)
                if jogador == 1 and computador == 'pedra':
                    print('JO')
                    sleep(1)
                    print('KEN')
                    sleep(1)
                    print('PO...')
                    sleep(1)
                    print('Eu tirei {} e você pedra!'.format(computador), end=' >')
                    print('>>EMPATE NESSA RODADA! PLACAR {} PARA MIM X {} PARA VOCÊ'.format(cganha, jganha))

                elif jogador == 1 and computador == 'papel':
                    print('JO')
                    sleep(1)
                    print('KEN')
                    sleep(1)
                    print('PO...')
                    sleep(1)
                    print('Eu tirei {} e você pedra!'.format(computador), end=' >')
                    cganha += 1
                    print('>>EU GANHEI NESSA RODADA! PLACAR: {} PARA MIM X {} PARA VOCÊ'.format(cganha, jganha))

                elif jogador == 1 and computador == 'tesoura':
                    print('JO')
                    sleep(1)
                    print('KEN')
                    sleep(1)
                    print('PO...')
                    sleep(1)
                    print('Eu tirei {} e você pedra!'.format(computador), end=' >')
                    jganha += 1
                    print('>>VOCÊ GANHOU NESSA RODADA! PLACAR {} PARA MIM X {} PARA VOCÊ'.format(cganha, jganha))

                elif jogador == 2 and computador == 'pedra':
                    print('JO')
                    sleep(1)
                    print('KEN')
                    sleep(1)
                    print('PO...')
                    sleep(1)
                    print('Eu tirei {} e você papel!'.format(computador), end=' >')
                    jganha += 1
                    print('>>VOCÊ GANHOU NESSA RODADA! PLACAR {} PARA MIM X {} PARA VOCÊ'.format(cganha,
                                                                                                 jganha))
                elif jogador == 2 and computador == 'papel':
                    print('JO')
                    sleep(1)
                    print('KEN')
                    sleep(1)
                    print('PO...')
                    sleep(1)
                    print('Eu tirei {} e você papel!'.format(computador), end=' >')
                    print('>>EMPATE NESSA RODADA! PLACAR {} PARA MIM X {} PARA VOCÊ'.format(cganha, jganha))

                elif jogador == 2 and computador == 'tesoura':
                    print('JO')
                    sleep(1)
                    print('KEN')
                    sleep(1)
                    print('PO...')
                    sleep(1)
                    print('Eu tirei {} e você papel!'.format(computador), end=' >')
                    cganha += 1
                    print('>>EU GANHEI NESSA RODADA! PLACAR: {} PARA MIM X {} PARA VOCÊ'.format(cganha, jganha))

                elif jogador == 3 and computador == 'pedra':
                    print('\033[mJO')
                    sleep(1)
                    print('KEN')
                    sleep(1)
                    print('PO...')
                    sleep(1)
                    print('Eu {} e você tesoura!'.format(computador), end=' >')
                    cganha += 1
                    print('>>EU GANHEI NESSA RODADA! PLACAR: {} PARA MIM X {} PARA VOCÊ'.format(cganha, jganha))

                elif jogador == 3 and computador == 'papel':
                    print('JO')
                    sleep(1)
                    print('KEN')
                    sleep(1)
                    print('PO...')
                    sleep(1)
                    print('Eu {} e você tesoura!'.format(computador), end=' >')
                    jganha += 1
                    print('>>VOCÊ GANHOU NESSA RODADA! PLACAR {} PARA MIM X {} PARA VOCÊ'.format(cganha, jganha))

                elif jogador == 3 and computador == 'tesoura':
                    print('JO')
                    sleep(1)
                    print('KEN')
                    sleep(1)
                    print('PO...')
                    sleep(1)
                    print('Eu {} e você tesoura!'.format(computador), end=' >')
                    print('>>EMPATE NESSA RODADA! PLACAR {} PARA MIM X {} PARA VOCÊ'.format(cganha, jganha))

                if jogador != 1 and jogador != 2 and jogador != 3:
                    print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')

        print('m=' * 60)
        if cganha > jganha:
            print('EU GANHEI O JOGO!! PLACAR FINAL: {} PARA MIM X {} PARA VOCÊ'.format(cganha, jganha))

        if jganha > cganha:
            print('VOCÊ GANHOU O JOGO! PLACAR FINAL: {} PARA MIM X {} PARA VOCÊ, PARABÉNS!!'.format(cganha,jganha))

        print('=' * 60)
    if n == 2:
        print('Você selecionou uma melhor de 5, quem tiver a melhor pontuação vence!')
        sleep(1)
        for c in range(1, 6):
            jogador=0
            while jogador != 1 and jogador != 2 and jogador != 3:
                print('Vamos para {}° de 5!'.format(c))
                jogador = int(input("""[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
Selecione qual opção você irá escolher:"""))
                opcoes = ['pedra', 'papel', 'tesoura']
                computador = choice(opcoes)
                if jogador == 1 and computador == 'pedra':
                    print('JO')
                    sleep(1)
                    print('KEN')
                    sleep(1)
                    print('PO...')
                    sleep(1)
                    print('Eu tirei {} e você pedra!'.format(computador), end=' >')
                    print('>>EMPATE NESSA RODADA! PLACAR {} PARA MIM X {} PARA VOCÊ'.format(cganha, jganha))

                elif jogador == 1 and computador == 'papel':
                    print('JO')
                    sleep(1)
                    print('KEN')
                    sleep(1)
                    print('PO...')
                    sleep(1)
                    print('Eu tirei {} e você pedra!'.format(computador), end=' >')
                    cganha += 1
                    print('>>EU GANHEI NESSA RODADA! PLACAR: {} PARA MIM X {} PARA VOCÊ'.format(cganha, jganha))

                elif jogador == 1 and computador == 'tesoura':
                    print('JO')
                    sleep(1)
                    print('KEN')
                    sleep(1)
                    print('PO...')
                    sleep(1)
                    print('Eu tirei {} e você pedra!'.format(computador), end=' >')
                    jganha += 1
                    print('>>VOCÊ GANHOU NESSA RODADA! PLACAR {} PARA MIM X {} PARA VOCÊ'.format(cganha, jganha))

                elif jogador == 2 and computador == 'pedra':
                    print('JO')
                    sleep(1)
                    print('KEN')
                    sleep(1)
                    print('PO...')
                    sleep(1)
                    print('Eu tirei {} e você papel!'.format(computador), end=' >')
                    jganha += 1
                    print('>>VOCÊ GANHOU NESSA RODADA! PLACAR {} PARA MIM X {} PARA VOCÊ'.format(cganha,
                                                                                                           jganha))
                elif jogador == 2 and computador == 'papel':
                    print('JO')
                    sleep(1)
                    print('KEN')
                    sleep(1)
                    print('PO...')
                    sleep(1)
                    print('Eu tirei {} e você papel!'.format(computador), end=' >')
                    print('>>EMPATE NESSA RODADA! PLACAR {} PARA MIM X {} PARA VOCÊ'.format(cganha, jganha))

                elif jogador == 2 and computador == 'tesoura':
                    print('JO')
                    sleep(1)
                    print('KEN')
                    sleep(1)
                    print('PO...')
                    sleep(1)
                    print('Eu tirei {} e você papel!'.format(computador), end=' >')
                    cganha += 1
                    print('>>EU GANHEI NESSA RODADA! PLACAR: {} PARA MIM X {} PARA VOCÊ'.format(cganha, jganha))

                elif jogador == 3 and computador == 'pedra':
                    print('\033[mJO')
                    sleep(1)
                    print('KEN')
                    sleep(1)
                    print('PO...')
                    sleep(1)
                    print('Eu {} e você tesoura!'.format(computador), end=' >')
                    cganha += 1
                    print('>>EU GANHEI NESSA RODADA! PLACAR: {} PARA MIM X {} PARA VOCÊ'.format(cganha, jganha))

                elif jogador == 3 and computador == 'papel':
                    print('JO')
                    sleep(1)
                    print('KEN')
                    sleep(1)
                    print('PO...')
                    sleep(1)
                    print('Eu {} e você tesoura!'.format(computador), end=' >')
                    jganha += 1
                    print('>>VOCÊ GANHOU NESSA RODADA! PLACAR {} PARA MIM X {} PARA VOCÊ'.format(cganha,jganha))

                elif jogador == 3 and computador == 'tesoura':
                    print('JO')
                    sleep(1)
                    print('KEN')
                    sleep(1)
                    print('PO...')
                    sleep(1)
                    print('Eu {} e você tesoura!'.format(computador), end=' >')
                    print('>>EMPATE NESSA RODADA! PLACAR {} PARA MIM X {} PARA VOCÊ'.format(cganha, jganha))

                if jogador != 1 and jogador != 2 and jogador != 3:
                    print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')

        print('=' * 60)
        if cganha > jganha:
            print('EU GANHEI O JOGO!! PLACAR FINAL: {} PARA MIM X {} PARA VOCÊ'.format(cganha, jganha))

        if jganha > cganha:
            print('VOCÊ GANHOU O JOGO! PLACAR FINAL: {} PARA MIM X {} PARA VOCÊ, PARABÉNS!!'.format(cganha,jganha))
        print('=' * 60)

    if n != 1 and n != 2:
        print('Opção inválida! Tente novamente!')

                      
                        
                
