# -*- coding: utf-8 -*-

'''
Coleta 3 valores a, b e c, na mesma linha, separada por espaços,
e armazena-os em variáveis.
Faz a conversão de cada valor para inteiro e atualiza as variáveis.
Define, inicialmente, a como maior.
Se b for maior que a e que c, b é o maior, então atribui na variável de maior.
Se c for maior que a e que b, c é o maior, então atribui na variável de maior.
Imprime o maior na tela.
'''

a, b, c = input().split()  # Coleta o 3 valores na mesma linha, separado por espaços
a = int(a)  # Converte a em inteiro
b = int(b)  # Converte b em inteiro
c = int(c)  # Converte c em inteiro

bigger = a  # Inicia o maior como a

if b > a and b > c:  # Verifica se b é o maior
    bigger = b  # Define b como maior, caso sim
elif c > a and c > b:  # Verifica se c é o maior
    bigger = c  # Define c como maior, caso sim

print(bigger, 'eh o maior')  # Imprime maior na tela