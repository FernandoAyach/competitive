# -*- coding: utf-8 -*-

'''
Coleta o valor da distância e converte em inteiro.
Coleta o valor dos litros e converte em real.
Imprime valor do consumo (distancia / litros) com 3 casas decimais na tela.
'''

distance = int(input())  # Distância em inteiro
liters = float(input())  # Litros em real

print('{:.3f} km/l'.format(distance / liters))  # Imprime consumo com 3 casas decimais na tela