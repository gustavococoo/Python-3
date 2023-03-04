''' Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
ano = int(input('Qual o seu ano de nascimento? '))
comparar = date.today().year - ano
print(f'Você nasceu no ano de {ano} e tem {comparar} anos')
if comparar >= 18 and comparar <= 24:
    print('Já está na hora exata de se alistar!')
elif comparar < 18:
    tempo = 18 - comparar
    print('Infelizmente ainda não está no tempo de se alistar ao serviço militar!')
    print('Falta {} ano, para o seu alistamento.'.format(tempo))
elif comparar > 24:
    tempo = comparar - 24
    print('Já passou do tempo do alistamento, passou {} ano.'.format(tempo))