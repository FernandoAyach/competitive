# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Le o número de casos de teste, converte em inteiro, e atribui para n.
 (2) Cria um loop for que repete n vezes. A cada repetição:
     (3) Le uma frase e atribui para sentence.
     (4) Cria uma lista counter com 26 posições, valendo 0, para contar as letras.
     (5) Inicia um loop de intervalo [0, len(sentence)). A cada repetição:
         (6) Cria uma variável code com o valor do código ASCII do caracter em questão, pelo ord().
         (7) Se o código estiver entre 65 e 90, soma 32 em code.
         (8) Se o código estiver entre 97 e 122, incrementa 1 em counter na posição code - 97.
     (9) Inicia uma variável bigger com valor -1 para servir de referência de maior número.
     (10) Cria um loop for de intervalo [0, 25]. A cada repetição:
         (11) Se o counter[j] > bigger, atribui o valor de counter[j] para bigger.
     (12) Cria um loop for de intervalo [0, 25]. A cada repetição:
         (13) Se o counter[j] == bigger, imprime chr(j + 97), sem pular linha, com end = "".
     (14) Pula uma linha com print().
'''

n = int(input())  # Le o número de casos de teste

for i in range(n):  # Loop que repete n vezes
    sentence = input()  # Le a frase
    counter = [0]*26  # Inicia uma lista contadora com 26 posições
    
    for j in range(len(sentence)):  # Loop que percorre toda a sentença
        code = ord(sentence[j])  # Obtem o código do caracter
        
        if code >= 65 and code <= 90:  # Se for maiusculo
            code += 32  # Soma 32
            
        if code >= 97 and code <= 122:  # Se for minusculo
           counter[code - 97] += 1  # Soma um no contador, no indice do ord respectivo
    
    bigger = -1  # Define um maior de referência
    for j in range(26):  # Percorre as 26 posições do counter
        if counter[j] > bigger:  # Se counter[j] > bigger
            bigger = counter[j]  # bigger = counter[j]
            
    for j in range(26):  # Percorre as 26 posições do counter
        if counter[j] == bigger:  # Se counter[j] == bigger
             print(chr(j + 97), end = "")  # Imprime a letra na tela
    print()  # Pula a linha, por conta do end = ""
        