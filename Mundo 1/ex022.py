# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = str(input('Nome completo: ')).strip()#strip- serve para remover os espaços da direita e esquerda
print(f'Nome com letras maiúsculas: {nome.upper()}')
print(f'Nome com letras menúsculas: {nome.lower()}')
print(f'Contagem de todos os caracteres (sem considerar espaços): {len(nome) - nome.count(" ")} caracteres')
print(f'O primeiro nome é {nome.split()[0]} e tem {len(nome.split()[0])} letras')