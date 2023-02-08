#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual foi a velocidade do veículo? '))
if velocidade > 80:
    calc = (velocidade - 80) * 7
    print('Você ultrapassou o limite de velocidade e será multado.')
    print(f'Você pagará R${calc:.2f} reais.')
else:
    print('Tudo certo!')