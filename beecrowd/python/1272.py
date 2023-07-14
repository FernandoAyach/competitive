# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Le o número de casos de teste, converte em inteiro, pelo int() e atribui para n.
 (2) Inicia um loop for que percorre o numero de casos de teste. A cada repetição:
     (3) Le a mensagem completa pelo input() e atribui para full_message.
     (4) Inicia variável true_message com valor '' para armazenar a mensagem final.
     (5) Inicia variável word com valor '' para armazenar a a palavra atual.
     (6) Inicia um loop for que percorre a string full message. A cada repetição:
         (7) Se o caracter for uma letra, concatena em word.
         (8) Senão, verifica se já tem uma palavra, se sim, concatena a primeira letra de word
         em true message. Em ambos os casos, reatribui '' para word
    (9) Se a frase acabou sem espaços e há uma palavra formada, adiciona a primeira letra para true_message.
    (10) Imprime a mensagem na tela
'''

n = int(input())  # Le o número de casos de teste 

for i in range(n):  # Inicia um loop de intervalo [0, n)
    full_message = input()  # Le a mensagem completa

    true_message = ''  # Variável para a mensagem final
    word = ''  # Palavra atual
    for character in full_message:  # Inicia um loop que percorre a mensagem
        
        if character != ' ':  # Se for uma letra 
            word += character  # Adiciona na palavra
        else:  # Senão, for um espaço
            if word != '':  # Se a palavra já tiver letras
                true_message += word[0]  # Adiciona a primeira letra na mensagem final
            word = ''  # Reinicia a palavra
            
    if word != '':  # Se a mensagem acabou sem espaços e tem uma palavra
        true_message += word[0]  # # Adiciona a primeira letra na mensagem final
        
    print(true_message)  # Imprime a mensagem final
    
