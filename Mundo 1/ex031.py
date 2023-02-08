#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50
# por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Qual a distância percorrida? '))
if distancia <= 200:
    calc = distancia * 0.50
    print(f'Com a distância de {distancia} km, você pagará R${calc}.')
else:
    calc = distancia * 0.45
    print(f'Com a distância de {distancia} km, você pagará R${calc}.')