# -*- coding: utf-8 -*-

'''
Coleta 4 valores e converte-os em inteiro.
Imprime "Valores aceitos" na tela se B > C, D > A, C + D > A + B, C e D forem positivos e A for par.
Caso contrário, imprime "Valores nao aceitos".
'''

a, b, c, d = input().split()  # Coleta a entrada inteira e insere nas variáveis
a = int(a)  # Converte a para inteiro
b = int(b)  # Converte b para inteiro
c = int(c)  # Converte c para inteiro
d = int(d)  # Converte d para inteiro

if(b > c and d > a and c + d > a + b and c > 0 and d > 0 and (a % 2 == 0)):  # Se cumprir as condições, os valores são aceitos
    print("Valores aceitos")  # Imprime resultado na tela
else:  # Caso contrário, não é aceito
    print("Valores nao aceitos")  #  Imprime resultado na tela