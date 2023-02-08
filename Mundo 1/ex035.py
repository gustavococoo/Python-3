#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))
if (r1 + r2 < r3) or (r1 + r3 < r2) or (r2 + r3 < r1):
    print('Com essas medidas não podem formar um triângulo.')
elif r1 == r2 and r1 == r3:
    print('Tiângulo Equilátero!')
elif r1 == r2 or r1 == r2 or r2 == r3:
    print('Triângulo Isósceles!')
else:
    print('Triângulo Escaleno!')