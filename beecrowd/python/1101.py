# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Inicia um loop infinito while. A cada repetição:
    (2) Coleta dois números, na mesma linha, separados por espaço, pelo input().split() e
    os atribui para as variáveis num1 e num2.
    (3) Converte num1 e num2 para inteiro, usando int(), e atualiza as respectivas variáveis.
    (4) Se um dos valores for menor ou igual a zero, para o loop com break.
    (5) Inicia variável num_sum para a soma dos valores.
    (6) Se num2 for menor que num1, troca os valores. É preciso realizar essa verificação para
    a utilização efetiva do loop for posteriormente.
    (7) Realiza um loop for de intervalo [num1, num2]. A cada repetição:
        (8) Soma o valor de i na variável num_sum
        (9) Imprime o valor de i na tela, sem pular linha, pelo end = ''.
    (10) Imprime a num_sum, com a sintaxe: 'Sum=<valor>'
'''

while True:  # Inicia loop infinito
    # Coleta dois números inteiros, na mesma linha, separados por espaços
    num1, num2 = input().split()  
    num1 = int(num1)  # Converte num1 para inteiro
    num2 = int(num2)  # Converte num2 para inteiro
    
    if num1 <= 0 or num2 <= 0:  # Se um dos valores for <= 0
        break  # Para o loop
    
    num_sum = 0  # Soma dos valores
    
    if num2 < num1:  # Garante que num1 é o menor valor, se num2 é menor
        aux = num1  # Armazena num1 em aux
        num1 = num2  # Atribui o valor de num2 em num1
        num2 = aux  # Atribui o valor de aux em num2
    
    for i in range(num1, num2 + 1):  # Loop de intervalo [num1, num2]
        num_sum += i  # Soma o valor de i em num_sum
        print(i, end = ' ')  # Imprime i
        
    print('Sum=', num_sum, sep = '')  # Imprime a soma dos valores
    
    