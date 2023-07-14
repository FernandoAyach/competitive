# -*- coding: utf-8 -*-

'''
Coleta 2 valores inteiro na mesma linha, separado por espaços.
Se o resto da divisão inteira entre eles for 0, são múltiplos. Imprime na tela.
Caso contrário, não são. Imprime na tela.
'''

a, b = input().split()  # Coleta 2 valores, na mesma linha, separados por espaços
a = int(a)  # Converte o primeiro valor em inteiro
b = int(b)  # Converte o segundo valor em inteiro

if(a % b == 0 or b % a == 0):  # Verifica se são múltiplos
    print('Sao Multiplos')  # Imprime na tela
else: # Não são múltiplos
    print('Nao sao Multiplos')  # Imprime na tela