# -*- coding: utf-8 -*-

'''
Entrada:
 - Coleta o tempo da viagem em uma linha, converte para inteiro e atribui à variável trip_time.
 - Coleta a velocidade em uma linha, converte para inteiro e atribui à variável speed.
 - Define uma constante para o consumo do carro CAR_CONSUME, com valor 12

Desenvolvimento:
 - Calcula a distância da viagem pela fórmula da velocidade média: v = d*t,
 e atribui para a variável trip_distance.
 - Tendo a proporção de consumo, calcula os litros usados dividindo a distância
 pelo consumo, atribiu o resultado à variável used_liters.
 
Saída:
 - Imprime resultado na tela com aproximação de 3 casas decimais.
 
'''

trip_time = int(input())  # Coleta tempo de viagem, em inteiro
speed = int(input())  # Coleta velocidade do carro, em inteiro
CAR_CONSUME = 12  # Define constante para o consumo do carro

trip_distance = trip_time * speed  # Calcula a distância da viagem

used_liters = trip_distance / CAR_CONSUME  # Calcula os litros utilizados

print('{:.3f}'.format(used_liters))  # Imprime resultado com 3 casas decimais