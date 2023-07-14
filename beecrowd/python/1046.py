# -*- coding: utf-8 -*-

'''
Coleta hora inicial e final, numa mesma linha, separado por espaços.
Converte a hora inicial e a final em inteiro.
Para o cálculo do evento, analisam-se 3 possibilidades:
Hora inicial maior que a final:
Nesse caso, o jogo é realizado em um período dentre 2 dias, assim, calcula-se o tempo do primeiro dia,
subtraindo 24 da hora inicial e soma com o período do segundo dia, que é o horário final em si.
Hora inicial menor que a final:
Nesse caso, o jogo é feito em 1 dia. Basta, então, subtrair a hora final da inicial
Hora inicial igual a final:
Nesse caso, o jogo durou um dia inteiro, ou seja, 24 horas.
'''

initHour, finishHour = input().split()  # Coleta os valores, na mesma linha, separados por espaços.
initHour = int(initHour)  # Converte a hora inicial em inteiro
finishHour = int(finishHour)  # Converte a hora final em inteiro

if(initHour > finishHour):  # Verifica se durou 2 dias
    print('O JOGO DUROU {} HORA(S)'.format((24 - initHour) + finishHour))  # Faz o cálculo do evento e imprime na tela
elif(initHour < finishHour):  # Verifica se durou 1 dia
    print('O JOGO DUROU {} HORA(S)'.format(finishHour - initHour))  # Faz o cálculo do evento e imprime na tela
else:  # O jogo durou exatamente 1 dia
    print('O JOGO DUROU 24 HORA(S)')  # O dia durou 24 horas, imprime na tela.