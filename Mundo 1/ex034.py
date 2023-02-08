#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite o seu salário: "))
if salario > 1250:
    aumento = (salario * 0.10) + salario
    print(f'O seu salário de R${salario} com o aumento de 10% passará a ser R${aumento}')
else:
    aumento = salario * 0.15 + salario
    print(f'O seu salário de R${salario} com o aumento de 15% passará a ser R${aumento}')