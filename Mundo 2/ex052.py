''' Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

num = int(input('Digite um número: '))
for c in range(1, 1+1):
    if num % 2 == 1:
        print('É PRIMO.')
    else:
        print('NÃO É PRIMO.')