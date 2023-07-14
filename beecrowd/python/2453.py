# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Coleta uma entrada entry pelo input().
 (2) Inicia uma variável previous_was_p com valor False, indicando que
 o último caracter não era p de repetição.
 (3) Cria uma string vazia message para armazenar a mensagem real.
 (4) Cria um loop for que percorre entry. A cada caracter:
     (5) Se for um p, mas não houve p de repetição antes dele, o último caracter é um p
     de repetição e não deve ser considerado, portanto atualiza previous_was_p para True.
     (6) Senão se for um p, mas houve p de repetição antes dele, último caracter não é um p de repetição
     e deve ser considerado, portanto atualiza previous_was_p para False e concatena o char em message.
     (7) Senão, for uma letra sem ser p ou espaço, concatena o char em message e atualiza previous_was_p para False.
 (8) Imprime a mensagem final
'''

entry = input()  # Coleta uma entrada pelo input()

previous_was_p = False  # Considera que o último caracter não era p de repetição

message = ""  # Cria uma string vazia para armazenar a mensagem real

for char in entry:  # Para cada caracter na entrada
    
    if char == "p" and not previous_was_p:  # Se for um p, mas não houve p de repetição antes dele
        previous_was_p = True  # O último caracter é um p de repetição e não deve ser considerado
    elif char == "p":  # Se for um p, mas houve p de repetição antes dele
        previous_was_p = False  # O último caracter não é um p de repetição, e deve ser considerado
        message += char  # Adiciona o caracter em mensagem
    else:  # Senão, for uma letra sem ser p ou espaço 
        message += char  # Adiciona na mensagem
        previous_was_p = False  # O último caracter não é p
print(message)  # Imprime a mensagem final
    