# -*- coding: utf-8 -*-

'''
Coleta as 3 notas do aluno, em real.
Calcula a média ponderada das notas.
Imprime na tela com 1 casa decimal.
'''

n1 = float(input())  # Coleta a nota 1
n2 = float(input())  # Coleta a nota 2
n3 = float(input())  # Coleta a nota 3

average = (n1*2 + n2*3 + n3*5) / 10  # Calcula a média ponderada

print('MEDIA = {:.1f}'.format(average))  # Imprime resultado na tela com 1 casa decimal