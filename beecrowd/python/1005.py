# -*- coding: utf-8 -*-

'''
Coleta as notas do aluno, converte em real e atribui em variáveis.
Calcula a média ponderada das notas, considerando seus pesos.
Imprime mensagem na tela com aproximação de 5 casas decimais.
'''

n1 = float(input()) #Coleta a primeira nota, em real
n2 = float(input()) #Coleta a segunda nota, em real
average = (n1*3.5 + n2*7.5) / 11 #Calcula a média

print('MEDIA = {:.5f}'.format(average)) #Imprime na tela com 5 casas decimais
