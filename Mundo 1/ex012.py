# Faça um programa que leia o preço de um produto e mostre o seu novo preço com 5% de desconto e se for parcelado

preço = float(input('Preço do produto: R$'))
desconto = preço * 0.05
preço_desconto = preço - desconto
preço_parcelado = preço + desconto
print('O produto que custa {:.2f} passará a custar {:.2f} com o desconto de {:.2f}.'.format(preço, preço_desconto, desconto))
print('O produto que custa {} passará a custar {} pagando parcelado com o aumento de {}'.format(preço, preço_parcelado, desconto))