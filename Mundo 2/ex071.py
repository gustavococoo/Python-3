''' Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual
será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão
entregues. OBS:
considere que o caixa possui cédulas de R$200, R$100, R$50, R$20, R$10, R$5 e R$1.'''

print('=' * 30)
print('{:^30}'.format('BANCO GUSTAVO COCO'))
print('=' * 30)
valor = int(input('Digite o valor a ser sacado: R$'))
total = valor
cédula = 200
total_cédula = 0
while True:
    if total >= cédula:
        total -= cédula
        total_cédula += 1
    else:
        if total_cédula > 0:
            print(f'Total de {total_cédula} de cédulas de R${cédula}')
        if cédula == 200:
            cédula = 100
        elif cédula == 100:
            cédula = 50
        elif cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 5
        elif cédula == 5:
            cédula = 1
        total_cédula = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO GUSTAVO COCO!')