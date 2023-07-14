# -*- coding: utf-8 -*-

'''
Entrada:
 (1) Coleta 5 valores na mesma linha, separados por espaços, pelo input().split() e
 atribiu para as variáveis c1, c2, c3, c4 e c5.
 (2) Converte cada valor para inteiro, pelo método int(), e atualiza sua respectiva variável.

Desenvolvimento + Saída:
 (1) Se sempre o próximo número da sequência for maior que o anterior, é crescente. Imprime C.
 (2) Se sempre o próximo número da sequência for menor que o anterior, é decrescente. Imprime D.
 (3) Senão, está desordenado. Imprime N.
'''

# Coleta 5 valores na mesma linha, separados por espaços
c1, c2, c3, c4, c5 = input().split()  
c1 = int(c1)  # Converte c1 para inteiro
c2 = int(c2)  # Converte c2 para inteiro
c3 = int(c3)  # Converte c3 para inteiro
c4 = int(c4)  # Converte c4 para inteiro
c5 = int(c5)  # Converte c5 para inteiro

# Se os valores são crescentes
if c2 > c1 \
    and c3 > c2 \
    and c4 > c3 \
    and c5 > c4:
    # Imprime C na tela
        print('C')
# Se os valores são decrescentes
elif c2 < c1 \
    and c3 < c2 \
    and c4 < c3 \
    and c5 < c4:
    # Imprime D na tela
        print('D')
# Se não forem crescentes nem descrecentes
else:
    # Imprime N na tela
    print('N')



