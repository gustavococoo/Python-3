'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
termos dessa progressão.'''

# fórmula = pt1 + (qt - 1)r
pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

s = pt # soma recebe primeiro termo
for c in range(1 , 10+1):
    print(f'O {c}º termo é {s}') #imprime os 10 primeiros termos
    s += r #aqui faz a somatória, somando o primeiro + a razão e dai por diante

