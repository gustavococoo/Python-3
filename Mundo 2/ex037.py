# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será
# a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro: '))
print('-='*15)
print('''{}1 - Binário
2 - Octal
3 - Hexadecimal{}'''.format('\033[33m', '\033[m'))
opção = int(input('Escolha a opção qual será a base de conversão:'))
print('-='*15)
if opção == 1:
    print(f'{num} na base Binária é: {bin(num)[2:]}')
elif opção == 2:
    print(f'{num} na base Octal é: {oct(num)[2:]}')
elif opção == 3:
    print(f'{num}na base Hexadecimal é: {hex(num)[2:]}')
else:
    print('Opção inválida, tente novamente!')