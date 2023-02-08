'''nome = "Gustavo Coco"
print('Boa noite, {}{}{}!'.format('\033[4;34m', nome, '\033[m'))'''

nome = "Gustavo Coco"
cores = {'Limpa':'\033[m',
        'Azul': '\033[34m',
        'pretoebranco':'\033[7;40m'}
print('Olá, {}{}{} muito prazer em conhecer você!'.format(cores['pretoebranco'], nome, cores['Limpa']))