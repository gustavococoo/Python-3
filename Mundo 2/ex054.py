'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores.'''

from datetime import date
maior = 0
menor = 0
for a in range(1, 7+1):
    ano = int(input(f'Qual o ano de nascimento da {a}ª pessoa: '))
    idade = date.today().year - ano
    if idade > 18:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas são maiores de idade!')
print(f'{menor} pessoas ainda atingiram a maioridade!')
