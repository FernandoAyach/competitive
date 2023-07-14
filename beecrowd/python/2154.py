# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Inicia um loop while infinito. A cada repetição:
     (2) Tenta ler um inteiro n, convertendo em inteiro.
     (3) Caso capturar EOFError, para o loop com break.
     (4) Le um polinômio, em uma mesma linha, separados por " + ", pelo input().split(" + ") e
     atribui para expression.
     (5) Cria uma lista vazia para armazenar a expressão derivada e atribui para derivated_expression.
     (6) Inicia um loop for de intervalo [0, len(expression)). A cada repetição:
         (7) Inicia uma variável new_term com uma string vazia para armazenar o termo derivado.
         (8) Inicia uma lista term para ler cada elemento do termo separados por x, pelo expression[i].split("x").
         (9) Inicia uma variável coeficient para armazenar o coeficiente do termo (term[0]), convertido
         em inteiro, pelo int().
         (10) Inicia uma variável exponent para armazenar o expoente do termo (term[1]), convertido
         em inteiro, pelo int().
         (11) Multiplica o coeficiente pelo expoente e atualiza a variável coeficient.
         (12) Decresce 1 na variável exponent.
         (13) Se exponent for maior que 1, concatena em new_term str(coeficient) + "x" + str(exponent).
         (14) Senão, concatena str(coeficient) + "x".
         (15) Concatena new_term em derivated_expression.
     (16) Imprime derivated_expression em forma de string, com os termos separados por " + ", pelo join().
'''

while True:  # Inicia um loop infinito
    
    try:  # Tenta
        n = int(input())  # Le um inteiro indicando a quantidade de termos
    except EOFError:  # Se não ouver mais entradas
        break  # Para o loop
    
    expression = input().split(" + ")  # Le um polinômio, em uma mesma linha, separados por " + "
    derivated_expression = []  # Cria uma lista para armazenar a expressão derivada
    
    for i in range(len(expression)):  # Loop que percorre a expressão
        new_term = ""  # Variável para armazenar o termo derivado
        term = expression[i].split("x")  # Coleta a expressão separada por x
        coeficient = int(term[0])  # Coleta o coeficiente
        exponent = int(term[1])  # Coleta o expoente
        
        coeficient *= exponent  # Multiplica o o coeficiente pelo expoente
        exponent -= 1  # Decresce o expoente em 1
        
        if exponent > 1:  # Se for um expoente maior que 1
            new_term += str(coeficient) + "x" + str(exponent)  # Concatena o coeficiente + x + expoente
        else:  # Senão
            new_term += str(coeficient) + "x"  # Concatena o coeficiente + x
        derivated_expression += [new_term]  # Adiciona o monômio na expressão
    
    print(" + ".join(derivated_expression))  # Junta a lista de monômios e imprime com um " + " entre eles.