# -*- coding: utf-8 -*-

'''
Entrada:
 (1) Coleta o valor de N, em uma linha, pelo input(), converte para inteiro, pelo int(),
e atribui para variável N.

Desenvolvimento + Saída:
 (1) Calcula o valor peças pela fórmula ((N+1)*(N+2))/2, converte em inteiro e imprime na tela.
'''

N = int(input())  # Coleta o valor de N

print(int(((N+1)*(N+2))/2))  # Calcula a quantidade de peças e mostra na tela, sem .0