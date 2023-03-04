'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

frase = str(input('Digite uma frase: ')).replace(' ', '').upper()#replace remove a virgula , upper converte a frase toda maiúscula
inverso = frase[::-1]
#for c in range(len(frase)):

if frase == inverso:
      print('É um palíndromo!')
else:
     print('Não é um palíndromo!')