'''  Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
 progressão usando a estrutura while.'''

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
contador = 1
soma = primeiro_termo # soma recebe primeiro termo
while contador <= 10:
    print(f'O {contador}º termo é {soma}') #imprime os 10 primeiros termos
    contador += 1
    soma += razão # soma o primeiro termo + a razão e dai por diante
print('FIM!')