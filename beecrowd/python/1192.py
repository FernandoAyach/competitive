# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Le o número de casos de teste, converte em inteiro, pelo int() e atribui para n.
 (2) Cria um loop for de intervalo [0, n). A cada repetição:
     (3) Coleta uma expressão pelo input() e atribui para expression.
     (4) Obtem o primeiro número por indexação [0] em expression, converte em inteiro, pelo int(),
     e atribui para n1.
     (5) Obtem a letra por meio da indexação [1] em expression, atribui para letter.
     (6) Obtem o segundo número por indexação [2] em expression, converte em inteiro, pelo int(),
     e atribui para n2.
     (7) Se n1 == n2, então imprime a multiplicação desses números.
     (8) Senão se letter for minúscula, então imprime a soma dos números.
     (9) Senão, imprime a diferença de n1 em n2.
'''

n = int(input())  # Coleta o número de casos de teste

for i in range(n):  # Cria um loop que repete n vezes
    
    expression = input()  # Coleta a expressão
    n1 = int(expression[0])  # Obtem o primeiro numero
    letter = expression[1]  # Obtem a letra
    n2 = int(expression[2])  # Obtem o segundo numero
    
    if n1 == n2:  # Se forem números iguais
        print(n1 * n2)  # Imprime a multiplicação dos números
    elif letter.islower():  # Senão se a letra for minuscula
        print(n1 + n2)  # Imprime a soma dos numeros
    else:  # Senão, for maiuscula
        print(n2 - n1)  # Imprime a diferença do n2 com n1