# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#exemplo: Ana Maria de Souza >> primeiro: Ana; último: Souza

nome = str(input('Nome completo: ')).strip()
n = nome.split()
print(f'Seu primeiro nome é {n[0]}')
print(f'Seu último nome é {n[len(n)-1]}')