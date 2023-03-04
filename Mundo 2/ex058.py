''' Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o
jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint
from time import sleep
palpites = 0
while True:
    computador = randint(0, 10)
    print('-='*20)
    jogador = int(input('Em qual número eu pensei? De 0 a 10 = '))
    palpites += 1
    print('ANALISANDO...')
    sleep(1)
    if jogador == computador:
        print(f'Parabéns eu pensei no número {jogador}, então você acertou!')
        break
    else:
        print(f'Você errou eu pensei no número {computador}, e você digitou {jogador}')
print(f'Foram necessários {palpites} palpites para você vencer!')