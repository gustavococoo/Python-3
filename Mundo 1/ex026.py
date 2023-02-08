# Faça um programa que leia uma frase pelo teclado e mostre
# quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e
# em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra "A" aparece: {frase.count("A")} vezes.')
print(f'A posição que a letra "A" aparece pela 1º vez é: {frase.find("A")+1}º posição.')
print(f'A posição que a letra "A" aparece a última vez é: {frase.rfind("A")+1}º posição.')