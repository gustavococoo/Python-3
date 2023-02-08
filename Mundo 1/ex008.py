# Escreve um programa que leia um valor em metros e exiba convertido em centrimetros e milimetros.

vm = float(input('Insira a metragem: '))
cm = vm * 100
mm = vm * 1000
print('{:.0f} metro equilivale à: \n{:.0f} centrimetros. \n{:.0f} milimetros.'.format(vm, cm, mm))