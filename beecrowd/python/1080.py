# -*- coding: utf-8 -*-

'''
Entrada + Desenvolvimento:
 (1) Inicia variável bigger, com valor zero, para armazenar o maior valor
 (2) Inicia variável position, com valor zero, para armazenar a posição do maior valor
 (3) Inicia uma variável de contador i, com valor inicial 1
 (4) Cria um loop while de i <= 100, realizando em cada repetição, a coleta do valor do usuário,
 pelo input, convertendo em inteiro, pelo int(), e armazenando na variável number.
 (5) Dentro desse loop, se number for maior que bigger, atribui o valor de number à bigger e armazena
 a posição i do number.
 (6) Incrementa o valor de i em 1.

Saída:
 (1) Imprime, em uma linha, o maior valor.
 (2) Imprime, em outra linha, a posição.

'''

bigger = 0  # Inicia variável de maior
position = 0  # Inicia variável da posição do maior

i = 1  # Inicia contador com 1
while(i <= 100):  # Percorre [i, 100]
    number = int(input())  # Coleta um número inteiro
    
    if number > bigger:  # Se o número for maior que o maior
        bigger = number  # Este será o maior
        position = i  # Arnazena a posição
    i += 1  # Incrementa o iterador

print(bigger)  # Imprime o maior
print(position)  # Imprime a posição do maior