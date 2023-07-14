# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Coleta o número de casos de teste, em uma linha, converte em inteiro, pelo int() e atribui
 para a variável n.
 (2) Inicia um loop for de intervalo [0, n). A cada repetição:
     (3) Coleta um número, em uma linha, converte em inteiro, pelo int() e atribui
     para a variável number.
     (4) Inicia uma variável de soma divisors_sum com valor inicial 0.
     (5) Inicia um loop for de intervalo [1, number). A cada repetição:
         (6) Se o resto divisão do número em questão com o number for igual a zero, é um divisor,
         portanto soma este valor em divisors_sum.
    (7) Se a soma dos divisores for igual ao number, imprime <number> eh perfeito.
    (8) Caso contrário, imprime <number> não eh perfeito.
'''

n = int(input())  # Coleta o número de casos de teste

for i in range(n):  # Inicia loop de intervalo [0, n)
    
    number = int(input())  # Coleta um número inteiro
    divisors_sum = 0  # Inicia variável de soma
    for j in range(1, number):  # Inicia um loop de intervalo [1, number)
    
        if number % j == 0:  # Se for um divisor
            divisors_sum += j  # Então, soma em divisors_sum
    if divisors_sum == number:  # Se a soma dos divisores for igual ao número
        print(number, 'eh perfeito')  # Imprime que é perfeito
    else:  # Caso contrário
        print(number, 'nao eh perfeito')  # Imprime que não é perfeito
            