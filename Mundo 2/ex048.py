'''Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram
 no intervalo de 1 até 500.'''

soma = 0
conta = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        conta += 1
        print(c, end=' ')
print(f'\nSão {conta} valores')
print(f'A somatório de todos os múltiplos de 3 dar: {soma}')