# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Le o valor de casos de testes, converte em inteiro, pelo int() e atribui para n.
 (2) Coleta a sequência de números, na mesma linha, separados por espaços, pelo input().split()
 e atribui para numbers.
 (3) Inicia variável smallest para armazenar o menor valor de referência, nesse caso, o numbers[0], convertido
 em inteiro.
 (4) Inicia variável para armazenar a posição do menor valor até então, nesse caso, 0.
 (5) Inicia um iterator i com valor 1.
 (6) Inicia um loop while de intervalo [1, n). A cada repetição:
     (7) Verifica se numbers[i] < smallest, se for o caso, atribui o número atual para smallest e
     atribui sua posição para position.
     (8) Incrementa i em 1.
 (9) Imprime o valor do menor número, em uma linha.
 (10) Imprime o valor de sua posição, em outra.
'''

n = int(input())  # Le o número de casos de teste

numbers = input().split()  # Le todos os números, na mesma linha, separados por espaços

smallest = int(numbers[0])  # Le um valor de referência, nesse caso, o primeiro, para ser o menor
position = 0  # Armazena a posição do menor

i = 1  # Iterator com valor 1, pois ja lemos o 0
while i < n:  # Inicia loop de intervalo [0, n)
    numbers[i] = int(numbers[i])  # Converte o valor do número em inteiro
    
    if numbers[i] < smallest:  # Se for menor que o menor
        smallest = numbers[i]  # Este será o novo menor
        position = i  # Armazena a posição
    i += 1  # Incrementa o iterador
print('Menor valor:', smallest)  # Imprime o valor do menor número
print('Posicao:', position)  # Imprime sua posição