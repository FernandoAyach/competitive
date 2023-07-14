# -*- coding: utf-8 -*-

'''
Entrada:
 (1) Coleta um número, em uma linha, converte em inteiro, pelo int() e atribui para a variável n.
 (2) Cria uma variável factorial com valor n.

Desenvolvimento:
 (1) Inicia um loop for de intervalo [2, n). Dentro desse loop:
 (2) Faz factorial *= i

Saída:
 (1) Imprime factorial na tela
'''

n = int(input())  # Coleta um número inteiro

factorial = n  # Inicia uma variável factorial com valor n

for i in range(2, n):  # Inicia um loop [2, n)
    factorial *= i  # Multiplica o valor de i à variável factorial
    
print(factorial)  # Imprime o fatorial