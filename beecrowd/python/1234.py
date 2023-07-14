# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Inicia um loop while infinito. A cada repetição:
     (2) Tenta ler uma entrada pelo input() e atribui para sentence.
     (3) Se der EOFError, acabaram as entradas, portanto para o loop, com break.
     (4) Inicia variável booleana last_was_upper com valor inicial falso, indicando que
     o primeiro caracter não é maiusculo.
     (5) Inicia uma string vazia dancing_sentence para armazenar a sentença dançante.
     (6) Cria um laço for que percorre todos os caracteres de sentence. A cada caracter:
         (7) Se for espaço, adiciona em dancing_sequence, sem modificações.
         (8) Senão se, last_was_upper for verdadeiro, adiciona o caracter em dancing_sequence
         com formatação minuscula, pela função lower(). Além disso, atualiza last_was_upper para false.
         (9) Senão, e last_was_upper for falso, adiciona o caracter em dancing_sequence
         com formatação maiuscula, pela função upper(). Além disso, atualiza last_was_upper para true.
     (10) Imprime dancing_sequence.
'''

while True:  # Inicia um loop infinito
    
    try: 
        sentence = input()  # Tenta ler uma sentença
    except EOFError:  # Se não houver mais entradas
        break  # Para o loop
    
    last_was_upper = False  # O último caracter não era maiusculo
   
    dancing_sequence = ""  # Inicia a sentença dançante
    
    for char in sentence:  # Para cada caracter da sentença original
        
        if char == " ":  # Se for espaço
            dancing_sequence += char  # Adiciona o espaço
        elif last_was_upper:  # Senão se, o último caracter foi maiusculo
            dancing_sequence += char.lower()  # Adiciona o caracter minusculo
            last_was_upper = False  # O ultimo caracter não foi maiusculo, a partir de agora
        else:  # Senão foi maiusculo
            dancing_sequence += char.upper()  # Adiciona o caracter maiusculo
            last_was_upper = True  # O ultimo caracter foi maiusculo, a partir de agora
    print(dancing_sequence)  # Imprime a sentença dançante