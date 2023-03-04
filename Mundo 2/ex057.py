''' Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado,
 peça a digitação novamente até ter um valor correto.'''

sexo = str(input('Digite o sexo[M ou F]: ')).strip().upper()[0]
while sexo not in ['M', 'F']:
    print('Valor inválido. Tente Novamente!')
    sexo = str(input('Digite o sexo[M ou F]: ')).strip().upper()[0]
print(f'Sexo {sexo} registro com sucesso!')