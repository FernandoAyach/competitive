# -*- coding: utf-8 -*-

'''
Coleta o valor do raio, em real, e armazena o valor do pi.
Calcula o volume da esfera.
Imprime resultado na tela com 3 casas decimais de aproximação.
'''

radius = float(input())  # Coleta raio em real
pi = 3.14159  # Armazena valor do pi

volume = (4/3) * pi * radius**3  # Calcula o volume

print('VOLUME = {:.3f}'.format(volume))  # Imprime na tela com 3 casas decimais