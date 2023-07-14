# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Le o número de casos de teste, converte em inteiro, pelo int(), e atribui para a variável t.
 (2) Inicia um loop for que repete t vezes. A cada repetição:
     (3) Le uma expressão, na mesma linha, separado por "!", pelo input().split(), e atribui para expression.
     (4) Obtem o número desejado pela indexação expresion[0], converte em inteiro pelo int(), e atribui para n.
     (5) Calcula o número de ! pela diferença do total de termos por 1 (número obtido).
     (6) Inicia uma variável response com valor inicial n para armazenar a resposta.
     (7) Inicia um iterador com valor 1 i.
     (8) Cria um loop infinito while. A cada repetição:
         (9) Calcula o próximo termo n - (k * i) e atribui para next_term.
         (10) Se o resultado for maior ou igual a 1, faz response *= next_term e incrementa o contador.
         (11) Senão, para o loop while com break.
     (12) Imprime a resposta na tela
'''

t = int(input())  # Le o número de casos de teste

for i in range(t):  # Loop que repete o número de casos de teste
    
    expression = input().split("!")  # Le a expressao inicial e separa o número dos "!"
    n = int(expression[0])  # Obtem o número
    k = len(expression) - 1  # Calcula o número de "!"
    
    response = n  # Variável que armazena a resposta, inicia com o numero
    
    i = 1  # Iterador começando por 1
    while True:  # Loop infinito
        next_term = n - (k * i)  # Calcula o próximo termo
        
        if next_term >= 1:  # Se for maior ou igual a 1
            response *= next_term  # Multiplica na resposta
            i += 1  # Incrementa o iterador
        else:  # Senão
            break  # Para o loop
    print(response)  # Imprime o resultado
        