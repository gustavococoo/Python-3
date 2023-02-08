# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Nome completo: '))
print(f'O nome {nome.upper()} contém "SILVA" ?', end=' ')
print('SILVA' in nome.upper().split())