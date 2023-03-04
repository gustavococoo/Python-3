''' Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

contador = 1
maior_idade = homem = mulher_nova = 0
while True:
    print('=' * 20)
    print(f'CADASTRE A {contador}ª PESSOA')
    print('=' * 20)
    idade = int(input(f'Digite a idade da {contador}ª pessoa: '))
    sexo = str(input(f'Digite o sexo da {contador}ª pessoa: [M/F] ')).strip().upper()[0]
    contador += 1
    if idade >= 18:
        maior_idade += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade <= 20:
        mulher_nova += 1
    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
print(f'Ao final foram {maior_idade} pessoas com mais de 18 anos.')
print(f'Ao todo tem {homem} homens cadastrados.')
print(f'E tem {mulher_nova} mulheres com menos de 20 anos.')