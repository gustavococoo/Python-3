# Faça um programa que leia o salário de um funcionário e mostre o seu novo salário, com 15% de aumento.

# pedindo o salário do funcionário
salario = float(input('Salário de: R$'))
# calculo com aumento de 15%
novo_salario = salario + (salario * 0.15)

#print('Aumento ganho R$ {:.2f}'.format(novo_salario))
print('Salário total com o aumento R$ {:.2f}'.format(novo_salario))