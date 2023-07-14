# -*- coding: utf-8 -*-

'''
Entrada + Desenvolvimento:
 (1) Inicia um loop while infinito com condição True.
 (2) Coleta um número, em uma linha, converte em inteiro, pelo int(), e atribui para a variável number.
 (3) Inicia uma variável de soma de pares com valor 0, even_sum
 (4) Se o número recebido for 0, para o loop com break
 (5) Senão se for número par, inicia um loop for de intervalo [number, number + 10), com step 2, pois,
 assim, obteremos os 5 pares consecutivos de number, ele incluso.
 (6) Senão, é impar e inicia um loop for de intervalo [number + 1, number + 11), com step 2, pois,
 assim, obteremos os 5 pares consecutivos de number.

Saída:
 (1) Imprime a soma na tela
'''

while True:  # Inicia loop infinito
    number = int(input())  # Coleta um número inteiro
    even_sum = 0  # Inicia variável de soma de pares
     
    if number == 0:  # Se number for 0
        break  # Para o laço
    elif number % 2 == 0:  # Se for par
        for i in range(number, number + 10, 2):  # Inicia um loop [number, number + 10)
            even_sum += i  # Soma os pares
    else: # Senão, é impar
        for i in range(number + 1, number + 11, 2):  # Inicia um loop [number + 1, number + 11)
            even_sum += i  # Soma os pares
    print(even_sum)  # Imprime soma na tela