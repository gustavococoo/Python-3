# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

from math import hypot
cateto1 = float(input('Digite a medida do cateto oposto: '))
cateto2 = float(input('Digite a medida do cateto adjacente: '))
print(f'O comprimento da hipotenusa entre {cateto1:.1f} e {cateto2:.1f} é: {hypot(cateto1, cateto2):.1f}')
