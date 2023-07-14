# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Inicia um loop for que repete 100x. A cada repetição:
     (2) Le um número, converte para real, pelo float, e atribui para number.
     (3) Se number for menor ou igual a 10, imprime "A[{}] = {}".format(i, number), na tela,
     ou seja, o indice do vetor e o valor respectivo.
'''

for i in range(100):  # Inicia um loop que repete 100x
    
    number = float(input())  # Le um número real
    
    if number <= 10:  # Se for menor ou igual a dez
        print("A[{}] = {}".format(i, number))  # Imprime o número e o índice do vetor