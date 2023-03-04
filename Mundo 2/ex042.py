''' Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes'''

r1 = float(input('Primeira área: '))
r2 = float(input('Segunda área: '))
r3 = float(input('Terceira área: '))
if (r3 > r2 + r1) or (r2 > r1 + r3) or (r1 > r2 + r3):
    print('Com essas medida não podem formar um triângulo')
elif r1 == r2 and r1 == r3:
    print('Triângulo EQUILÁTERO!')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('Triângulo ISÓSCELES!')
else:
    print('Triângulo ESCALENO!')
