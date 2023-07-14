# -*- coding: utf-8 -*-

'''
Entrada:
 - Coleta o valor, em uma linha, converte em real e atribui para a
 variável value.

Desenvolvimento + Saída:
 - Para encontrar o intervalo que o valor se situa, utiliza-se
 de cláusulas condicionais e o operador and.
 - Se for maior ou igual a zero e menor ou igual a 25, é do intervalo: [0,25], imprime o intervalo
 - Se for maior que 25 e maior ou igual a 50, é do intervalo: (25,50], imprime o intervalo
 - Se for maior que 50 e maior ou igual a 75, é do intervalo: (50,75], imprime o intervalo
 - Se for maior que 75 e maior ou igual a 100, é do intervalo: (75,100], imprime o intervalo
 - Senão, está fora de intervalo, imprime Fora de intervalo
'''

value = float(input())  # Coleta o valor, em real

if value >= 0 and value <= 25:  # Verifica se é [0,25]
    print('Intervalo [0,25]')  # Imprime o intervalo na tela
elif value > 25 and value <= 50:  # Verifica se é (25,50]
    print('Intervalo (25,50]')  # Imprime o intervalo na tela
elif value > 50 and value <= 75:  # Verifica se é (50,75]
    print('Intervalo (50,75]')  # Imprime o intervalo na tela
elif value > 75 and value <= 100:  # Verifica se é (75,100]
    print('Intervalo (75,100]')  # Imprime o intervalo na tela
else:
    print('Fora de intervalo') # Imprime que não está em nenhum intervalo
    