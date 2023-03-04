''' Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
 pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''

while True:
    print('-' * 25)
    num = int(input('Digite um número para ver sua tabuada: [0 p/sair]'))
    print('-'*25)
    contador = 1
    if num <= 0:
        break
    while contador <= 10:
        print(f'{num} x {contador} = {num*contador}')
        contador += 1
print('Programa encerrado!')