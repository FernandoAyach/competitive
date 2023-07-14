# -*- coding: utf-8 -*-

'''
Entrada:
 (1) Coleta a distancia da base e do topo, em linhas diferentes, converte-as para inteiro, int(), e atribui,
 respectivamente, para as variáveis base_distance e top_distance.

Desenvolvimento + Saída:
 (1) Define a área total da nota (160 x 70) e atribui para a variável total_area.
 (2) Calcula a área da esquerda, equivalente a área de um trapézio, usando base_distance e top_distance
 como bases. Atribui para a variável left_area.
 (3) A área da direita é a área total menos a da esquerda. Atribui para variável right_area.
 (4) Se as áreas forem iguais, imprime 0, nenhuma vale nada.
 (5) Se a left_area for maior que a right_area, imprime 1, Felix ganhou a nota valiosa.
 (6) Senão, right_area é maior, imprime 2, Marzia ganhou a nota valiosa.
'''

base_distance = int(input())  # Coleta a distância da base em inteiro
top_distance = int(input())  # Coleta a distância do top em inteiro

total_area = 160 * 70  # Calcula a área total

left_area = ((base_distance + top_distance) * 70) / 2  # Calcula a área da esquerda
right_area = total_area - left_area  # Calcula a área da direita

# Se forem iguais
if left_area == right_area:
    # Imprime 0
    print(0)
# Se a da esquerda for maior
elif left_area > right_area:
    # Imprime 1
    print(1)
# Senão, a direita é maior
else:
    # Imprime 2
    print(2)