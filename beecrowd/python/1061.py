# -*- coding: utf-8 -*-

'''
Entrada:
 (1) Coleta o prefixo (que só nos serve para possibilar o uso do input().split(), não iremos usá-lo) e
 o dia inicial, na mesma linha, separado por "Dia ", pelo input().split() e armazena nas variáveis prefix
 e init_day.
 (2) Converte init_day em inteiro e atualiza a variável.
 (3) Coleta o valor da hora, minuto e segundo inicial, na mesma linha, separado por " : ", pelo input().split()
 e atribui para as variáveis init_hour, init_minute e init_second.
 (4) Converte cada uma dessas variáveis para inteiro, atualizando seu valor, logo em seguida.
 (5) Realiza o mesmo processo para o dia final e o horário final, com a diferença que o valor do dia final é atribuído
 para final_day e o restante do horário para final_hour, final_minute e final_second.

Desenvolvimento:
 (1) Inicia constantes DAY_IN_SECONDS, HOUR_IN_SECONDS, MINUTES_IN_SECONDS, FIRST_DAY para facilitar a leitura do cálculo seguinte. As
 três primeiras são os valores do dia, hora e minutos em segundos. Já a última representa a unidade do primeiro dia. Usaremos os cálculos em
 segundos para universalizar as unidades do calculo.
 (2) Calcula o tempo do primeiro dia subtraindo o dia em segundos pelo horário inicial em segundos. Atribui o valor para init_time_in_seconds.
 (3) Calcula o tempo do último dia convertendo o horário final em segundos. Atribui o valor para final_time_in_seconds.
 (4) Calcula os dias intermediários subtraindo o final pelo inicial, descartando 1, que representa o primeiro dia. Atribui o valor para intermediate_days.
 (5) Soma o total de segundos do primeiro e do segundo dia e atribui para total_time_in_seconds.
 (6) Tendo o valor total em segundos, basta converter para dia, hora, minuto e segundo. Para isso, utiliza-se o mecanismo das divisões inteiras e restos.
 (7) Os valores totais do dia, hora, minuto e segundos são atribuidos para as variáveis total_days, total_hours, total_minutes e total_time_in_seconds,
 respectivamente.

Saída:
 (1) Imprime o valor dos dias, horas, minutos e segundos totais, um em cada linha.

'''
# Entrada -------------------------------------------------------------------------------------------

prefix, init_day = input().split('Dia ')  # Coleta o prefixo e o valor do primeiro dia, na mesma linha, separado por "Dia "
init_day = int(init_day)  # Converte o dia em inteiro

# Coleta o valor da hora, minuto e segundo inicial, na mesma linha, separado por " : "
init_hour, init_minute, init_second = input().split(' : ')  
init_hour = int(init_hour)  # Converte a hora inicial em inteiro
init_minute = int(init_minute)  # Converte o minuto inicial em inteiro
init_second = int(init_second)  # Converte o segundo inicial em inteiro

prefix, final_day = input().split('Dia ')  # Coleta o prefixo e o valor do último dia, na mesma linha, separado por "Dia "
final_day = int(final_day)  # Converte o dia em inteiro

# Coleta o valor da hora, minuto e segundo final, na mesma linha, separado por " : "
final_hour, final_minute, final_second = input().split(' : ')
final_hour = int(final_hour)  # Converte a hora final em inteiro
final_minute = int(final_minute)  # Converte o minuto final em inteiro
final_second = int(final_second)  # Converte o segundo final em inteiro

# Cálculo em segundos -------------------------------------------------------------------------------------------

DAY_IN_SECONDS = 86400  # Dia em segundos
HOUR_IN_SECONDS = 3600  # Hora em segundos
MINUTES_IN_SECONDS = 60  # Minuto em segundos
FIRST_DAY = 1  # Primeiro dia

# Cálculo do tempo de evento do primeiro dia
init_time_in_seconds =  DAY_IN_SECONDS - (init_hour * HOUR_IN_SECONDS + init_minute * MINUTES_IN_SECONDS + init_second)

# Cálculo do tempo de evento do último dia
final_time_in_seconds =  final_hour * HOUR_IN_SECONDS + final_minute * MINUTES_IN_SECONDS + final_second

# Cálculo dias dias intermediários
intermediate_days =  (final_day - init_day) - FIRST_DAY

# Tempo total do primeiro e segundo dia, em segundos
total_time_in_seconds = init_time_in_seconds + final_time_in_seconds

# Conversão -----------------------------------------------------------------------------------

total_days = (total_time_in_seconds // DAY_IN_SECONDS) + intermediate_days  # Total de dias
total_time_in_seconds = total_time_in_seconds % DAY_IN_SECONDS  # Resto de segundos

total_hours = total_time_in_seconds // HOUR_IN_SECONDS  # Total de horas
total_time_in_seconds = total_time_in_seconds % HOUR_IN_SECONDS  # Resto de segundos

total_minutes = total_time_in_seconds // MINUTES_IN_SECONDS  # Total de minutos
total_time_in_seconds = total_time_in_seconds % MINUTES_IN_SECONDS  # Total de segundos

# Saída --------------------------------------------------------------------------------------

print(total_days, 'dia(s)')  # Imprime o total de dias
print(total_hours, 'hora(s)')  # Imprime o total de horas
print(total_minutes, 'minuto(s)')  # Imprime o total de minutos
print(total_time_in_seconds, 'segundo(s)')  # Imprime o total de segundos
