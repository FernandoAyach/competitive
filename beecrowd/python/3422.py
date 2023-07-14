# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Coleta o número de casos de teste, em uma linha, converte em inteiro pelo int() e atribui para a
 variável n.
 (2) Cria constantes FIRST_TURN_TIME, SECOND_TURN_TIME armazenando os tempos totais da partida
 até aquele momento, respectivamente 45 e 90.
 (3) Cria um loop for de intervalo [0, n). Em cada execução:
     (4) Coleta o tempo da partida e o turno, na mesma linha, separados por espaços, pelo input().split() e atribui
     para time e turn.
     (5) Converte time para inteiro pelo int() e atualiza variável.
     (6) Se for o primeiro turno, verifica se o tempo é <= FIRST_TURN_TIME, nesse caso, não há prorrogação e imprime o tempo
     na tela. No caso de ter prorrogação, imprime FIRST_TURN_TIME, (time - FIRST_TURN_TIME), sep = '+', sendo '(time - FIRST_TURN_TIME)
     o tempo da prorrogação' e 'sep = +' como forma de trocar os espaços por +.
     (7) Senão for o primeiro turno, atualiza a variável time com o valor do FIRST_TURN_TIME.
     (8)Verifica se o tempo é <= SECOND_TURN_TIME, nesse caso, não há prorrogação e imprime o tempo
     na tela. No caso de ter prorrogação, imprime SECOND_TURN_TIME, (time - SECOND_TURN_TIME), com 'sep = +'
'''

n = int(input())  # Coleta o número de casos de teste, em inteiro
FIRST_TURN_TIME = 45  # Constante de tempo do primeiro turno
SECOND_TURN_TIME = 90  # Constante de tempo do segundo turno

for i in range(n):  # Loop que repete n vezes
    
    # Coleta o tempo e o turno da partida, na mesma linha, separados por espaços
    time, turn = input().split()  
    time = int(time)  # Converte time para inteiro
    
    if turn == '1T':  # Se for o primeiro turno
        
        if time <= FIRST_TURN_TIME:  # Se não há prorrogação
            print(time)  # Imprime time
        else:  # Senão, tiver prorrogação
            print(FIRST_TURN_TIME, (time - FIRST_TURN_TIME), sep = '+')  # Imprime tempo da partida+tempo da prorrogação
    else:  # Senão, for o segundo turno
        
        time += FIRST_TURN_TIME  # Incrementa o tempo do primeiro turno em time
        if time <= SECOND_TURN_TIME:  # Se não há prorrogação
            print(time)  # Imprime time
        else:  # Senão, tiver prorrogação
            print(SECOND_TURN_TIME, (time - SECOND_TURN_TIME), sep = '+')  # Imprime tempo da partida+tempo da prorrogação
        