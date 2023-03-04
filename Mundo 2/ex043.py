'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida'''

peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura? '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'O seu Índice de Massa Corporal é {imc:.1f} está abaixo do peso!')
elif imc < 25:
    print(f'O seu Índice de Massa Corporal é {imc:.1f} está no Peso Ideal!')
elif imc < 30:
    print(f'O seu Índice de Massa Corporal é {imc:.1f} está Sobrepeso!')
elif imc <= 40:
    print(f'O seu Índice de Massa Corporal é {imc:.1f} está na fase de Obesidade!')
else:
    print(f'O seu Índice de Massa Corporal é {imc:.1f} está em Obesidade Mórbida, precisa de cuidar!')