'''  Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa
 encerrará quando ele disser que quer mostrar 0 termos.'''

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
count = 1
soma = primeiro_termo
total = 0
mais_termos = 10
while mais_termos != 0:
    total += mais_termos
    while count <= total:
        print(f'O {count} termo é {soma}')
        count += 1
        soma += razão
    mais_termos = int(input('Quantos termos quer mostrar mais? '))
print('Progressão finalizada!')