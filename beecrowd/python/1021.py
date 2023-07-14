# -*- coding: utf-8 -*-

'''
Coleta o valor completo, em real.
Para calcular a quantidade notas e moedas do valor, utilizam-se de
divisões inteiras e restos, seguindo o processo:
valor_completo // valor_nota, para obter a quantidade de cédulas
valor_completo % valor_nota, para obter o resto da divisão anterior
e reiniciar o processo.
Imprime as quantidades no final.
'''

full_value = float(input()) # Coleta o valor completo, em float

# NOTAS

bank_notes_100 = int(full_value // 100)  # Quantidade de notas de 100
full_value = full_value % 100 # Resto da divisão por 100

bank_notes_50 = int(full_value // 50)  # Quantidade de notas de 50
full_value = full_value % 50 # Resto da divisão por 50

bank_notes_20 = int(full_value // 20)  # Quantidade de notas de 20
full_value = full_value % 20 # Resto da divisão por 20

bank_notes_10 = int(full_value // 10)  # Quantidade de notas de 10
full_value = full_value % 10 # Resto da divisão por 10

bank_notes_5 = int(full_value // 5)  # Quantidade de notas de 5
full_value = full_value % 5 # Resto da divisão por 5

bank_notes_2 = int(full_value // 2)  # Quantidade de notas de 2
full_value = full_value % 2 # Resto da divisão por 2

# MOEDAS

coins_1 = int(full_value // 1)  # Quantidade de moedas de 1
full_value = round(full_value % 1, 2)  # Resto da divisão por 1

coins_05 = int(full_value // 0.5)  # Quantidade de moedas de 0.5
full_value = round(full_value % 0.5, 2)  # Resto da divisão por 0.5

coins_025 = int(full_value // 0.25)  # Quantidade de moedas de 0.25
full_value = round(full_value % 0.25, 2)  # Resto da divisão por 0.25

coins_010 = int(full_value // 0.10)  # Quantidade de moedas de 0.10
full_value = round(full_value % 0.10, 2)  # Resto da divisão por 0.10

coins_005 = int(full_value // 0.05) # Quantidade de moedas de 0.005
full_value = round(full_value % 0.05, 2)  # Resto da divisão por 0.005

coins_001 = int(full_value / 0.01)  # Quantidade de moedas de 0.01

# Imprime a quantidade de cada nota
print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(bank_notes_100))
print('{} nota(s) de R$ 50.00'.format(bank_notes_50))
print('{} nota(s) de R$ 20.00'.format(bank_notes_20))
print('{} nota(s) de R$ 10.00'.format(bank_notes_10))
print('{} nota(s) de R$ 5.00'.format(bank_notes_5))
print('{} nota(s) de R$ 2.00'.format(bank_notes_2))

# Imprime a quantidade de cada moeda
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(coins_1))
print('{} moeda(s) de R$ 0.50'.format(coins_05))
print('{} moeda(s) de R$ 0.25'.format(coins_025))
print('{} moeda(s) de R$ 0.10'.format(coins_010))
print('{} moeda(s) de R$ 0.05'.format(coins_005))
print('{} moeda(s) de R$ 0.01'.format(coins_001))