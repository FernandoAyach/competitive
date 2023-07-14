# -*- coding: utf-8 -*-

'''
Entrada:
 (1) Coleta um valor, em uma linha, pelo input(), converte para inteiro, pelo int(), e
 atribui para a variável number.

Desenvolvimento + Saída:
 (1) Se o número for ímpar, inicia um laço for que percorrerá o intervalo [number, number+12), em
 dois em dois, pois queremos somente os números ímpares. Detalhe que incluímos o number pois ele é ímpar. Imprime
 a cada iteração o próximo impar.
 (2) Senão, percorre um intervalo [number + 1, number + 13), em dois em dois, obtendo os impares a partir de number,
 sendo ele não incluido, pois é par. Imprime a cada iteração o próximo impar.
'''

number = int(input())  # Coleta um número inteiro

# Se for ímpar
if number % 2 != 0:
    
    # Percorre [number, number+12), em 2 em 2
    for i in range(number, number + 12, 2):
        print(i)  # Imprime impar na tela
# Senão
else:
    
    # Percorre [number + 1, number + 13), em 2 em 2
    for i in range(number + 1, number + 13, 2):
        print(i)  # Imprime impar na tela