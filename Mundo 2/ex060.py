''' Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120'''

num = int(input('Digite um número maior do 0 para calcular seu fatorial: '))
resultado = 1
contador = num
print(f'Calculo do Fatorial de {num}! = ',end='')
while contador > 0:
    print(f'{contador}', end=' ')
    print('x ' if contador > 1 else '= ', end='')
    resultado *= contador
    contador -= 1
print(resultado)