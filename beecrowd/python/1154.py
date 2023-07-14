# -*- coding: utf-8 -*-

'''
Entrada + Desenvolvimento + Saída:
 (1) Inicia a variável n para contar os elementos, valor inicial zero.
 (2) Inicia a variável age_sum para armazenar a soma dos elementos, valor inicial zero.
 (3) Inicia um loop while infinito. A cada repetição desse loop:
 (4) Coleta uma idade, em uma linha, converte em inteiro, pelo int() e atribui à variável age.
 (4) Se for age for negativo, calcula a média age_sum / n, com duas casas decimais e imprime na tela e para o loop com break
 (5) Se não for negativa, segue a sequencia do código e soma age em age_sum.
 (6) Incrementa n em 1.
'''

n = 0  # Contador de elementos
age_sum = 0  # Soma de idades
while True:  # Inicia um loop infinito
    age = int(input())  # Coleta uma idade, em inteiro
     
    if age < 0:  # Se for negativo
        print('{:.2f}'.format(age_sum / n))  # Calcula a média
        break  # Para o loop
   
    age_sum += age  # Soma a idade à age_sum
    n += 1  # Incrementa 1 elemento
    