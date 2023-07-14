# -*- coding: utf-8 -*-

'''
Coleta 3 valores reais, na mesma linha, separado por espaços.
Verifica se correspondem a um triângulo, se sim, imprime o perímetro desse na tela.
Caso contrário, é um trapézio, imprime a área desse na tela.
'''

a, b, c = input().split()  # Coleta 3 valores, na mesma linha, separado por espaços
a = float(a)  # Converte o primeiro lado em inteiro
b = float(b)  # Converte o segundo lado em inteiro
c = float(c)  # Converte o terceiro lado em inteiro

if(a < b + c and b < a + c and c < a + b):  # Verifica se é um triâgulo
    print('Perimetro = {:.1f}'.format(a + b + c))  # É um triângulo, calcula e imprime o perímetro
else:  # Não é um triângulo, e sim, um trapézio
    print('Area = {:.1f}'.format(((a + b) * c) / 2)) # Não é um triângulo, calcula e imprime o área do trapézio