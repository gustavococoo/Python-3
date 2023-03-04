''' Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário
se ele quer ou não continuar a digitar valores.'''

r = 'S'
soma = contador = menor = maior = 0
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    soma += n
    contador += 1
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
média = soma / contador
print(f'Foram digitados {contador} números.')
print(f'A média foi: {média:.2f}')
print(f'O maior valor foi: {maior}')
print(f'O menor valor foi: {menor}')