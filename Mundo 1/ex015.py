# Escreva um programa que pergunte a quantidade de Km percorridos por um carro
# alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Qual a quantidade de km percorridos? '))
dias = int(input('Qual a quantidade de dias que ele foi alugado? '))
preço = (60 * dias) + (km * 0.15)
print('O preço a pagar pela quantidade de km rodados e dias será de R${:.2f}'.format(preço))