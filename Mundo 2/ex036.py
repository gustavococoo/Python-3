# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o
# salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou
# então o empréstimo será negado.

print('*='*15)
print('  {}Empréstimo bancário{}'.format('\033[4;33m', '\033[m'))
print('*='*15)
vlrCasa = float(input('Qual o valor da casa? R$'))
salário = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos você vai pagar? '))
qntMeses = 12 * anos
prestação = (vlrCasa / qntMeses)
# calcula se a prestação é maior do que 30% do salário dele
if prestação > salário * 0.3:
    print('Infelizmente você não pode ter o empréstimo!')
else:
    print(f'Você pode ter o empréstimo, com parcelas de R${prestação:0.2f}')
