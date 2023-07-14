# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Coleta a quantidade de números da sequência fibonacci, em uma linha, converte em inteiro, pelo
 int() e atribui para a variável n.
 (2) Se n for 1, imprime 0.
 (3) Senão se n for 2, imprime 0 1.
 (4) Senão:
     (5) Imprime 0 1 na tela, sem pular linha, com end = '', para posicionar os números em uma linha só
     (6) Inicia variável previous, contendo o penúltimo número, com valor 0
     (7) Inicia variável current, contendo o último número, com valor 1
     (8) Inicia um loop for de intervalo [2, n). Em cada repetição:
         (9) Calcula o próximo fibonacci fazendo previous + current e atribui para a variável next_fibonacci.
         (10) Imprime na tela posicionando um espaço no começo, o número resultante e sem pular linha (end = '').
         (11) Atribui o valor do current para o previous.
         (12) Atribui o valor de next_fibonacci para current.
    (13) Pula uma linha, com print().
'''

# Coleta a quantidade de números da sequência fibonacci
n = int(input())

if n == 1:  # Se for um número
    print(0)  # Imprime 0
elif n == 2:  # Se for 2 números
    print(0, 1)  # Imprime 0 1
else: # Se for mais de dois números
    print('0 1', end = '')  # Imprime os dois primeiros, sem pular linha
    previous = 0  # Define o anterior
    current = 1  # Define o atual
    for i in range(2, n):  # Loop que repete [2, n)
        next_fibonacci = previous + current  # Calcula o próximo número
        print('', next_fibonacci, end = '')  # Imprime na tela, sem pular linha
        
        previous = current  # Atualiza o anterior
        current = next_fibonacci  # Atualiza o atual
    print()  # Pula a linha, para não quebrar o programa