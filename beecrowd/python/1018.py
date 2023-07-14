# -*- coding: utf-8 -*-

'''
Entrada:
 - Coleta a quantidade de dinheiro inteira, em uma linha, converte em inteiro
 e atribui para a variável full_money.
 
Desenvolvimento:
 - Para o cálculo das cédulas, utiliza-se o mecanismo de divisões e restos inteiros.
 - Para cada caso, divide o dinheiro total pelo valor da cédula e atribui para uma
 variável, essa contendo a quantidade daquela cédula.
 - Em seguida, atualiza a variável full_money com o resto da divisão anterior.
 - Faz esse processo até as notas de 1.

Saída:
 - Imprime, antes dos cálculos, a quantia total.
 - Imprime, em linhas diferentes, cada quantidade de cédulas obtidas.
'''

full_money = int(input())
print(full_money)

banknotes_100 = full_money // 100
full_money = full_money % 100

banknotes_50 = full_money // 50
full_money = full_money % 50

banknotes_20 = full_money // 20
full_money = full_money % 20

banknotes_10 = full_money // 10
full_money = full_money % 10

banknotes_5 = full_money // 5
full_money = full_money % 5

banknotes_2 = full_money // 2
banknotes_1 = full_money % 2

print('{} nota(s) de R$ 100,00'.format(banknotes_100))
print('{} nota(s) de R$ 50,00'.format(banknotes_50))
print('{} nota(s) de R$ 20,00'.format(banknotes_20))
print('{} nota(s) de R$ 10,00'.format(banknotes_10))
print('{} nota(s) de R$ 5,00'.format(banknotes_5))
print('{} nota(s) de R$ 2,00'.format(banknotes_2))
print('{} nota(s) de R$ 1,00'.format(banknotes_1))
