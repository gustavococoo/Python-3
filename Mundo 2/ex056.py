''' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''

somaidade = 0
homem_velho = ''
maior_idade = 0
mulheres_nova = 0
for c in range(1, 4+1):
    nome = str(input(f'Digite o nome da {c}ª pessoa: ')).strip()
    idade = int(input(f'Digite a idade do(a) {nome}: '))
    sexo = str(input(f'Digite o sexo do(a) {nome}[M/F]: ')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maior_idade = idade
        homem_velho = nome
    if sexo in 'Mm' and maior_idade < idade:
        maior_idade = idade
        homem_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulheres_nova += 1

media = somaidade / 4
print(f'A média de idade do grupo é {media} anos')
print(f'O nome do homem mais velho é {homem_velho} e tem {maior_idade}')
print(f'Ao todo são {mulheres_nova} mulher(es) com menos de 20 anos.')
