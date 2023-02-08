#Deselvolva um programa que leia as duas notas de um aluno, e mostre a sua média.

p = float(input('Insira a primeira nota: '))
s = float(input('Insira a segunda nota: '))
m = (p + s) / 2
print('A média é: {:.1f}'.format(m))