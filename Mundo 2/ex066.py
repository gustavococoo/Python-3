''' Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
 o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi
 a soma entre elas (desconsiderando o flag).'''

soma = contador = 0
while True:
    num = int(input('Digite um número: [999 condição de parada] '))
    if num == 999:
        break
    contador += 1
    soma += num
print(f'Ao todo foram digitados {contador} valores e a soma deles dá {soma}.')