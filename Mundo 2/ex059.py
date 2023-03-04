''' Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

print('=-' * 15)
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
opção = 1
maior = 0
while opção!= 5:
    print('''{}
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa{}'''.format('\033[33m', '\033[m'))
    opção = int(input('Digite a opção desejada: '))
    if opção == 1:
        print(f'A soma entre {num1} + {num2} deu: {num1+num2}')
    elif opção == 2:
        print(f'A multplicação entre {num1} X {num2} deu: {num1*num2}')
    elif opção == 3:
        if num1 > num2:
           maior = num1
        else:
           maior = num2
        print(f'Entre {num1} e {num2} o maior valor é {maior}')
    elif opção == 4:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
   # elif opção == 5:
    #    break
    elif opção > 5:
        print('Opção inválida, tente novamente!')
print('FIM!')