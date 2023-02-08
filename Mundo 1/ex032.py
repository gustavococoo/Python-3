#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
ano = int(input('Digite o ano para ser analisado: '))
if ano == 0:
    # date.today() faz a busca do ano atual
    ano = date.today().year
    print(ano)
#formula para calcular o ano bissexto
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print(f'O ano {ano} É BISSEXTO!')
else:
    print(f'O ano {ano} NÃO É BISSEXTO!')