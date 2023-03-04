''' Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário
vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

total_gasto = count = produto_barato = total_mil = 0
produto = ''
while True:
    nome_produto = str(input('Qual o nome do produto? ')).strip()
    preco_produto = float(input('Qual o preço do produto? '))
    count += 1
    total_gasto += preco_produto
    print('='*25)
    if preco_produto > 1000:
        total_mil += 1
    if count == 1 or preco_produto < produto_barato:
        produto_barato = preco_produto
        produto = nome_produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
        print('=' * 25)
    if resposta == 'N':
        break
print(f'O total gasto na compra foi de R${total_gasto}')
print(f'{total_mil} produtos custaram mais de R$1000.')
print(f'O nome do produto mais barato foi {produto} e custou R$ {produto_barato}')