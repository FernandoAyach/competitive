# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Coleta o número de casos de teste, em uma linha, converte em inteiro, pelo int() e
 atribui para a variável n.
 (2) Inicia um loop for de intervalo [0, n - 1]. A cada repetição:
     (3) Inicia variável days correspondente ao número de dias, inicia com 0.
     (4) Coleta a quantidade de comida, converte em real, pelo float e atribui para food.
     (5) Inicia um loop while que repete enquanto food > 1. A cada repetição.
         (6) Divide food pela metade.
         (7) Soma um dia à days.
     (8) Imprime o total de dias
'''

n = int(input())  # Coleta o número de casos de teste

for i in range(n):  # Inicia um loop de intervalo [0, n - 1]
    
    days = 0  # Dias totais
    food = float(input())  # Total de suprimento em kg
    
    while food > 1:  # Enquanto houver mais de 1kg
        
        food /= 2  # Come a metade
        days += 1  # Soma um dia
    print(days, 'dias')  # Imprime o total de dias
        
    
    