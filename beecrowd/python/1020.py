# -*- coding: utf-8 -*-

'''
Entrada:
 - Coleta a idade em dias, em uma linha, converte em inteiro
 e atribui para a variável age_in_days.

Desenvolvimento:
 - Para calcular a idade em anos, meses e dias, utiliza-se do
 mecanismo de divisões e restos inteiros.
  - Sendo assim, para cada caso, divide-se a idade em dias pela
  quantidade respectiva de dias em cada formato de tempo (ano e mes).
 - Atribui o valor obtido para uma variável.
 - Após isso, coleta o resto da divisão anterior, atualizando
 a quantidade de dias restante, para ser utilizada na próxima.
 - Faz isso até que o resto da divisão seja a quantidade de dias restantes.
 
Saída:
 - Imprime, em linhas diferentes, a quantidade de anos, meses e dias da idade.
'''

age_in_days = int(input())  # Coleta a idade completa em dias, em inteiro

age_in_years = age_in_days // 365  # Calcula a quantidade de anos
age_in_days = age_in_days % 365  # Coleta o resto de dias

age_in_months = age_in_days // 30  # Calcula a quantidade de meses
age_in_days = age_in_days % 30  # Resto de dias restantes, sendo que 0 <= x < 30

print('{} ano(s)'.format(age_in_years))  # Imprime a quantidade de anos
print('{} mes(es)'.format(age_in_months))  # Imprime a quantidade de meses
print('{} dia(s)'.format(age_in_days))  # Imprime a quantidade de dias

