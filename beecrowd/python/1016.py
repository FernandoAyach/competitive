# -*- coding: utf-8 -*-

'''
Coleta o valor da distância e converte em inteiro.
O tempo para o carro Y se afastar N km do carro X é dado
pela multiplicação entre a N km e 2. Pois o carro Y afasta-se
1 km a cada 2 minutos.
'''

distance = int(input())   # Coleta distância em inteiro

print('{} minutos'.format(distance * 2))  # Calcula o tempo e imprime formatado