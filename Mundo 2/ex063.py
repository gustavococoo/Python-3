''' Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos
 de uma Sequência de Fibonacci. Exemplo:
0 – 1 – 1 – 2 – 3 – 5 – 8'''

num = int(input('Quantos termos quer pra mostrar? '))
t1 = 0
t2 = 1
count = 3
print(f'{t1} > {t2} > ',end='')
while count <= num:
    t3 = t1 + t2
    print(f'{t3} > ', end='')
    t1 = t2
    t2 = t3
    count += 1
print('FIM.')