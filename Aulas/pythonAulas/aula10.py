'''
#Condição composta
tempo = int(input('Quantos tem o seu carro? '))
if tempo <= 3:
    print('Carro Novo!')
else:
    print('Carro Velho!')
print('-'*20)

#Condição simples
nome = str(input('Qual o seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
print(f'Bem-vindo, {nome}')
'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Parabéns' if m >= 6.0 else 'Estude mais')