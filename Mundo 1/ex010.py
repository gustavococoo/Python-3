# Escreve um programa que leia o quanto uma pessoa tem dinheiro na carteira e quantos doláres ela pode comprar.

d = float(input('Quanto dinheiro você tem na carteira? R$'))
c = d / 5.16
print('Você pode comprar US${:.2f} doláres com {:.1f} reais'.format(c, d))