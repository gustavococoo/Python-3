''' Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando o flag).'''

contador = soma = n = 0
while n != 999:
    n = int(input('Digite um número [999 condição de parada]: '))
    if n != 999:
        soma += n
        contador += 1
print(f'Ao todo foram digitados {contador} números e soma entre eles deu: {soma}')
