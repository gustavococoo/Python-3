# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
angulo = int(input('Digite um número inteiro qualquer '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'Seno {seno:.2f}\nCosseno {cosseno:.2f}\nTangente {tangente:.2f}')