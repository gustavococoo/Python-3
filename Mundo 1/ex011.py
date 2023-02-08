# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
#de tinta necesssária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m2.

lar = float(input('Digite a largura da parade: '))
alt = float(input('Digite a altura da parede: '))
ar = lar * alt
print('Sua parede tem área total de {:.2f} m².'.format(ar))
print('O rendimento do fabricante é de 2m² por litro.')
qnt = ar / 2
print('Para uma parede que tem a área de {:.2f} m² serão necessários {:.1f} litros de tinta.'.format(ar, qnt))