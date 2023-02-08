#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
#descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0, 5)
print('-='*20)
print('Jogo da Adivinhação!')
print('-='*20)
jogador = int(input('Em qual número eu pensei? De 0 a 5 '))
print('ANALISANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns eu pensei no número {}, então você acertou!'.format(jogador))
else:
    print(f'Você errou eu pensei no número {computador} e você digitou {jogador}')