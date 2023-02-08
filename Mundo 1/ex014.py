#  Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit

celsius = float(input('Informe a temperatura em ºC: '))
convesão = ((9 * celsius) / 5) + 32
print('A temperatura de {:.1f}ºC em Fahrenheit é {:.1f}ºF'.format(celsius,convesão))