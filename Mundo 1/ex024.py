# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Digite o nome da cidade: ')).strip()
print('A cidade começa com o nome "SANTO"?', end=' ')
print('SANTO' in cidade.upper().split()[0])