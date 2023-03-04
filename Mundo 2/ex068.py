''' Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
print('='*20)
print('JOGO DO PAR OU ÍMPAR')
print('='*20)
contador = 0
while True:
    computador = randint(0, 10)
    num = int(input('Informe um valor: '))
    jogador = str(input('Jogue Par ou Ímpar? [P/I]')).strip().upper()[0]
    print('-'*20)
    resultado = computador + num
    if resultado % 2 == 0 and jogador == 'P':
        print(f'Você jogou {num} e o computador {computador}. Total de {resultado} Deu PAR')
        print('Você Venceu! \nVamos jogar novamente...')
        print('-'*20)
        contador += 1
    elif resultado % 2 == 1 and jogador == 'I':
        print(f'Você jogou {num} e o computador {computador}. Total de {resultado} Deu ÍMPAR')
        print('Você Venceu! \nVamos jogar novamente...')
        print('-' * 20)
        contador += 1
    elif resultado % 2 == 0 and jogador == 'I':
        print(f'Você jogou {num} e o computador {computador}. Total de {resultado} Deu PAR')
        print('Você Perdeu!')
        print('-' * 20)
        break
    else:
        print(f'Você jogou {num} e o computador {computador}. Total de {resultado} Deu ÍMPAR')
        print('Você Perdeu!')
        print('-' * 20)
        break
print(f'GAME OVER! \nVocê venceu {contador} vezes!')
