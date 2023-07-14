# -*- coding: utf-8 -*-

'''
Coleta o valor total da duração em segundos, converte em inteiro.
Coleta a quantidade de horas usando a divisão inteira entre os segundos e 3600 (sec em hora).
Recolhe o resto de segundos e faz o mesmo processo anterior, agora divindo por 60 para obter os minutos.
Recolhe o resto da divisão, esse será os segundos restantes, respeitando: [0,60).
Imprime mensagem na tela.
'''

seconds = int(input()) # Coleta os segundos e converte em inteiro

hours = seconds // 3600 #Calcula a quantidade de horas

seconds = seconds % 3600 #Coleta o resto da divisão e atualiza os segundos

minutes = seconds // 60 #Calcula a quantidade de minutos

seconds = seconds % 60 #Com o resto da divisão anterior, obtem-se os segundos restantes

print('{}:{}:{}'.format(hours, minutes, seconds)) #Imprime mensagem na tela

