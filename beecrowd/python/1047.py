# -*- coding: utf-8 -*-

'''
Coleta os valores dos horários inicial e final, na mesma linha,
separado por espaços.
Converte-os para inteiro.
Para calcular, teremos dois casos de análise:

Se jogo ocorreu em exatamente um dia: são 24 horas de jogo.
Se Jogo ocorreu em dois dias diferentes: Converte os dois horários para minutos.
O tempo do jogo será dado pelo tempo do primeiro dia (Dia em minutos - horário em minutos) +
tempo do segundo dia em minutos. Converte os valores para horas e minutos após isso.
Se jogo ocorreu dentro de um dia: Converte os dois horários para minutos e
subtrai o valor do horário final do inicial. Converte os minutos resultantes
para horas e minutos.

Imprime resultado na tela.
'''

init_hour, init_min, final_hour, final_min = input().split()  # Coleta os valores, na mesma linha, separados por espaço
init_hour = int(init_hour)  # Converte a hora inicial para inteiro
init_min = int(init_min)  # Converte o minuto inicial para inteiro
final_hour = int(final_hour)  # Converte a hora final para inteiro
final_min = int(final_min)  # Converte o minuto final para inteiro

init_time_in_minutes = init_hour*60 + init_min  # Inicio do jogo em minutos
final_time_in_minutes = final_hour*60 + final_min  # Final do jogo em minutos
DAY_IN_MINUTES = 1440  # Dia completo em minutos
    
if init_time_in_minutes == final_time_in_minutes:  # Jogo durou um dia
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')  # Imprime duração do jogo
else:
    game_time_in_minutes = 0  # Inicia variável para quantificar o tempo do jogo em minutos
    
    if init_time_in_minutes > final_time_in_minutes:  # Jogo em dias diferentes
        game_time_in_minutes = (DAY_IN_MINUTES - init_time_in_minutes) + final_time_in_minutes  # Calcula o tempo do jogo em minutos
    else:  # Jogo no mesmo dia
        game_time_in_minutes = final_time_in_minutes - init_time_in_minutes  # Calcula o tempo do jogo em minutos

    # Conversão
    game_total_hours = game_time_in_minutes // 60  # Converte o tempo em horas
    game_total_minutes = game_time_in_minutes % 60 # Coleta os minutos restantes
 
    # Saída
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(game_total_hours, game_total_minutes))  # Imprime duração do jogo
