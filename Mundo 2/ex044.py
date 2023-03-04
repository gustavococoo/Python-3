'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros'''

print('{:=^40}'.format(' LUÍS CONSTRUÇÕES '))
produto = float(input('Valor do produto: R$'))
print('''Formas de pagamento
{}1 - Dinheiro / cheque
2 - À vista no cartão
3 - Cartão em até 2x
4 - Cartão 3x ou mais{}'''.format('\033[36m', '\033[m'))
opção = int(input('Escolha a opção para o pagamento: '))
if opção == 1:
    desconto = produto - (produto * 0.1) # calculo para 10% de desconto do produto
    print(f'Produto custando R${produto}, com o desconto de 10% você pagará R${desconto}')
elif opção == 2:
    desconto = produto - (produto * 0.05) # calculo para 5% de desconto do produto
    print(f'Produto custando R${produto}, com o desconto de 5% você pagará R${desconto}')
elif opção == 3:
    print(f'Produto com o preço normal!')
elif opção == 4:
    juros = produto + (produto * 0.2)
    parcela = int(input('Em quantas parcelas? '))
    print(f'Parcelando em {parcela}x ')
    print(f'Produto custando R${produto}, com essa forma de pagamento terá juros de 20% você pagará {juros}')
else:
    print('Opção inválida, tente novamente!')
