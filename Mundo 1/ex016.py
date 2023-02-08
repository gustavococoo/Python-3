# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

# primeira forma
'''from math import trunc
num = float(input('Digite um número quebrado: '))
print(f'Sua porção inteira é {trunc(num)}')'''

# Segunda forma
num = float(input('Digite um número quebrado: '))
print(f'A sua porção inteira é {int(num)}')