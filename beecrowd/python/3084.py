# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Define constantes HOUR_IN_ANGLE e MINUTE_IN_ANGLE, armazenando, respectivamente 30 e 6, para
 representar a angulação respectiva de um hora e de um minuto.
 (2) Inicia um loop infinito while. Dentro de cada loop:
     (3) Realiza uma estrutura try except, se conseguir obter hours_angle e minutes_angle, na mesma linha,
     separado pos espaços, pelo input().split(), segue o código naturalmente.
     (4) Caso contrário, captura EOFError, as entradas acabaram, para o loop com break.
     (5) Converte hours_angle e minutes_angle para inteiro, atualiza as variáveis
     (6) Calcula a quantidade de horas por hours_angle // HOUR_IN_ANGLE.
     (7) Calcula a quantidade de minutos por minutes_angle // MINUTE_IN_ANGLE
     (8) Mostra o resultado na tela com o format. Cada valor terá largura dois e com preenchimento
     de zeros à esquerda, portanto, caso for 1 dígito, o format preencherá automaticamente com 0.
'''

HOUR_IN_ANGLE = 30  # Define constante para a angulação da hora
MINUTE_IN_ANGLE = 6  # Define constante para a angulação do minuto
while True:  # Inicia um loop infinito
    
    try:  # Tenta executar o código abaixo
        # Coleta a angulação das horas e dos minutos, na mesma linha, separados por espaços
        hours_angle, minutes_angle = input().split()  
    except EOFError:  # Se deu EOFError, acabaram as entradas
        break  # Para o loop
    
    hours_angle = int(hours_angle)  # Converte hours_angle para inteiro
    minutes_angle = int(minutes_angle)  # Converte minutes_angle para inteiro

    hours = hours_angle // HOUR_IN_ANGLE  # Calcula a quantidade de horas
    minutes = minutes_angle // MINUTE_IN_ANGLE  # Calcula a quantidade de minutes
    
    # Mostra o resultado na tela com a formatação de 0 à esquerda, caso for menor que 2 dígitos
    print('{0:02d}:{1:02d}'.format(hours, minutes))  
