# -*- coding: utf-8 -*-

'''
Entrada:
 (1) Coleta um número, em uma linha, pelo input(), converte em inteiro, pelo int() e
 atribui para a variável number.

Desenvolvimento + Saída:
 (1) Inicia um laço de intervalo em que i assume [1, 11) pela estrutura for
 (2) Imprime, em cada execução, iterador x number = number * 1
'''

number = int(input())

for i in range(1, 11):
    print(i, 'x', number, '=', number * i)