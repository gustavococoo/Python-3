'''Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''

num = int(input('{}Digite o número para ver sua tabuada:{} '.format('\033[4:34:40m', '\033[m')))
for c in range(1, 10+1):
    print(f'{num} x {c} = {num*c}')
print('FIM!')